

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

            elif football.position + play.yards < 0:
                play.result = "safety"
                drive_result.ending_field_position = -1
                drive_result.result = "safety"

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
                    drive_result.points += 1

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

                else:
                    play.points = 0
                    drive_result.points = 0
                    drive_result.ending_field_position = football.position
                    play.result = "field goal missed"
                    drive_result.result = "missed field goal"
        else:
            raise ValueError("Unknown play class type")
    
    def punt(self, football, scoreboard, drive_result):
       
        drive_result.ending_field_position = football.position
        drive_result.result = "punt"
    