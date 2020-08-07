
from football_drive import FootballDrive
from score_board import ScoreBoard
import numpy as np

        
class GameManager:

    def __init__(self):
        self.type = "GameManager"
    
    def run_drive(self, scoreboard, matchup, football):
        
        drive = FootballDrive(
            scoreboard = scoreboard,
            matchup = matchup, 
            football = football
            )

        return drive

    def change_half(self, scoreboard, football):
        scoreboard.change_half()
        football.position = 20
    



