
from football_drive import FootballDrive
import numpy as np




class ScoreBoard:

    def __init__(self):

        self.score = [0, 0]
        self.game_length = predict_game_length()
        self.half = 1
        
        self._plays_in_half = [self.game_length // 2] * 2
        self.possession = 0
        self.ball_on = 20
        self.change_type = "kickoff"
        
        self.drive_log = list() 
        
    @property
    def home_score(self):
        return self.score[0]
     
    @property
    def away_score(self):
        return self.score[0]
        
    @property
    def time_in_half(self):
        return self.plays_in_half > 0
        
    @property
    def plays_in_half(self):
        return self._plays_in_half[self.half - 1]
    
    @plays_in_half.setter
    def plays_in_half(self, new_plays_in_half):
        
        if new_plays_in_half < -1:
            raise ValueError("Invalid plays in half")
        self._plays_in_half[self.half - 1] = new_plays_in_half      
                
                
    @property
    def defense(self):
        return abs(self.possession - 1)
        
class GameManager:

    def __init__(self):
        self.type = "GameManager"
    
    def update_scoreboard(self, scoreboard, drive):
    
        scoreboard.drive_log.append(drive)
        scoreboard.plays_in_half -= drive.play_count
        turnover_types = ["turnover on downs", "fumble", "interception", "missed field goal"]    
    
        if drive.result == "punt":
            scoreboard.change_type = "punt"
            scoreboard.ball_on = drive.ending_field_position
            self.__flip_possession(scoreboard)
            
        elif drive.result in turnover_types:
            scoreboard.change_type = "turnover"
            scoreboard.ball_on = drive.turnover_position
            self.__flip_possession(scoreboard)
            
        elif drive.points > 0:
            scoreboard.score[scoreboard.possession] += drive.points
            scoreboard.change_type = "kickoff"
            self.ball_on = 20
            self.__flip_possession(scoreboard)
            
        else:
            pass
    
    def time_in_half(self, scoreboard):
        
        return scoreboard.time_in_half
    
    def run_drive(self, scoreboard, matchup):
        
        current_drive = FootballDrive(
            ball_on = scoreboard.ball_on, plays_remain = scoreboard.plays_in_half,
            change_type = scoreboard.change_type, team_w_ball = matchup[scoreboard.possession], 
            team_wo_ball = matchup[scoreboard.defense], score = scoreboard.score
            )

        return current_drive

    def change_half(self, scoreboard):
        scoreboard.half += 1
        scoreboard.possession = 1
        scoreboard.change_type = "kickoff"
        scoreboard.ball_on = 20
    
    def __flip_possession(self, scoreboard):

        scoreboard.possession = abs(scoreboard.possession - 1)



def predict_game_length():

    return 150
