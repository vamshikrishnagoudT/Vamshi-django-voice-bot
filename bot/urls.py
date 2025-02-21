from django.urls import path
from .views import speech_to_text, process_text, get_speech_file
from .views import analytics_dashboard
urlpatterns = [
    path("stt/", speech_to_text, name="speech_to_text"),  # Speech-to-Text API
    path("nlu/", process_text, name="process_text"),  # NLP Processing API   
    path("", get_speech_file, name="text_to_speech"),  # TTS API (returns audio)
]


urlpatterns += [
    path("dashboard/", analytics_dashboard, name="analytics_dashboard"),
]