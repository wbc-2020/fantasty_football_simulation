
from football_play import KickReturnTeam

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