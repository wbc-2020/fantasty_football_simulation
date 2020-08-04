




class Football:

    def __init__(self):
    
        self._position = 20
    
    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, new_position):
    
        if new_position > 101 or new_position < -1:
            raise ValueError("Invalid ball position.")
        self._position = new_position         

    def flip_field(self):
        
        self._position = 101 - self._position        