class ScoreBoard:
    """Score object for football game
    
    Attributes
    ----------
    score
    home_score
    away score
    half
    possession
    change_type
    drive_log
    down
    to_gain
    time_in_half
    plays_in_half
    defense
    
    Methods
    -------
    add_safety()
    add_touchdown()
    add_field_goal()
    add_extra_point()
    first_down()
    deduct_time()
    change_half()
    turnover()
    punt()
    
    Raises
    ------
    """
    def __init__(self):
        self.score = [0, 0]
        self.game_length = predict_game_length()
        self._half = 1

        self._plays_in_half = [self.game_length // 2] * 2
        self._possession = 0
        self.change_type = "kickoff"

        self.drive_log = list() 
        
        self._down = 1
        self.to_gain = 10
    
    @property
    def home_score(self):
        return self.score[0]

    @property
    def away_score(self):
        return self.score[1]

    @property
    def possession(self):
        return(self._possession)
    
    @possession.setter
    def possession(self, new_possession):
        if new_possession not in [0, 1]:
            raise ValueError("Invalid possesion")
        self._possession = new_possession

    @property
    def down(self):
        return self._down

    @down.setter
    def down(self, new_down):
        if new_down not in [1, 2, 3, 4]:
            raise ValueError("Invalid down")
        self._down = new_down

    @property
    def half(self):
        return self._half
        
    @half.setter
    def half(self, new_half):
        if new_half not in [1,2]:
            raise ValueError("Invalid half")
        self._half = new_half

    @property
    def to_gain(self):
        return self._to_gain
        
    @to_gain.setter
    def to_gain(self, new_to_gain):
        if new_to_gain < 1:
            raise ValueError("Invalid to gain")
        self._to_gain = new_to_gain

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
        if points < 0:
            raise ValueError("Invalid points")
        self.score[side] += points
        
    def add_safety(self):
        self._add_points(self.defense, 2)
        self.change_type  = "punt"
        self.flip_possession
        
    def add_touchdown(self):
        self._add_points(self.possession, 6)
        self.change_type = "kickoff"
        self.flip_possession()

    def add_field_goal(self):
        self._add_points(self.possession, 3)
        self.change_type = "kickoff"
        self.flip_possession()

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

    def turnover(self):
        self.change_type = "turnover"
        self.flip_possession()

    def punt(self):
        self.change_type = "punt"
        self.flip_possession()

def predict_game_length():
    return 150
