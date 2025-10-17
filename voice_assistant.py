import speech_recognition as sr
from gtts import gTTS
import playsound, tempfile, os

def listen_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎙️ Listening...")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print(f"🗣️ You said: {text}")
        return text
    except sr.UnknownValueError:
        return "Sorry, I could not understand your voice."
    except sr.RequestError:
        return "Speech recognition service unavailable."

def speak_text(text):
    tts = gTTS(text=text, lang='en')
    with tempfile.NamedTemporaryFile(delete=True) as fp:
        temp_path = f"{fp.name}.mp3"
        tts.save(temp_path)
        playsound.playsound(temp_path)
        os.remove(temp_path)
