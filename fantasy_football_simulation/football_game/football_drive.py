from play_caller import PlayCaller
from football_drive_mechanics import ChangeOfPossession
from score_board import ScoreBoard


class FootballDrive:

    def __init__(self, scoreboard, matchup):
        # Public Attribute
        self.result = "incomplete"
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
        self.plays_remain = scoreboard.plays_in_half
        self.ball_on = scoreboard.ball_on

        self.starting_field_position = self.ball_on
        self.ending_field_position = self.ball_on
 
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

        self.__change_possession()

        while self.plays_remain > 0 and self.result == "incomplete":

                if self.down > 4:
                    self.__turnover_on_downs()
                    break

                self.__call_a_play()
                
                if self.play_call == "punt":
                    self.__punt()
                    break

                self.__run_a_play()

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
        self.play_log.append(self.play_call)

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
        
        change_of_possession = ChangeOfPossession(self.change_type, self.ball_on, self.team_w_ball, self.team_wo_ball)
        change_of_possession.change_possession()

        self.play_call = change_of_possession.play_call
        self.play_call.run_play()

        self.ball_on = self.play_call.ball_on
        self.starting_field_position = self.play_call.ball_on

        if self.play_call.play_type != "turnover":
            self.play_log.append(self.play_call)
            self.plays_remain -= 1

        if self.play_call.result == "touchdown":
            self.__touchdown()

    def __extra_point(self):    
        
        play_caller = PlayCaller(self.team_w_ball, self.team_wo_ball, self.score)
        play_caller.call_extra_point(self.ball_on)
        self.extra_point_play = play_caller.play_call

        self.extra_point_play.run_play()
        self.points += self.extra_point_play.points
        self.play_log.append(self.extra_point_play)

    def __touchdown(self):
        
        self.points = 6
        self.result = "touchdown"
        self.ending_field_position = 100
        self.__extra_point()

    def __punt(self):
        
        self.result = "punt"
        self.ending_field_position = self.ball_on

    def __turnover_on_downs(self):
        
        self.result = "turnover on downs"
        self.turnover_position = self.ball_on

    def __field_goal_good(self):
        
        self.points = 3
        self.result = "field goal"
        self.ending_field_position = 100

    def __field_goal_missed(self):
        
        self.result = "missed field goal"
        self.ending_field_position = self.ball_on

    def __fumble(self):
        
        self.result = "fumble"
        # May have return
        self.ending_field_position = self.ball_on + self.yards

    def __interception(self):
        
        self.result = "interception"
        # May have return
        self.ending_field_position = self.ball_on + self.yards

    def __first_down(self):
        
        self.down = 1
        self.to_gain = 10
        self.ball_on += self.play_call.yards
        self.ending_field_position = self.ball_on

    def __next_play(self):
        
        self.down+= 1
        self.to_gain -= self.play_call.yards
        self.ball_on += self.play_call.yards
        self.ending_field_position += self.play_call.yards
