import random

class board:
    def __init__(self, dim_size, num_snakes, num_laders):
        self.dim_size = dim_size
        self.num_snakes = num_snakes
        self.num_laders = num_laders

        self.snakes_pos = set()
        self.laders_pos = set()

        self.board = [[None for _ in range(dim_size)] for _ in range(dim_size)]
        self.initialize_snakes_pos()
        self.initialize_laders_pos()
    
    def start_in_set(self, set, pos):
        for x, _, _ in set:
            if x == pos:
                return True
        return False
    
    def in_set(self, set, pos):
        for s in set:
            if pos in s:
                return True
        return False
    
    def index_to_pos(self, index):
        return index // self.dim_size, index % self.dim_size
    
    def pos_to_index(self, row, col):
        return row*self.dim_size + col
    
    def initialize_snakes_pos(self):
        num_snakes_put = 0
        while num_snakes_put < self.num_snakes:
            pos1, pos2 = random.randint(0, self.dim_size ** 2 - 1), random.randint(0, self.dim_size ** 2 - 1)
            snake_head, snake_tail = max(pos1, pos2), min(pos1, pos2)
            if snake_head == snake_tail or self.start_in_set(self.snakes_pos, snake_head) or self.indexes_same_row_or_col(snake_head, snake_tail) or snake_head == self.dim_size ** 2 - 1:
                continue
            num_snakes_put += 1
            self.snakes_pos.add((snake_head, snake_tail, num_snakes_put))
        
    def initialize_laders_pos(self):
        num_laders_put = 0
        while num_laders_put < self.num_laders:
            pos1, pos2 = random.randint(0, self.dim_size ** 2 - 1), random.randint(0, self.dim_size ** 2 - 1)
            lader_start, lader_end = min(pos1, pos2), max(pos1, pos2)
            if lader_start == lader_end or self.start_in_set(self.snakes_pos, lader_start) or lader_start == 0 or self.indexes_same_row_or_col(lader_start, lader_end) or lader_end == self.dim_size ** 2 - 1:
                continue
            num_laders_put += 1
            self.laders_pos.add((lader_start, lader_end, num_laders_put))
    
    def indexes_same_row_or_col(self, index1, index2):
        row1, col1 = self.index_to_pos(index1)
        row2, col2 = self.index_to_pos(index2)
        if abs(row1 - row2) <=1 or abs(col1 - col2) <=1:
            return True
        return False
    
    def pos_end_up(self, index):
        end_up = index
        for x, y, _ in self.snakes_pos:
            if index == x:
                end_up = self.pos_end_up(y)
        for x, y, _ in self.laders_pos:
            if index == x:
                end_up = self.pos_end_up(y)
        return min(end_up, self.dim_size ** 2 - 1)
    
    def move(self, start_index, move):
        return self.pos_end_up(min(start_index + move, self.dim_size ** 2 - 1))
    
    def getCellName(self, index):
        cellName = ""
        for x,y,z in self.snakes_pos:
            if index == x:
                cellName += "SH" + str(z)
            if index == y:
                cellName += "ST" + str(z)
        
        for x,y,z in self.laders_pos:
            if index == x:
                cellName += "LS" + str(z)
            if index == y:
                cellName += "LE" + str(z)
        
        if cellName == "":
            cellName += str(index)
        
        offset1 = (12 - len(cellName)) // 2
        offset2 = 12 - offset1 - len(cellName)
        return (' ' * offset1 + cellName + ' ' * offset2)
    
    def print_board(self, players):
        board_str = "----------\n"
        for row in range(self.dim_size):
            board_row = "|"
            for col in range(self.dim_size):
                cellName = ""
                for player in range(len(players)):
                    if self.pos_to_index(row, col) == players[player].pos:
                        cellName += "P" + str(player)
                if cellName == "":
                    board_row += self.getCellName(self.pos_to_index(row, col))
                else:
                    offset1 = (12 - len(cellName)) // 2
                    offset2 = 12 - offset1 - len(cellName)
                    board_row += (' ' * offset1 + cellName + ' ' * offset2)
                board_row += "|"
            board_str = board_row + "\n" + board_str
        board_str = "----------\n" + board_str
        return board_str
