
import random

EMOTIONS = ["calm", "curious", "focused", "anxious", "inspired"]

def detect_emotion(audio_input=None, context=None):
    return random.choice(EMOTIONS)

def log_emotion(emotion):
    with open("emotion_log.txt", "a") as f:
        f.write(f"{emotion}\n")
