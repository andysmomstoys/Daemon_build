# scrolls/scroll_condition.py

class ScrollCondition:
    def __init__(self, check_function):
        self.check_function = check_function

    def is_met(self, context):
        return self.check_function(context)
