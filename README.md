# Django Voice Bot 🎤🗣️  

An AI-powered **voice bot** built using Django that can transcribe speech, understand natural language, generate responses, and convert text to speech.  

## 🚀 Features  
- **Speech-to-Text (STT):** Converts voice input to text using OpenAI Whisper.  
- **Natural Language Understanding (NLU):** Detects user intent using NLP models.  
- **Response Generation:** Uses rule-based logic or GPT-2 to generate responses.  
- **Text-to-Speech (TTS):** Converts responses into speech using `pyttsx3`.  
- **Backend Integration:** Fetches data dynamically from a database.  
- **Analytics Dashboard (Optional):** Tracks user interactions and bot performance.  

## 🛠️ Technologies Used  
- **Python** (Django Framework)  
- **OpenAI Whisper** (Speech-to-Text)  
- **Hugging Face Transformers** (NLP)  
- **Pyttsx3** (Text-to-Speech)  
- **PostgreSQL / SQLite** (Database)  
- **Postman** (API Testing)  

## 📦 Installation  

### **Step 1: Clone the Repository**  
```bash
git clone https://github.com/YOUR_USERNAME/django-voice-bot.git
cd django-voice-bot
🎯 API Endpoints
Endpoint	Method	Description
/api/stt/	POST	Converts speech to text
/api/nlu/	POST	Processes user input and detects intent
/api/tts/	POST	Converts text responses to speech
/api/get-audio/	GET	Retrieves the generated speech audio
🧪 Testing with Postman
Open Postman and create a POST request to http://127.0.0.1:8000/api/stt/.
Upload an audio file (.wav format) as audio in form-data.
Click Send and get the transcribed text response!
🤝 Contribution
Want to improve this project? Feel free to fork, submit pull requests, or raise issues!

📜 License
This project is open-source under the MIT License.