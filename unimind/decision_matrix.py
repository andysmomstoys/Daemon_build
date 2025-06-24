# unimind/decision_matrix.py

class DecisionMatrix:
    def __init__(self):
        self.weights = {
            'logic': 0.4,
            'emotion': 0.2,
            'memory': 0.3,
            'intuition': 0.1
        }

    def evaluate(self, inputs):
        score = 0
        for key, value in inputs.items():
            score += self.weights.get(key, 0) * value
        return score

    def choose(self, options):
        scored = {k: self.evaluate(v) for k, v in options.items()}
        return max(scored, key=scored.get)
