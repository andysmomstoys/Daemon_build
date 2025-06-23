from unimind.core import Unimind
from prometheus.specialties import PrometheusSpecialties
from codex.ingestion import ingest_documents
from voice.voice_listener import start_voice_listener
from emotion.emotion_engine import EmotionEngine
from rituals.ritual_registry import RitualRegistry
from introspection.personality_tracker import PersonalityTracker
from memory_tree.memory_logger import MemoryLogger
from optimizer.auto_upgrade import run_auto_optimization
from scrolls.scroll_engine import ScrollEngine
from sensors.vision import VisionSensor
import threading

if __name__ == "__main__":
    print("[Daemon] Starting Prometheus daemon...")
    
    unimind = Unimind()
    prom = PrometheusSpecialties()
    emotions = EmotionEngine()
    memory = MemoryLogger()
    rituals = RitualRegistry()
    scrolls = ScrollEngine()
    vision = VisionSensor()

    # Launch sensors and modules
    threading.Thread(target=start_voice_listener, daemon=True).start()
    threading.Thread(target=vision.classify_surroundings, daemon=True).start()
    threading.Thread(target=run_auto_optimization, daemon=True).start()

    # Load Codex documents
    ingest_documents("codex/data/")

    # Introspection loop
    personality = PersonalityTracker()
    while True:
        personality.log_state()
        unimind.reflect()
