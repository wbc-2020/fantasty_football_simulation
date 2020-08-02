from football_game_mechanics import GameManager


class Official(GameManager):

    def __init(self):
        
        GameManager.__init__(self)
    
    def flip_field(self, football):

        football.flip_field()

            
    
    def officiate(self, play, football, scoreboard):
    
        if play.class_name == "KickReturnTeam":
            
            football.position = 100 - football.position - play.kick_length = play.return_yards
            
            
            if football.position > 100:
                self.play.result = "touchdown"
                self.play.points = 6
                scoreboard.score[scoreboard.possession] += 6
                self.result = "touchdown"
            else:
                self.play.result = "drive start"
                self.play.points = 6
            
        elif play_class_name == "RegularTeam":
            
            
        elif play_class_name == "PlaceKickTeam":
            if play.play_type == "extra point attempt":
                if play.good:
                    play.points = 1
                    play.result = "extra point good"
            
                else:
                    play.points = 0
                    play.result = "extra point missed"
        else:
            if self.good:
                play.points = 3
                play.result = "field goal good"

            else:
                play.points = 0
                playf.result = "field goal missed"
        else:
            raise ValueError("Unknown play class type")
    
    
    
    def play_update_scoreboard(self, scoreboard, play):
            
        

        
        
        
        
    def __update_play_results(self):
        
        if self.play.result == "touchdown":
            self.__touchdown()

        elif self.play.result == "first down":
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