# scrolls/trigger_manager.py

from memory_tree.memory_logger import log_memory

def trigger_scroll(scroll_name, reason="user_request"):
    print(f"[TriggerManager] Scroll '{scroll_name}' invoked due to: {reason}")
    log_memory(event=f"Triggered scroll: {scroll_name}", metadata={"reason": reason})
