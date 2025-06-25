# lam/symbolic_state.py

symbolic_state = {
    "history": [],
    "current_context": {},
    "flags": {}
}

def update_state_with_input(user_input):
    try:
        # Log input history
        symbolic_state["history"].append(user_input)
        symbolic_state["last_input"] = user_input

        # Basic symbolic parsing (placeholder for future logic)
        if "learn" in user_input.lower():
            symbolic_state["current_context"]["mode"] = "learning"
            symbolic_state["flags"]["is_learning"] = True
        elif "task" in user_input.lower():
            symbolic_state["current_context"]["mode"] = "task_execution"
            symbolic_state["flags"]["has_active_task"] = True
        else:
            symbolic_state["current_context"]["mode"] = "idle"
            symbolic_state["flags"].clear()

        print(f"[SymbolicState] Updated state: {symbolic_state}")

    except Exception as e:
        print(f"[SymbolicState Error] Failed to update state: {e}")