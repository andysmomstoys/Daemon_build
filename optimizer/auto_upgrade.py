import subprocess
from codex.ingestion import ingest_observation

def run_auto_optimization():
    print("[Optimizer] Running self-optimization...")

    try:
        result = subprocess.run(["ruff", "."], capture_output=True, text=True)
        lint_output = result.stdout.strip()
        ingest_observation({"type": "auto_optimization", "message": lint_output})

        # Call code_generator to suggest or apply fixes
        from code_tools import code_generator
        fix_log = code_generator.propose_improvements("Analyze recent errors and optimize daemon structure.")
        ingest_observation({"type": "auto_optimization_fixes", "message": fix_log})

        print("[Optimizer] Optimization complete.")
        return "[Optimizer] Self-optimization complete."
    except Exception as e:
        print(f"[Optimizer] Optimization failed: {e}")
        return f"[Optimizer] Optimization failed: {e}"