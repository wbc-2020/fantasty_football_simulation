from score_board import ScoreBoard

# Need to implement 
#     two point conversion attempt
#     fumbles
#     interceptions
class Official:

    def __init(self):
        
        self.class_type = "Official"

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
            
            if play.outcome.turnover:
                drive_result.ending_field_position = football.position
                drive_result.result = "turnover"  

                football.position += play.yards
                football.flip_field()

                scoreboard.turnover()
                
            else:
                if football.position + play.yards >= 100:
                    play.result = "touchdown"
                    play.points = 6
                    
                    drive_result.points = 6
                    drive_result.ending_field_position = 100
                    drive_result.result = "touchdown"
                    
                    football.position = 20
                    
                    scoreboard.add_touchdown()

                elif football.position + play.yards < 0:
                    play.result = "safety"
                    
                    drive_result.ending_field_position = -1
                    drive_result.result = "safety"
                    
                    football.position = 20
                    
                    scoreboard.add_safety()
                

                elif scoreboard.to_gain - play.yards <= 0:
                    play.result = "first down"
                    play.points = 0
                    
                    football.position += play.yards
                    
                    scoreboard.first_down()

                elif scoreboard.down == 4:
                    play.result = "turnover on downs"
                    
                    drive_result.ending_field_position = football.position
                    drive_result.result = "turnover on downs"  
                    
                    football.position += play.yards
                    football.flip_field()
                    
                    scoreboard.turnover()

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
                    play.result = "field goal good"
                    
                    drive_result.points = 3
                    drive_result.ending_field_position = football.position
                    drive_result.result = "field goal"
                    
                    football.position = 20
                    
                    scoreboard.add_field_goal()

                else:
                    play.points = 0
                    play.result = "field goal missed"                    
                    
                    drive_result.points = 0
                    drive_result.ending_field_position = football.position
                    drive_result.result = "missed field goal"
                    
                    football.flip_field()
                    
                    scoreboard.turnover()

        else:
            raise ValueError("Unknown play class type")
    
    def punt(self, football, scoreboard, drive_result):
       
        drive_result.ending_field_position = football.position
        drive_result.result = "punt"

        football.flip_field()
        
        scoreboard.punt()

    def change_half(self, scoreboard, football):
        scoreboard.change_half()
        football.position = 20
