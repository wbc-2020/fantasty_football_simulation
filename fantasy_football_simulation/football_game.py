#class for football game
import numpy as np
from .football_drive import FootballDrive

class FootballGame:


    def __init__(self, team_1, team_2):
        self.home_team = team_1
        self.away_team = team_2
        self.matchup = [team_1, team_2]
        
    def print_matchup(self):
        print(f"{self.home_team} vs. {self.away_team}")
        
            
    def __get_play_count(self):
        return(150)
        
    def __flip_coin(self):
        return int(np.random.binomial(1, .5, 1))
        

    def __flip_possession(self):
        self.possession = abs(self.possession - 1)
    
    def play(self):
        
        plays = self.__get_play_count()
        self.remain_plays = int(plays)
        self.score = [0, 0]
        self.coin_winner = self.__flip_coin()
        self.drive_log = list()
        
        self.possession = abs(self.coin_winner - 1)
        
        ball_on = 20
        change_type = "kickoff"
        
        while self.remain_plays > 0:
            
            current_drive = FootballDrive(ball_on = ball_on, plays_remain = self.remain_plays, change_type = change_type)
            current_drive.run_drive()

            
            if current_drive.result == "punt":
                change_type = "punt"
                ball_on = current_drive.ending_field_position
                self.__flip_possession()
            elif current_drive.result == "turnover on downs":
                change_type = "turnover on downs"
                ball_on = current_drive.ending_field_position
                self.__flip_possession()
            elif current_drive.points > 0:
                self.score[self.possession] += current_drive.points
                change_type = "kickoff"
                ball_on = 20
                self.__flip_possession()
            else:
                pass
        
            self.drive_log.append(current_drive)
            self.remain_plays -= current_drive.play_count
    
        

    def game_drive_summary(self):
        print("\n\n         ****GAME SUMMARY****\n\n")
        print(f"Final Score: {self.home_team} - {self.score[0]}\n             {self.away_team} - {self.score[1]}")
        for drive in self.drive_log:
        
            print(f"Drive resulted in a {drive.result}")
            print(f"{drive.play_count} plays for {drive.points} points")
        
        
