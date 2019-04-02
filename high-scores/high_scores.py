class HighScores(object):
    def __init__(self, scores):
        self.scores = scores

    def personal_best(self):
        return max(self.scores)

    def latest(self):
        return self.scores[-1]

    def personal_top(self):
        return sorted(self.scores, reverse=True)[:3]

    def report(self):
        if self.latest() == self.personal_best()
            return self.latest()
        else:
            return %(self.latest(), self.highest() - self.latest())


