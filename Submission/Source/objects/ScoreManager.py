class ScoreManager:
    def __init__(self, eventManager):
        self.score = 0
        eventManager.subscribe("COIN_EATEN", self.OnCoinEaten)
    
    def OnCoinEaten(self, data):
        self.score += 1