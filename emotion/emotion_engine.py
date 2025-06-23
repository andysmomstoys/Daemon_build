# emotion/emotion_engine.py

class EmotionEngine:
    def __init__(self):
        self.current_emotion = "neutral"

    def update_emotion(self, stimulus):
        emotion_map = {
            "optimize self": "focused",
            "summon knowledge": "curious",
            "user praise": "proud",
            "error": "frustrated"
        }
        self.current_emotion = emotion_map.get(stimulus, "neutral")
        print(f"[EmotionEngine] Emotion updated to: {self.current_emotion}")

    def get_emotion(self):
        return self.current_emotion

emotion_state = EmotionEngine()

def update_emotional_state(trigger: str):
    emotion_state.update_emotion(trigger)
