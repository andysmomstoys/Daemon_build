# code_tools/code_generator.py

import os
from datetime import datetime

def propose_improvements(context=""):
    log_path = "logs/improvement_history.log"
    os.makedirs("logs", exist_ok=True)
    with open(log_path, "a") as f:
        f.write(f"{datetime.now().ctime()} - Proposed improvement: {context}\n")
    print(f"[CodeGenerator] Logged improvement for: {context}")
    return f"Proposed improvement logged: {context}"