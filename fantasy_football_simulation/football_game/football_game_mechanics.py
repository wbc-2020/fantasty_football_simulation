
from football_drive import FootballDrive
from score_board import ScoreBoard
import numpy as np

        
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
            scoreboard = scoreboard,
            matchup = matchup
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
