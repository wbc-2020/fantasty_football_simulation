


from football_play import *
from football_events import *
from football_drive import *
from football_game import FootballGame
from football_events import *


result = [0, 0, 0]


for i in range(1, 100001):
    game = FootballGame("a", "b", "New York")

    game.play()
    
    if game.score[0] > game.score[1]:
        result[0] += 1
    elif game.score[0] < game.score[1]:
        result[1] += 1
    else:
        result[2] += 1

print(result)