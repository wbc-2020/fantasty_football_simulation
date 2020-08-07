#!/usr/bin/env python

class Football:
    """Tracks position of football on field
    Parameters
    ----------
    none
    
    Attributes
    ----------
    position (int) position of football on field
    
    Methods
    -------
    flip_field : flip the field between possessions
    
    """

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