#!/usr/bin/env python
"""Simulate a football game

This module implements a simulation of a football game using NFL rules.
"""

import numpy as np
from game_manager import GameManager
from football import Football
from score_board import ScoreBoard


class FootballGame:
    """Simulate a football game

    This class simulates a football game and the associated play/player level statistics


    Parameters
    ----------
    home team : team (TBI)
        Home team
    away_team: team (TBI)
        Away team
    location: str
        Location of game

    Attributes
    ----------
    home_team: team (TBI)
        Home team 
    away_team: 
        Away team 
    location: str
        Location of game
    score: list of int
        Initialized as "TBD" upon creation
    drive_log: list of drive objects
        
    Methods
    -------
    play()
        Simulate the game
        


    Notes
    -----
    A football game object is a list of football drive objects built by the play() method. The game algorithm is:

        while there is time left in the game:
            run a drive
            update results of a drive
            update clock
    """

    def __init__(self, home_team, away_team, location):
    
        self.home_team = home_team
        self.away_team = away_team
        self.location = location
        self.date = "TBD"
     
        self.score_board = ScoreBoard()
        self.game_manager = GameManager()
        self.football = Football()
    
    
    @property
    def score(self):

        return self.score_board.score

    @property
    def matchup(self):

        return [self.home_team, self.away_team]



    def play(self):
        """P
        """

        for half in range(1, 3):

            while self.score_board.plays_in_half > 0:

                current_drive = self.game_manager.run_drive(self.score_board, self.matchup, self.football) 
                
                current_drive.run_drive()

                self.game_manager.update_results(self.score_board, current_drive, self.football)

            if half == 1:

                self.game_manager.change_half(self.score_board, self.football)
        
    def game_drive_summary(self):
    
       
        print("\n\n         ****GAME SUMMARY****\n\n")
        print(f"Final Score: {self.home_team} - {self.score[0]}\n             {self.away_team} - {self.score_board.score[1]}")
        for drive in self.score_board.drive_log:

            print(f"{drive.team_w_ball} : Drive resulted in a {drive.result.result}")
            print(f"{drive.play_count} plays for {drive.points} points")


