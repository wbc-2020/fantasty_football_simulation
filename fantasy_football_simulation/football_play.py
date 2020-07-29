import numpy as np
from .football_models import *

class FootballPlay(object):
    """
    a general class for a football play
    
    attributes:
        ball_on - passed in
        scoring - initialized to false
    """

    def __init__(self, ball_on):
        """
        constructor for FootballPlay class
        """
        self.ball_on = ball_on
        self.scoring = False   
    

class RegularFootballPlay(FootballPlay):
    """
    class for regular offensive play
    
    attributes:
        down - passed in
        to_gain - passed in 
    """

    def __init__(self, ball_on, down, to_gain):
        """
        constructor for RegularFootballPlay class
        """
        
        FootballPlay.__init__(self, ball_on)
        self.down = down
        self.to_gain = to_gain

    def evaluate_play(self, gain):
        """
        decide result of offensive play
        """         
        if self.ball_on + gain >= 100:
            self.result = "touchdown"
            self.gain = 100 - self.ball_on
            self.points = 6
            self.scoring = True
        elif self.to_gain - gain <= 0:
            self.result = "first down"
            self.points = 0
        else:
            self.result = "next down"
            self.points = 0


    
class RunPlay(RegularFootballPlay):
    """
    doc string
    """   
    def __init__(self, ball_on, down, to_gain):
        """
        doc string
        """     
        RegularFootballPlay.__init__(self, ball_on, down, to_gain)
        self.play_type = "run"

    def run_play(self):
        """
        doc string
        """         
        self.gain = predict_run()
        
        self.evaluate_play(self.gain)
        
    
    
class PassPlay(RegularFootballPlay):
    """
    doc string
    """    
    def __init__(self, ball_on, down, to_gain):
        """
        doc string
        """     
        RegularFootballPlay.__init__(self, ball_on, down, to_gain)
        self.play_type = "pass"

    def run_play(self):
        """
        doc string
        """         
        self.gain = predict_pass()
        
        self.evaluate_play(self.gain)
        
       

class FieldGoal(FootballPlay):
    """
    doc string
    """
    def __init__(self, ball_on):
        """
        doc string
        """         
        FootballPlay.__init__(self, ball_on)
        self.type = "field goal attempt"
        
    def run_play(self):
        """
        doc string
        """     
        self.points = 3
        self.scoring = True
        self.good = True
        self.result = "field goal"



class ChangeOfPossessionPlay(FootballPlay):
    """
    doc string
    """
    def __init__(self, ball_on):
        """
        doc string
        """         
        FootballPlay.__init__(self, ball_on) 
        
    def evaluate_play(self):
        """
        doc string
        """         
        self.points = 0      
        
        
class KickOff(ChangeOfPossessionPlay):
    """
    doc string
    """
    def __init__(self, ball_on):
        """
        doc string
        """         
        ChangeOfPossessionPlay.__init__(self, ball_on)
        self.play_type = "kickoff return"

    def run_play(self):
        """
        doc string
        """      
        self.gain = 5
        self.kick_length = 60
        self.ball_on = 100 - self.ball_on - self.kick_length + self.gain


class Punt(ChangeOfPossessionPlay):
    """
    doc string
    """
    def __init__(self, ball_on):
        """
        doc string
        """         
        ChangeOfPossessionPlay.__init__(self, ball_on)
        self.play_type = "punt return"

    def run_play(self):   
        """
        doc string
        """         
        self.gain = 5
        self.kick_length = 40
        self.ball_on = 100 - self.ball_on - self.kick_length + self.gain
        
        
class Turnover(ChangeOfPossessionPlay):
    """
    doc string
    """   
    def __init__(self, ball_on):
        """
        doc string
        """         
        ChangeOfPossessionPlay.__init__(self, ball_on)
        self.play_type = "turnover"
        
    def run_play(self):   
        """
        doc string
        """ 
        self.ball_on = 100 - self.ball_on
        
        
        
        
        
        
        