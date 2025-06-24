# sensors/audio.py
import pyaudio
import numpy as np

def detect_volume_threshold(threshold=300):
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)
    
    print("[Audio Sensor] Listening for loud input...")
    try:
        while True:
            data = np.frombuffer(stream.read(1024), dtype=np.int16)
            volume = np.linalg.norm(data)
            if volume > threshold:
                print(f"[ALERT] Volume spike detected: {volume}")
                return "LOUD_EVENT"
    finally:
        stream.stop_stream()
        stream.close()
        p.terminate()
