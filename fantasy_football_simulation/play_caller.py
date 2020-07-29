from .football_play import *
import numpy as np



class PlayCaller:

    def __init__(self, ball_on):
        self.ball_on = ball_on
        
        
    def call_play(self, down, to_gain):
        
        self.down = down
        self.to_gain = to_gain
        
        #check for 4th down
        if self.down == 4:
        #punt, field goal, or go for it?
            if self.ball_on <= 50:
                self.play_call = "punt"
            elif (self.ball_on > 50 and self.to_gain <= 2) or (self.ball_on >= 95):
                self.play_call = RunPlay(self.ball_on, self.down, self.to_gain)
            elif self.ball_on >= 65:
                self.play_call = FieldGoal(self.ball_on)
            else:
                self.play_call = "punt"
           

        #else call run or pass play
        else:
            n = int(np.random.binomial(1, .5, 1))
            if n == 1:
                self.play_call = RunPlay(self.ball_on, self.down, self.to_gain)
            else:                
                self.play_call = PassPlay(self.ball_on, self.down, self.to_gain)
        
    def call_change_possession(self, change_type):
        
        if change_type == "punt":
            self.play_call = Punt(self.ball_on)
        elif change_type == "turnover on downs":
            self.play_call = Turnover(self.ball_on)
        else:
            self.play_call = KickOff(self.ball_on)