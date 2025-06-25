# voice/voice_listener.py

import speech_recognition as sr
from rituals.ritual_registry import RitualRegistry

def start_voice_listener():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()
    rituals = RitualRegistry()

    print("[VoiceListener] Listening for ritual invocation...")
    with microphone as source:
        audio = recognizer.listen(source)

    try:
        phrase = recognizer.recognize_google(audio).lower()
        print(f"[VoiceListener] Heard phrase: {phrase}")
        return rituals.cast_ritual(phrase)
    except sr.UnknownValueError:
        return "[VoiceListener] Could not understand audio."
    except sr.RequestError as e:
        return f"[VoiceListener] API error: {e}"
