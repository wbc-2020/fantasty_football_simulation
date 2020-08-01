#!/usr/bin/env python
"""Simulate a football game

This module implements a simulation of a football game using NFL rules.
"""

import numpy as np
from football_drive import FootballDrive
from football_game_mechanics import predict_game_length, coin_toss


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
        self.score = "TBD"
        self.coin_winner = "TBD"
        self.drive_log = None

    def get_matchup(self):
    
        return [self.home_team, self.away_team]

    def get_coin_toss_winner(self):
    
        return self.get_matchup()[self.coin_winner]


    def play(self):
        """P
        """

        self.__pregame()

        while self.remain_plays > 0:

            current_drive = FootballDrive(ball_on = self.ball_on, plays_remain = self.remain_plays,
                                          change_type = self.change_type, team_w_ball = self.get_matchup()[self.possession], 
                                          team_wo_ball = self.get_matchup()[self.defense], score = self.score)
            current_drive.run_drive()

            self.__update_results_of_drive(current_drive)

            self.remain_plays -= current_drive.play_count

    def game_drive_summary(self):
    
        print("\n\n         ****GAME SUMMARY****\n\n")
        print(f"Final Score: {self.home_team} - {self.score[0]}\n             {self.away_team} - {self.score[1]}")
        for drive in self.drive_log:
        
            print(f"{drive.team_w_ball} : Drive resulted in a {drive.result}")
            print(f"{drive.play_count} plays for {drive.points} points")

    #
    # Private methods
    #
    def __get_play_count(self):
    
        return predict_game_length()

    def __flip_possession(self):
    
        self.defense = abs(self.possession)
        self.possession = abs(self.possession - 1)

    def __pregame(self):

        self.score = [0, 0]
        self.drive_log = list()
        
        self.remain_plays = self.__get_play_count()
        self.coin_winner, self.possession, self.defense = coin_toss()

        self.ball_on = 20
        self.change_type = "kickoff"

    def __update_results_of_drive(self, drive):

        self.drive_log.append(drive)
        turnover_types = ["turnover on downs", "fumble", "interception", "missed field goal"]
        
        if drive.result == "punt":
            self.change_type = "punt"
            self.ball_on = drive.ending_field_position
            self.__flip_possession()
            
        elif drive.result in turnover_types:
            self.change_type = "turnover"
            self.ball_on = drive.turnover_position
            self.__flip_possession()
            
        elif drive.points > 0:
            self.score[self.possession] += drive.points
            self.change_type = "kickoff"
            self.ball_on = 20
            self.__flip_possession()
            
        else:
            pass
