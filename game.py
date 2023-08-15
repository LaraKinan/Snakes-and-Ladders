from board_class import board
from player_class import player

class game:

    def __init__(self, dim_size = 10, num_snakes = 3, num_laders = 5, num_players = 1):
        self.board = board(dim_size, num_snakes, num_laders)
        self.num_players =num_players
        self.players = [player() for _ in range(num_players)]
        self.curr_player = 0
    
    def player_move(self):
        curr_player = self.players[self.curr_player]
        print("Player Turn: ", self.curr_player, " Player is at ", self.board.index_to_pos(curr_player.pos))
        curr_player.move(self.board)
        print("Player is at pos ", self.board.index_to_pos(curr_player.pos))
        self.curr_player = (self.curr_player + 1) % self.num_players
    
    def is_game_over(self):
        for player in self.players:
            if player.pos >= self.board.dim_size ** 2 - 1:
                return True
        return False
    
    def __str__(self):
        game_stats = self.board.print_board(self.players)
        return game_stats

    def play(self):
        while not self.is_game_over():
            print(self)
            self.player_move()

new_game = game()
new_game.play()
