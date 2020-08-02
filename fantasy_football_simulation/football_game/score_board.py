class ScoreBoard:
    """
    
    Attributes
    ----------
    
    """
    def __init__(self):

        self.score = [0, 0]
        self.game_length = predict_game_length()
        self.half = 1
        
        self._plays_in_half = [self.game_length // 2] * 2
        self.possession = 0
        self.ball_on = 20
        self.change_type = "kickoff"
        
        self.drive_log = list() 
        
    @property
    def home_score(self):
        return self.score[0]
     
    @property
    def away_score(self):
        return self.score[0]
        
    @property
    def time_in_half(self):
        return self.plays_in_half > 0
        
    @property
    def plays_in_half(self):
        return self._plays_in_half[self.half - 1]
    
    @plays_in_half.setter
    def plays_in_half(self, new_plays_in_half):
        
        if new_plays_in_half < -1:
            raise ValueError("Invalid plays in half")
        self._plays_in_half[self.half - 1] = new_plays_in_half      
                
                
    @property
    def defense(self):
        return abs(self.possession - 1)
        
        
        
def predict_game_length():

    return 150