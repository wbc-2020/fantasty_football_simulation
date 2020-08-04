
from football_drive import FootballDrive
from score_board import ScoreBoard
import numpy as np

        
class GameManager:

    def __init__(self):
        self.type = "GameManager"
    
    def update_results(self, scoreboard, drive, football):
    
        scoreboard.drive_log.append(drive)
        turnover_types = ["turnover on downs", "fumble", "interception", "missed field goal"]    
    
        if drive.result.result == "punt":
            scoreboard.change_type = "punt"
            football.flip_field()
            scoreboard.flip_possession()
            
        elif drive.result.result in turnover_types:
            scoreboard.change_type = "turnover"
            football.flip_field()
            scoreboard.flip_possession()
            
        elif drive.result.points > 0:
            scoreboard.score[scoreboard.possession] += drive.result.points
            scoreboard.change_type = "kickoff"
            football.position = 20
            scoreboard.flip_possession()
 
        elif drive.result.result == "safety":
            scoreboard.safety()
            scoreboard.change_type  = "punt"
            football.position = 20
            scoreboard.flip_possession
            
        else:
            pass
    
    def time_in_half(self, scoreboard):
        
        return scoreboard.time_in_half
    
    def run_drive(self, scoreboard, matchup, football):
        
        drive = FootballDrive(
            scoreboard = scoreboard,
            matchup = matchup, 
            football = football
            )

        return drive

    def change_half(self, scoreboard, football):
        scoreboard.half += 1
        scoreboard.possession = 1
        scoreboard.change_type = "kickoff"
        football.position = 20
    



