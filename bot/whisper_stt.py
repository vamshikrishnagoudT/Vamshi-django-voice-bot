import whisper

# Load the model (use "tiny" for faster results, "small" for better accuracy)
model = whisper.load_model("tiny")

def transcribe_audio(audio_path):
    result = model.transcribe(audio_path)
    return result["text"]
