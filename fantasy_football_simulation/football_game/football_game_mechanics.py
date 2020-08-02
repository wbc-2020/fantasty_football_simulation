
from football_drive import FootballDrive
from score_board import ScoreBoard
import numpy as np

        
class GameManager:

    def __init__(self):
        self.type = "GameManager"
    
    def update_results(self, scoreboard, drive, football):
    
        scoreboard.drive_log.append(drive)
        scoreboard.plays_in_half -= drive.play_count
        turnover_types = ["turnover on downs", "fumble", "interception", "missed field goal"]    
    
        if drive.result == "punt":
            scoreboard.change_type = "punt"
            football.position = drive.ending_field_position
            self.__flip_possession(scoreboard)
            
        elif drive.result in turnover_types:
            scoreboard.change_type = "turnover"
            football.position = drive.turnover_position
            self.__flip_possession(scoreboard)
            
        elif drive.points > 0:
            scoreboard.score[scoreboard.possession] += drive.points
            scoreboard.change_type = "kickoff"
            football.position = 20
            self.__flip_possession(scoreboard)
            
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
    
    def __flip_possession(self, scoreboard):

        scoreboard.possession = abs(scoreboard.possession - 1)


