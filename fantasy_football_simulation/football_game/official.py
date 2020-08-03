


class Official:

    def __init(self):
        
        self.class_type = "Official"
    
    def flip_field(self, football):

        football.flip_field()


    def officiate(self, play, football, scoreboard, drive_result):
  
        if play.class_type == "KickReturnTeam":  
            football.position = 100 - football.position - play.kick_length + play.return_yards
            
            
            if football.position > 100:
                play.result = "touchdown"
                play.points = 6
                drive_result.result = "touchdown"
            
            else:
                self.play.result = "drive start"
                self.play.points = 0
            
        elif play.class_type == "RegularTeam":
             
            if football.position + play.yards >= 100:
                play.result = "touchdown"
                play.points = 6
                drive_result.result = "touchdown"
            
            elif scoreboard.to_gain - play.yards <= 0:
                play.result = "first down"
                play.points = 0
                football.position += play.yards
                scoreboard.first_down()
            
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
            
                else:
                    play.points = 0
                    play.result = "extra point missed"
                    drive_result.result = "touchdown w missed extra point"
            else:
                if play.good:
                    play.points = 3
                    play.result = "field goal good"
                    drive_result.result = "field goal"

                else:
                    play.points = 0
                    play.result = "field goal missed"
                    drive_result.result = "missed field goal"
        else:
            raise ValueError("Unknown play class type")
    
 