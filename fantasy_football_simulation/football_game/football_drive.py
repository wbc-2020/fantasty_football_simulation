from play_caller import PlayCaller
from score_board import ScoreBoard
from football import Football
from official import Official

class DriveResult:

    def __init__(self):
        self._result = "incomplete"
        self.points = 0
        self.starting_field_position = None
        self.ending_field_position = None
        
    def is_incomplete(self):
        
        if self.result == "incomplete":
           return True
           
        else:
            return False
    
    @property
    def result(self):
    
        return self._result
            
    @result.setter
    def result(self, new_result):
    
        self._result = new_result
    
class FootballDrive:

    def __init__(self, scoreboard, matchup, football):
        # Public Attribute
        self.result = DriveResult()
        self.play_log = list()
        # Internal attributes

        self.play_call = None
        self.extra_point_play = None
        self.turnover_position = None

        self.scoreboard = scoreboard
        self.matchup = matchup
        
        self.football = football
        self.official = Official()
        
        self.team_w_ball = self.matchup[self.scoreboard.possession]
        self.team_wo_ball = self.matchup[self.scoreboard.defense]
    
    @property
    def change_type(self):
    
        return self.scoreboard.change_type

    @property
    def play_count(self):
        
        return(len(self.play_log))

    @property
    def score(self):

        return(self.scoreboard.score)

    def run_drive(self):

        if self.scoreboard.change_type != "turnover":
            self.__change_possession()
      
        while self.scoreboard.time_in_half > 0 and self.result.is_incomplete():

                self.__call_a_play()
                
                if self.play_call == "punt":
                    self.official.punt(self.football, self.scoreboard, self.result)
                    break

                self.__run_a_play()
                     
                self.official.officiate(play = self.play_call, football = self.football, 
                    scoreboard = self.scoreboard, drive_result = self.result)

                self.play_log.append(self.play_call)
                
                self.__update_play_results()

    def drive_summary(self):

        print("Drive Summary\n\n")
        print(f"Drive began from own {self.starting_field_position}")
        print(f"{self.play_count} plays ending in a {self.result}")
        print("\nPlay by Play\n")
        
        for play in self.play_log:
            print(f"{play.play_type} play for {play.yards} yards and {play.points} points")

    def __call_a_play(self):
        
        call = PlayCaller(self.football.position, self.team_w_ball, self.team_wo_ball)
        call.call_play(self.football.position, self.scoreboard.down, self.scoreboard.to_gain)
        self.play_call = call.play_call

    def __run_a_play(self):
        
        self.play_call.run_play()

        

    def __update_play_results(self):
        
        if self.play_call.result == "touchdown":
            self.__extra_point()

    def __change_possession(self):
        
        play = PlayCaller(self.team_w_ball, self.team_wo_ball, self.score)
        play.call_kick_return(self.football.position, self.change_type)
        play.play_call.run_play()

        self.official.officiate(play = play.play_call, football = self.football, 
            scoreboard = self.scoreboard, drive_result = self.result)

        if play.play_call.play_type != "turnover":
            self.play_log.append(play.play_call)

    def __extra_point(self):    
        
        play_caller = PlayCaller(self.team_w_ball, self.team_wo_ball, self.score)
        play_caller.call_extra_point()
        self.extra_point_play = play_caller.play_call

        self.extra_point_play.run_play()
        
        self.official.officiate(play = self.extra_point_play, football = self.football, 
                    scoreboard = self.scoreboard, drive_result = self.result)
        
        self.play_log.append(self.extra_point_play)
