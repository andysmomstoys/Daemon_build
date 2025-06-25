# scrolls/scroll_action.py

class ScrollAction:
    def __init__(self, action_function):
        self.action_function = action_function

    def execute(self, *args, **kwargs):
        return self.action_function(*args, **kwargs)
