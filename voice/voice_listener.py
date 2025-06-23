# voice/voice_listener.py

import speech_recognition as sr
from rituals.ritual_registry import RitualRegistry

class VoiceListener:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        self.rituals = RitualRegistry()

    def listen_for_ritual(self):
        print("[VoiceListener] Listening for ritual invocation...")
        with self.microphone as source:
            audio = self.recognizer.listen(source)

        try:
            phrase = self.recognizer.recognize_google(audio).lower()
            print(f"[VoiceListener] Heard phrase: {phrase}")
            return self.rituals.cast_ritual(phrase)
        except sr.UnknownValueError:
            return "[VoiceListener] Could not understand audio."
        except sr.RequestError as e:
            return f"[VoiceListener] API error: {e}"
