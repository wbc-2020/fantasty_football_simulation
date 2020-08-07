

# Need to implement 
#     two point conversion attempt
#     fumbles
#     interceptions
class Official:

    def __init(self):
        
        self.class_type = "Official"
    
    def flip_field(self, football):

        football.flip_field()


    def officiate(self, play, football, scoreboard, drive_result):
  
        if play.class_type == "KickReturnTeam":  
            football.position = 100 - football.position - play.kick_length + play.return_yards

            scoreboard.deduct_time()
            
            if football.position > 100:
                play.result = "touchdown"
                play.points = 6
                drive_result.points = 6
                drive_result.ending_field_position = 100
                drive_result.result = "touchdown"
                scoreboard.add_touchdown()

            else:
                play.result = "drive start"
                play.points = 0

        elif play.class_type == "RegularTeam":

            scoreboard.deduct_time()
            
            if football.position + play.yards >= 100:
                play.result = "touchdown"
                play.points = 6
                drive_result.points = 6
                drive_result.ending_field_position = 100
                drive_result.result = "touchdown"
                scoreboard.add_touchdown()
                scoreboard.change_type = "kickoff"
                football.position = 20
                scoreboard.flip_possession()

            elif football.position + play.yards < 0:
                play.result = "safety"
                drive_result.ending_field_position = -1
                drive_result.result = "safety"
                scoreboard.add_safety()
                scoreboard.change_type  = "punt"
                football.position = 20
                scoreboard.flip_possession

            elif scoreboard.to_gain - play.yards <= 0:
                play.result = "first down"
                play.points = 0
                football.position += play.yards
                scoreboard.first_down()

            elif scoreboard.down == 4:
                play.result = "turnover on downs"
                football.position += play.yards
                drive_result.ending_field_position = football.position
                drive_result.result = "turnover on downs"  
                scoreboard.change_type = "turnover"
                football.flip_field()
                scoreboard.flip_possession()                

            else:
                play.result = "next down"
                play.points = 0
                football.position += play.yards
                scoreboard.down += 1
                scoreboard.to_gain -= play.yards

        elif play.class_type == "PlaceKickTeam":

            if play.play_type == "extra point attempt":

                if play.good:
                    play.points = 1
                    play.result = "extra point good"
                    scoreboard.add_extra_point()

                else:
                    play.points = 0
                    play.result = "extra point missed"
                    drive_result.result = "touchdown w missed extra point"
            else:
                if play.good:
                    play.points = 3
                    drive_result.points = 3
                    drive_result.ending_field_position = football.position
                    play.result = "field goal good"
                    drive_result.result = "field goal"
                    scoreboard.add_field_goal()
                    scoreboard.change_type = "kickoff"
                    football.position = 20
                    scoreboard.flip_possession()

                else:
                    play.points = 0
                    drive_result.points = 0
                    drive_result.ending_field_position = football.position
                    play.result = "field goal missed"
                    drive_result.result = "missed field goal"
                    scoreboard.change_type = "turnover"
                    football.flip_field()
                    scoreboard.flip_possession()
        else:
            raise ValueError("Unknown play class type")
    
    
    
    
    
    def punt(self, football, scoreboard, drive_result):
       
        drive_result.ending_field_position = football.position
        drive_result.result = "punt"
        scoreboard.change_type = "punt"
        football.flip_field()
        scoreboard.flip_possession()
    