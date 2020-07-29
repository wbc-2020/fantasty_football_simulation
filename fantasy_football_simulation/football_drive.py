from .play_caller import PlayCaller




class FootballDrive:

    def __init__(self, ball_on, plays_remain, change_type, down = 1, to_gain = 10):
        
        #drive summary stats
        self.play_log = list()
        self.starting_field_position = ball_on
        self.ending_field_position = ball_on
        self.points = 0
        self.result = "incomplete"
        self.play_count = 0
        
        #drive internals
        self.change_type = change_type
        self.ball_on = ball_on
        self.plays_remain = plays_remain
        self.down = down
        self.to_gain = to_gain
    
    
    def __call_a_play(self):
        call = PlayCaller(self.ball_on)
        call.call_play(self.down, self.to_gain)
        self.play_call = call.play_call
        
        
    def __run_a_play(self):
        self.play_call.run_play()
  
  
    def __change_possession(self):
    
        call = PlayCaller(self.ball_on)
        call.call_change_possession(self.change_type)
        self.play_call = call.play_call
        self.play_call.run_play()
        self.play_call.evaluate_play()
        self.ball_on = self.play_call.ball_on
        self.starting_field_position = self.play_call.ball_on
        self.cop_score = False        
        self.play_log.append(self.play_call)
    
    def run_drive(self):
        
        
        
        self.__change_possession()
        
        
        #is there time left in the game
        #is drive unfinished
        while self.plays_remain > 0 and self.result == "incomplete":
                
                #check to see if unsuccesful 4th down
                if self.down > 4:
                   self.result = "turnover on downs" 
                   break
                   
                self.__call_a_play()
                
                if self.play_call == "punt":
                    self.result = "punt"
                    self.plays_remain -= 1
                    break
                    
               
                   
                self.__run_a_play()
                self.play_count += 1
                self.plays_remain -= 1
                self.play_log.append(self.play_call)
            
                #update results of play
                if self.play_call.result == "touchdown":
                    self.points = 6
                    self.result = "touchdown"
                    self.ending_field_position = 100
                elif self.play_call.result == "first down":
                    self.down = 1
                    self.to_gain = 10
                    self.ball_on += self.play_call.gain
                    self.ending_field_position = self.ball_on
                elif self.play_call.result == "field goal":
                    self.points = 3
                    self.result = "field goal"
                    self.ending_field_position = 100
                else:
                    self.down+= 1
                    self.to_gain -= self.play_call.gain
                    self.ball_on += self.play_call.gain
                    self.ending_field_position += self.play_call.gain
        
        
    def drive_summary(self):
        print("Drive Summary\n\n")
        print(f"Drive began from own {self.starting_field_position}")
        print(f"{self.play_count} plays ending in a {self.result}")    
        print("\nPlay by Play\n")
        for play in self.play_log:
            print(f"{play.play_type} play for {play.gain} yards and {play.points} points")







  
    
   
            
        
        