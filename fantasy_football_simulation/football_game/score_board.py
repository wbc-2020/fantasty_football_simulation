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
        self._possession = 0
        self.ball_on = 20
        self.change_type = "kickoff"
        
        self.drive_log = list() 
        
        self.down = 1
        self.to_gain = 10
    
    @property
    def home_score(self):
        return self.score[0]
     
    @property
    def possession(self):
    
        return(self._possession)
    
    @possession.setter
    def possession(self, new_possession):
    
        if new_possession not in [0, 1]:
            print(f"Invalid possesion of : {new_possession}")
            raise ValueError("Invalid possesion")

        self._possession = new_possession

    @property
    def away_score(self):
        return self.score[1]
        
    @property
    def time_in_half(self):
        return self.plays_in_half > 0
        
    @property
    def plays_in_half(self):
        return self._plays_in_half[self.half - 1]
    
    @plays_in_half.setter
    def plays_in_half(self, new_plays_in_half):
        
        if new_plays_in_half < 0:
            raise ValueError("Invalid plays in half")
        self._plays_in_half[self.half - 1] = new_plays_in_half                   
                
    @property
    def defense(self):
        return abs(self.possession - 1)
     
    # Methods
    def _add_points(self, side, points):
    
        self.score[side] += points
    
    
    def add_safety(self):

        self._add_points(self.defense, 2) 
        
    def add_touchdown(self):

        self._add_points(self.possession, 6)
        
    def add_field_goal(self):
       
        self._add_points(self.possession, 3)
        
    def add_extra_point(self):
    
        self._add_points(self.possession, 1)

    def flip_possession(self):
        self.possession = abs(self.possession - 1)
        self.first_down()

    def first_down(self):
        self.down = 1
        self.to_gain = 10

    def deduct_time(self):
        
        self.plays_in_half -= 1

    def change_half(self):
    
        self.half += 1
        self.possession = 1
        self.change_type = "kickoff"
    
def predict_game_length():

    return 150