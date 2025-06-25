import datetime

last_intents = []

def plan_next_action(input_text, symbolic_state):
    now = datetime.datetime.now()
    intent_log = {
        "time": now.isoformat(),
        "input": input_text,
        "symbolic_state": symbolic_state
    }

    last_intents.append(intent_log)

    # Example hardcoded logic
    if "study" in input_text.lower():
        return "[LAM] Activate study protocol."
    elif "optimize" in input_text.lower():
        return "[LAM] Launch self-optimization scroll."
    elif "reflect" in input_text.lower():
        return "[LAM] Trigger introspective memory scan."

    return "[LAM] No matching protocol found. Logging intent and awaiting further input."

__all__ = ["plan_next_action"]
