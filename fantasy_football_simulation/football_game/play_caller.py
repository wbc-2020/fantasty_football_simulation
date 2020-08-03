from football_play import RegularTeam, PlaceKickTeam, KickReturnTeam
import numpy as np



class PlayCaller:
    """
    """
    
    def __init__(self, team_w_ball, team_wo_ball, score):
        """
        """
        
        self.team_w_ball = team_w_ball
        self.team_wo_ball = team_wo_ball
        self.score = score
        
    def call_play(self, ball_on, down, to_gain):
        """
        """
        
        self.ball_on = ball_on
        self.down = down
        self.to_gain = to_gain
        
        #check for 4th down
        if self.down == 4:
        #punt, field goal, or go for it?
            if self.ball_on <= 50:
                self.play_call = "punt"
            elif (self.ball_on > 50 and self.to_gain <= 2) or (self.ball_on >= 95):
                self.play_call = RegularTeam(self.ball_on, self.down, self.to_gain, 
                                             self.team_w_ball, self.team_wo_ball, play_type = "run attempt")
            elif self.ball_on >= 65:
                self.play_call = PlaceKickTeam(self.ball_on, self.team_w_ball, self.team_wo_ball, play_type = "field goal attempt")
            else:
                self.play_call = "punt"
           

        #else call run or pass play
        else:
            n = int(np.random.binomial(1, .5, 1))
            if n == 1:
                self.play_call = RegularTeam(self.ball_on, self.down, self.to_gain, 
                                             self.team_w_ball, self.team_wo_ball, play_type = "run attempt")

            else:
                self.play_call = RegularTeam(self.ball_on, self.down, self.to_gain, 
                                             self.team_w_ball, self.team_wo_ball, play_type = "pass attempt")

    def call_extra_point(self):

        ball_on = 20
        go_for_two = False

        if go_for_two:
            self.call_play(98, 1, 2)

        else:
            self.play_call = PlaceKickTeam(ball_on, self.team_w_ball, self.team_wo_ball, play_type = "extra point attempt")
        
        
    def call_kick_return(self, ball_on, play_type):
    
        if play_type == "kickoff":
            self.play_call = KickReturnTeam(ball_on, self.team_w_ball, self.team_wo_ball, play_type = "kickoff return")
            
        else:
            self.play_call = KickReturnTeam(ball_on, self.team_w_ball, self.team_wo_ball, play_type = "punt return")
            