
from football_play import KickReturnTeam
import numpy as np


class ChangeOfPossession:

    def __init__(self, change_type, ball_on, team_w_ball, team_wo_ball):
        
        self.type = "change of possesion"
        self.change_type = change_type
        self.ball_on = ball_on
        self.team_w_ball = team_w_ball
        self.team_wo_ball = team_wo_ball

    def change_possession(self):

        turnover_types = ["turnover"]

        if self.change_type == "punt":
            self.play_call = KickReturnTeam(self.ball_on, self.team_w_ball, self.team_wo_ball, play_type = "punt return")
            
        elif self.change_type in turnover_types :
            self.play_call = FlipField(self.ball_on)

        else:
            self.play_call = KickReturnTeam(self.ball_on, self.team_w_ball, self.team_wo_ball, play_type = "kickoff return")


class FlipField:

    def __init__(self, ball_on):

        self.ball_on = ball_on
        self.play_type = "turnover"

    def run_play(self):

        self.ball_on = 100 - self.ball_on
        self.result = "NA"




def flip_coin():

    return int(np.random.binomial(1, .5, 1))


def coin_toss():

        coin_winner = flip_coin()

        possession, defense = predict_coin_decision(coin_winner)

        return [coin_winner, possession, defense]

def predict_game_length():

    return 150


def predict_coin_decision(coin_winner):

    possession = abs(coin_winner - 1)
    defense = coin_winner

    return [possession, defense]
