

class FootballEvent():
    
    def __init__(self):
        self._event_type = None
     
    @property
    def event_type(self):
        return self._event_type


class Penalty(FootballEvent):
    
    def __init__(self):
        FootballEvent.__init__(self)
        self._event_type = "penalty"


class Injury:
    pass


class Fumble:
    pass
    

class Interception:
    pass


class BlockedKick:
    pass
    

class Sack:
    pass