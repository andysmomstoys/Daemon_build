from unimind.core import Unimind
from voice.voice_listener import start_voice_listener
from scrolls.scroll_engine import execute_scroll
from prometheus.specialties import Prometheus
from codex.ingestion import CodexIngestor
from memory_tree.memory_logger import log_memory
from optimizer.auto_upgrade import auto_optimize
from backup.self_restore import initialize_backup

if __name__ == "__main__":
    print("🌞 Prometheus Daemon v2 Booting...")

    # Initialize core systems
    mind = Unimind()
    prom = Prometheus(mind)

    # Connect subsystems
    start_voice_listener(callback=execute_scroll)
    CodexIngestor.load_documents()
    log_memory("Daemon started.")
    auto_optimize()
    initialize_backup()

    # Keep running
    while True:
        prom.pulse()# main.py
# Auto-generated logic for main.py in 

