# Import needed packages
import numpy as np
from football_models import *


class FootballPlay(object):

    def __init__(self, ball_on, team_w_ball, team_wo_ball, play_type):

        self._ball_on = ball_on
        self._points = 0
        self.team_w_ball = team_w_ball
        self.team_wo_ball = team_wo_ball
        self.outcome = PredictPlay(ball_on, team_w_ball, team_wo_ball, play_type)
        self.result = "not yet run"
        self.play_type = play_type

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
        if new_points < 0:
            raise ValueError("Invalid points")
        self._points = new_points

    @property
    def event_flag(self):
        return self.outcome.event_flag

    def run_play(self):
        self.outcome.predict()
        self._evaluate_play()    
        
# Children of FootballPlay
class RegularTeam(FootballPlay):

    def __init__(self, ball_on, down, to_gain, team_w_ball, team_wo_ball, play_type):

        # Public attributes
        FootballPlay.__init__(self, ball_on, team_w_ball, team_wo_ball, play_type)
        self.down = down
        self.to_gain = to_gain
        
    @property
    def yards(self):
        return self.outcome.gain

    def _evaluate_play(self):

        if self.ball_on + self.yards >= 100:
            self.result = "touchdown"
            self.points = 6
            
        elif self.to_gain - self.yards <= 0:
            self.result = "first down"
            self.points = 0
            
        else:
            self.result = "next down"
            self.points = 0


class KickReturnTeam(FootballPlay):

    def __init__(self, ball_on, team_w_ball, team_wo_ball, play_type):

        FootballPlay.__init__(self, ball_on, team_w_ball, team_wo_ball, play_type)

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
        
    def _evaluate_play(self):

        self.ball_on = 100 - self.ball_on - self.kick_length + self.return_yards

        if self.ball_on >= 100:
            self.points = 6
            self.result = "touchdown"

        self.points = 0
        self.result = "drive start"


class PlaceKickTeam(FootballPlay):

    def __init__(self, ball_on, team_w_ball, team_wo_ball, play_type):

        FootballPlay.__init__(self, ball_on, team_w_ball, team_wo_ball, play_type)
        kick_length = 100 - self.ball_on + 25 

    @property
    def yards(self):
        
        return 100 - self.ball_on + 25

    @property
    def good(self):

        return self.outcome.good

    def _evaluate_play(self):

        if self.play_type == "extra point attempt":
            if self.good:
                self.points = 1
            
            else:
                self.points = 0

        else:
            if self.good:
                self.points = 3
                self.result = "field goal good"

            else:
                self.points = 0
                self.result = "field goal missed"

