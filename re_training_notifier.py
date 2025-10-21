import numpy as np

class Retraining_notifier:
    def __init__(self, size=10, threshold=0.9):
        self.size = size
        self.reward_history = np.zeros(size)
        self.threshold = threshold
        self.cnt = 0
        self.ready = False
    
    def store(self, reward):
        self.reward_history[self.cnt % self.size] = reward
        self.cnt += 1
    
    def require_retrain(self):
        return np.mean(self.reward_history) < self.threshold and self.cnt >= self.size