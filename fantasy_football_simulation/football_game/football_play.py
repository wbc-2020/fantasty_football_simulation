# Import needed packages
import numpy as np
from football_models import *


class FootballPlay(object):

    def __init__(self, ball_on, team_w_ball, team_wo_ball, play_type):

        self._ball_on = ball_on
        self.team_w_ball = team_w_ball
        self.team_wo_ball = team_wo_ball
        self.outcome = PredictPlay(ball_on, team_w_ball, team_wo_ball, play_type)
        self.play_type = play_type
        self._result = None
        self._points = None
        self.turnover = False
        

    @property
    def ball_on(self):
    
        return self._ball_on

    @ball_on.setter
    def ball_on(self, new_ball_on):
    
        if new_ball_on > 100 or new_ball_on < 0:
            raise ValueError("Invalid ball on")
        self._ball_on = new_ball_on

    @property
    def points(self):
        return self._points

    @points.setter
    def points(self, new_points):
        if new_points not in [0, 1, 2, 3, 6]:
            raise ValueError("Invalid points")
        self._points = new_points

    @property
    def result(self):

        return self._result
 
    @result.setter
    def result(self, new_result):

        self._result = new_result

    @property
    def event_flag(self):
        return self.outcome.event_flag

    def run_play(self):
        self.outcome.predict()   

    def label_result(self, result):
    
        self.result = result
        
    
# Children of FootballPlay
class RegularTeam(FootballPlay):

    def __init__(self, ball_on, down, to_gain, team_w_ball, team_wo_ball, play_type):

        # Public attributes
        FootballPlay.__init__(self, ball_on, team_w_ball, team_wo_ball, play_type)
        self.down = down
        self.to_gain = to_gain
        self.class_type = "RegularTeam"
        
    @property
    def yards(self):
        return self.outcome.gain

class KickReturnTeam(FootballPlay):

    def __init__(self, ball_on, team_w_ball, team_wo_ball, play_type):

        FootballPlay.__init__(self, ball_on, team_w_ball, team_wo_ball, play_type)
        self.class_type = "KickReturnTeam"

    # Used by higher level classes
    @property
    def yards(self):
    
        return self.return_yards
        
    @property
    def kick_length(self):
        return self.outcome.kick_length
        
    @property
    def return_yards(self):
    
        return self.outcome.return_yards
        

class PlaceKickTeam(FootballPlay):

    def __init__(self, ball_on, team_w_ball, team_wo_ball, play_type):

        FootballPlay.__init__(self, ball_on, team_w_ball, team_wo_ball, play_type)
        self.class_type = "PlaceKickTeam"
        kick_length = 100 - self.ball_on + 25 

    @property
    def yards(self):
        
        return 100 - self.ball_on + 25

    @property
    def good(self):

        return self.outcome.good



