from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Conversation, User, ConversationHistory
import openai
from google.cloud import speech, texttospeech
from langchain.chains import ConversationalChain
from langchain.memory import ConversationBufferMemory
from langchain.llms import OpenAI

# Configure logging
logger = logging.getLogger(__name__)
openai.api_key = settings.OPENAI_API_KEY


@api_view(['POST'])
def chat_view(request):
    user_id = request.data.get('user_id')
    user_input = request.data.get('user_input')
    user = User.objects.get(id=user_id)

    # Retrieve conversation history
    history = ConversationHistory.objects.filter(user=user).order_by('-id').first()
    if history:
        messages = history.messages
    else:
        messages = []
        
    system_message = {
        "role": "system",
        "content": "You are an adaptive language-learning AI designed to assist users in practicing and learning a new language. ..."
    }
    messages.insert(0, system_message)  # Insert the system message at the beginning

    # Initialize LangChain with OpenAI
    llm = OpenAI(api_key=settings.OPENAI_API_KEY)
    memory = ConversationBufferMemory(messages=messages)

    # Create a conversational chain
    conversational_chain = ConversationalChain(llm=llm, memory=memory)
    ai_response = conversational_chain.run(user_input)

    # Save the conversation
    Conversation.objects.create(user=user, user_input=user_input, ai_response=ai_response)

    # Update conversation history
    if history:
        history.messages.append({"role": "user", "content": user_input})
        history.messages.append({"role": "assistant", "content": ai_response})
        history.save()
    else:
        ConversationHistory.objects.create(user=user, messages=[{"role": "user", "content": user_input}, {"role": "assistant", "content": ai_response}])

    return Response({"ai_response": ai_response})

@api_view(['POST'])
def speech_to_text(request):
    client = speech.SpeechClient()
    audio = request.data.get('audio_content')  # Base64 audio content
    audio = speech.RecognitionAudio(content=audio)

    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code='en-US'
    )

    response = client.recognize(config=config, audio=audio)
    transcript = response.results[0].alternatives[0].transcript
    return Response({"transcript": transcript})

@api_view(['POST'])
def text_to_speech(request):
    text = request.data.get('text')
    user_id = request.data.get('user_id')

    client = texttospeech.TextToSpeechClient()
    input_text = texttospeech.SynthesisInput(text=text)

    voice = texttospeech.VoiceSelectionParams(
        language_code='en-US',
        ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
    )

    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    response = client.synthesize_speech(
        input=input_text, voice=voice, audio_config=audio_config
    )

    audio_content = response.audio_content
    return Response({"audio_content": audio_content})
