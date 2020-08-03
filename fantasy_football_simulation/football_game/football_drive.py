from play_caller import PlayCaller
from score_board import ScoreBoard
from football import Football
from official import Official

class DriveResult:

    def __init__(self):
        self._result = "incomplete"
        
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
        self.points = 0
        self.play_log = list()
        # Internal attributes

        self.down = 1
        self.to_gain = 10

        self.play_call = None
        self.extra_point_play = None
        self.turnover_position = None

        self.scoreboard = scoreboard
        self.matchup = matchup

        # Need to modify this, so not property
        self.plays_remain = abs(scoreboard.plays_in_half)
        self.ball_on = football.position

        self.starting_field_position = self.ball_on
        self.ending_field_position = self.ball_on
        
        self.football = football
        self.official = Official()
 
    @property
    def change_type(self):
    
        return self.scoreboard.change_type

    @property 
    def team_w_ball(self):

        return self.matchup[self.scoreboard.possession]

    @property
    def team_wo_ball(self):

        return self.matchup[self.scoreboard.defense]

    @property
    def play_count(self):
        
        return(len(self.play_log))

    @property
    def score(self):

        return(self.scoreboard.score)


    def run_drive(self):

        if self.scoreboard.change_type != "turnover":
            self.__change_possession()
      
        while self.plays_remain > 0 and self.result.is_incomplete():

                if self.down > 4:
                    self.__turnover_on_downs()
                    break

                self.__call_a_play()
                
                if self.play_call == "punt":
                    self.__punt()
                    break

                self.__run_a_play()
                
       
                self.official.officiate(play = self.play_call, football = self.football, 
                    scoreboard = self.scoreboard, drive_result = self.result, to_gain = self.to_gain)

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
        
        call = PlayCaller(self.ball_on, self.team_w_ball, self.team_wo_ball)
        call.call_play(self.ball_on, self.down, self.to_gain)
        self.play_call = call.play_call

    def __run_a_play(self):
        
        self.play_call.run_play()
        self.plays_remain -= 1
        

    def __update_play_results(self):
        
        if self.play_call.result == "touchdown":
            self.__touchdown()

        elif self.play_call.result == "first down":
            self.__first_down()

        elif self.play_call.result == "field goal good":
            self.__field_goal_good()

        elif self.play_call.result == "field goal missed":
            self.__field_goal_missed()

        elif self.play_call.result == "fumble":
            self.__fumble()

        elif self.play_call.result == "interception":
            self.__interception()

        else:
            self.__next_play()

    def __change_possession(self):
        
        play = PlayCaller(self.team_w_ball, self.team_wo_ball, self.score)
        play.call_kick_return(self.football.position, self.change_type)
        play.play_call.run_play()

        self.ball_on = play.play_call.ball_on
        self.starting_field_position = self.ball_on

        if play.play_call.play_type != "turnover":
            self.play_log.append(play.play_call)
            self.plays_remain -= 1

        if play.play_call.result == "touchdown":
            self.__touchdown()

    def __extra_point(self):    
        
        play_caller = PlayCaller(self.team_w_ball, self.team_wo_ball, self.score)
        play_caller.call_extra_point()
        self.extra_point_play = play_caller.play_call

        self.extra_point_play.run_play()
        
        self.official.officiate(play = self.extra_point_play, football = self.football, 
                    scoreboard = self.scoreboard, drive_result = self.result)
        
        self.points += self.extra_point_play.points
        self.play_log.append(self.extra_point_play)

    def __touchdown(self):
        
        self.points = 6
        self.ending_field_position = self.football.position
        self.__extra_point()

    def __punt(self):
        
        self.result.result = "punt"
        self.ending_field_position = self.ball_on

    def __turnover_on_downs(self):
        
        self.result.result = "turnover on downs"
        self.turnover_position = self.football.position

    def __field_goal_good(self):
        
        self.points = 3
        self.ending_field_position = 100

    def __field_goal_missed(self):
        
        self.ending_field_position = self.football.position

    def __fumble(self):
        
        # May have return
        self.ending_field_position = self.ball_on + self.yards

    def __interception(self):
        
        # May have return
        self.ending_field_position = self.ball_on + self.yards

    def __first_down(self):
        
        self.down = 1
        self.to_gain = 10
        self.ball_on += self.play_call.yards

    def __next_play(self):
        
        self.down+= 1
        self.to_gain -= self.play_call.yards
        self.ball_on += self.play_call.yards
