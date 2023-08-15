import random
from board_class import board
    
class player:
    
    def __init__(self, start_index = 0):
        self.pos = start_index
    
    def roll_dice(self):
        dice_roll = random.randint(1, 6)
        print("Rolled ", dice_roll)
        return dice_roll
    
    def move(self, board: board):
        self.pos = board.pos_end_up(self.pos + self.roll_dice())