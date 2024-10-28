from django.urls import path
from .views import chat_view, speech_to_text, text_to_speech

urlpatterns = [
    path('chat/', chat_view, name='chat'),  # Endpoint for chat interactions
    path('speech-to-text/', speech_to_text, name='speech_to_text'),  # Endpoint for speech-to-text
    path('text-to-speech/', text_to_speech, name='text_to_speech'),  # Endpoint for text-to-speech
]
