from django.shortcuts import render
from django.http import JsonResponse, FileResponse
from django.views.decorators.csrf import csrf_exempt
import os
import pyttsx3
from .nlu import classify_intent
from .whisper_stt import transcribe_audio
from transformers import pipeline
from .models import FAQ, UserQuery
from django.shortcuts import render
from django.db.models import Count
from .models import UserQuery
# Load the text generation model (GPT-2)
generator = pipeline("text-generation", model="gpt2")

# Function to generate speech from text
def text_to_speech(response_text, audio_filename="response_audio.wav"):
    engine = pyttsx3.init()
    engine.save_to_file(response_text, audio_filename)
    engine.runAndWait()
    return audio_filename

@csrf_exempt
def speech_to_text(request):
    if request.method == "POST":
        if request.FILES.get("audio"):
            audio_file = request.FILES["audio"]
            temp_audio_path = "temp_audio.wav"

            # Save the audio file temporarily
            with open(temp_audio_path, "wb") as f:
                f.write(audio_file.read())

            # Transcribe the audio file
            try:
                text = transcribe_audio(temp_audio_path)
                os.remove(temp_audio_path)  # Remove temporary audio file
                return JsonResponse({"transcribed_text": text})
            except Exception as e:
                return JsonResponse({"error": f"Error processing audio: {str(e)}"}, status=400)
        else:
            return JsonResponse({"error": "No audio file provided"}, status=400)

    return JsonResponse({"error": "Invalid request method"}, status=400)

# @csrf_exempt
# def process_text(request):
#     if request.method == "POST":
#         user_text = request.POST.get("text", "")
#         if not user_text:
#             return JsonResponse({"error": "Text is required"}, status=400)
        
#         # Get the intent of the user's message
#         intent = classify_intent(user_text)
        
#         # Generate a response based on intent
#         if intent == "greeting":
#             response = "I'm good, thanks for asking! How can I assist you today?"
#         elif intent == "account_info":
#             response = "I can help you with your account. Please provide your account details."
#         elif intent == "faq":
#             response = "I can answer frequently asked questions. What do you need help with?"
#         else:
#             # Use GPT-2 for a more natural response
#             gpt_response = generator(user_text, max_length=50, num_return_sequences=1)
#             response = gpt_response[0]["generated_text"]

#         # Convert response to speech
#         audio_file = text_to_speech(response)

#         # Return the intent, response, and speech file
#         return JsonResponse({
#             "intent": intent,
#             "response": response,
#             "audio_url": f"/media/{audio_file}"
#         })
    
#     return JsonResponse({"error": "Invalid request"}, status=400)
@csrf_exempt
def process_text(request):
    if request.method == "POST":
        user_text = request.POST.get("text", "")
        if not user_text:
            return JsonResponse({"error": "Text is required"}, status=400)

        # Check if the question exists in the database
        faq = FAQ.objects.filter(question__icontains=user_text).first()
        if faq:
            response = faq.answer
        else:
            # Use GPT-2 to generate a response
            gpt_response = generator(user_text, max_length=50, num_return_sequences=1)
            response = gpt_response[0]["generated_text"]

        # Save query and response to database
        UserQuery.objects.create(user_text=user_text, bot_response=response)

        # Convert response to speech
        audio_file = text_to_speech(response)

        return JsonResponse({
            "response": response,
            "audio_url": f"/media/{audio_file}"
        })
    
    return JsonResponse({"error": "Invalid request"}, status=400)
@csrf_exempt
def get_speech_file(request):
    """Serve the generated speech audio file."""
    audio_path = "response_audio.wav"
    if os.path.exists(audio_path):
        return FileResponse(open(audio_path, "rb"), content_type="audio/wav")
    else:
        return JsonResponse({"error": "Audio file not found"}, status=404)




def analytics_dashboard(request):
    total_queries = UserQuery.objects.count()
    top_queries = UserQuery.objects.values('user_text').annotate(count=Count('user_text')).order_by('-count')[:5]

    context = {
        'total_queries': total_queries,
        'top_queries': top_queries
    }
    return render(request, 'dashboard.html', context)
