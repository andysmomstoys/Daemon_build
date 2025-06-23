
SCROLLS = {}

def register_scroll(name, trigger_fn, execute_fn):
    SCROLLS[name] = {"trigger": trigger_fn, "execute": execute_fn}

def invoke_scroll(name, context):
    if name in SCROLLS:
        scroll = SCROLLS[name]
        if scroll["trigger"](context):
            return scroll["execute"](context)
    return None
