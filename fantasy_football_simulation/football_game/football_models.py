import numpy as np
from football_events import *


class PredictPlay:

    def __init__(self, ball_on, team_w_ball, team_wo_ball, play_type):

        self._ball_on = ball_on
        self.team_w_ball = team_w_ball
        self.team_wo_ball = team_wo_ball
        self.play_type = play_type
        self.event_log = list()
        self.kick_length = None
        self.return_yards = None

    @property
    def ball_on(self):

        return self._ball_on

    @ball_on.setter
    def ball_on(self, new_ball_on):

        if new_ball_on > 100 or new_ball_on < 0:
            raise ValueError("Invalid ball on")
        self._ball_on = new_ball_on

    def predict(self):
        
        if self.play_type == "run attempt":
            self.__predict_run()

        elif self.play_type == "pass attempt":
            self.__predict_pass()

        elif self.play_type == "fake field goal attempt":
            self.__predict_fake_fieldgoal()

        elif self.play_type == "fake punt attempt":
            self.__predict_fake_punt()

        elif self.play_type == "punt return":
            self.__predict_punt_return()

        elif self.play_type == "kickoff return":
            self.__predict_kick_return()

        elif self.play_type == "field goal attempt":
            self.__predict_field_goal()

        elif self.play_type == "extra point attempt":
            self.__predict_extra_point()

        else:
            pass

    # Play prediction models

    def __predict_run(self):

        gain = np.random.poisson(lam = 5)

        self.__check_gain(gain)

    def __predict_pass(self):

        gain = np.random.poisson(lam = 5)

        self.__check_gain(gain)

    def __predict_fake_fieldgoal(self):

        gain = 0

        self.__check_gain(gain)

    def __predict_fake_punt(self):

        gain = 0

        self.__check_gain(gain)

    def __predict_kick_return(self):

        max_kick_length = 100 - self.ball_on

        self.kick_length = 60

        if self.kick_length > max_kick_length:
            self.kick_length = max_kick_length

        self.return_yards = 5

        ball_on = 100 - self.ball_on - self.kick_length + self.return_yards

        if ball_on >= 100:
            self.return_yards = 100 - self.ball_on - self.kick_length

    def __predict_punt_return(self):

        max_kick_length = 100 - self.ball_on

        self.kick_length = 40

        if self.kick_length > max_kick_length:
            self.kick_length = max_kick_length

        self.return_yards = 5

        ball_on = 100 - self.ball_on - self.kick_length + self.return_yards

        if ball_on >= 100:
            self.return_yards = 100 - self.ball_on - self.kick_length

    def __predict_field_goal(self):

        self.good = True
        self.result = "field goal good"

    def __predict_extra_point(self):

        self.good = True
        self.result = "extra point good"

    # Class helper functions
    def __check_gain(self, gain):

        if self.ball_on + gain >= 100:
            self.gain = 100 - self.ball_on

        else: 
            self.gain = gain






















def predict_extra_point():
    good = True
    result = "field goal good"
    
    return [good, result]

def predict_two_point():    
    pass
    
