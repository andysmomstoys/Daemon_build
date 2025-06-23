# Main runtime loop for daemon_v2_origin

from unimind.core import Unimind
from codex.ingestion import CodexIngestor
from scrolls.scroll_engine import ScrollEngine

if __name__ == '__main__':
    unimind = Unimind()
    codex = CodexIngestor()
    scroll_engine = ScrollEngine(unimind, codex)

    unimind.bootstrap()
    codex.load_initial_knowledge()
    scroll_engine.run()
