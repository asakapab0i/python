#import random module

class Tictactoe:
    """A tictactoe game"""

    #constructor
    def __init__(self, player_instance, bot_instance):
        self._player_instance = player_instance
        self._bot_instanace = bot_instance
        self._board = range(0,10)
        
    def board(self):
        print self._board[0], '|', self._board[2], '|', self._board[2]
        print('----------')
        print self._board[3], '|', self._board[4], '|', self._board[5]
        print('----------')
        print self._board[6], '|', self._board[7], '|', self._board[9]

    def start(self):
        self.board()

        is_valid = True
        while is_valid:
            if is_ended() == True
                self.player_instance.on_turn()
                self.bot_instance.on_onturn()
            else:
                is_valid = False
                
    def is_ended():
        return False;    
    

def main():
    tictac = Tictactoe("Bryan","Bot")
    tictac.start()

if __name__ == "__main__":
    main()
        
        
        
        
        
