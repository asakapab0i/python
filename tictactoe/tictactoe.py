import random
class Game:
    """A Tic Tac Toe Game"""

    def __init__(self):
        #initialize board
        self._board = range(1,10);
    def game_screen(self):
        #make a game screen
        print self._board[0], '|' , self._board[1],'|',self._board[2]
        print('--------------')
        print self._board[3], '|' , self._board[4],'|',self._board[5]
        print('--------------')
        print self._board[6], '|' , self._board[7],'|',self._board[8]
    def select_position(self):
        #manual select for position
        valid = False
        while not valid:
            try:
                selected = int(input("Choose board position: "))
                if 1 <= selected <= 10:
                    valid = True
                else:
                    print("Invalid selection please input between 1 - 10")
            except ValueError:
                print("Invalid selection please input between 1 - 10")
        return selected
                
    def auto_position(self):
        #auto generate position
        position = random.randint(1,9)
        return position

    def check_win_player(self):
        if self._board[0] == 'X' and self._board[1] == 'X' and self._board[2] == 'X':
            return True
        elif self._board[0] == 'X' and self._board[1] == 'X' and self._board[2] == 'X':
            return True
        elif self._board[3] == 'X' and self._board[4] == 'X' and self._board[5] == 'X':
            return True
        elif self._board[6] == 'X' and self._board[7] == 'X' and self._board[8] == 'X':
            return True
        elif self._board[0] == 'X' and self._board[3] == 'X' and self._board[6] == 'X':
            return True
        elif self._board[1] == 'X' and self._board[4] == 'X' and self._board[1] == 'X':
            return True
        elif self._board[2] == 'X' and self._board[5] == 'X' and self._board[8] == 'X':
            return True
        elif self._board[0] == 'X' and self._board[4] == 'X' and self._board[8] == 'X':
            return True
        elif self._board[2] == 'X' and self._board[4] == 'X' and self._board[6] == 'X':
            return True
        else:
            return False

    def check_win_bot(self):
        if self._board[0] == 'O' and self._board[1] == 'O' and self._board[2] == 'O':
            return True
        elif self._board[0] == 'O' and self._board[1] == 'O' and self._board[2] == 'O':
            return True
        elif self._board[3] == 'O' and self._board[4] == 'O' and self._board[5] == 'O':
            return True
        elif self._board[6] == 'O' and self._board[7] == 'O' and self._board[8] == 'O':
            return True
        elif self._board[0] == 'O' and self._board[3] == 'O' and self._board[6] == 'O':
            return True
        elif self._board[1] == 'O' and self._board[4] == 'O' and self._board[1] == 'O':
            return True
        elif self._board[2] == 'O' and self._board[5] == 'O' and self._board[8] == 'O':
            return True
        elif self._board[0] == 'O' and self._board[4] == 'O' and self._board[8] == 'O':
            return True
        elif self._board[2] == 'O' and self._board[4] == 'O' and self._board[6] == 'O':
            return True
        else:
            return False

    def players_turn(self):
        check_player = self.check_win_player()
        if check_player is True:
            print("Player wins the game!")
            return
        #player
        noexit = True
        while noexit:
            try:
                
                
                player_selected = self.select_position()
                if isinstance(self._board[player_selected-1], int) == True:
                    self._board[player_selected-1] = 'X'
                    self.game_screen()
                    print("----------------")
                    print("---Player End---")
                    print("------TURN------")
                    noexit = False
                   
                    
                else:
                    print('Position is already chosen! -- enter another position.')
            except ValueError:
                print('Position is already chosen! -- enter another position.')
            


    def bots_turn(self):
        check_bot = self.check_win_bot()
        if check_bot is True:
            print("Bot wins the game!")
            return
        #bot
        
                    
        noexit = True
        while noexit:
                
                bot_selected = self.auto_position()
                if isinstance(self._board[bot_selected-1], int) == True:
                    self._board[bot_selected-1] = 'O'
                    self.game_screen()
                    print("----------------")
                    print("----Bot End-----")
                    print("------TURN------")
                    noexit = False
               
def run_game(game):
    count = 0
    game.game_screen()
    while count != 10:
        game.players_turn()
        game.bots_turn()
        count += 2
            
        
    
    
def main():
    new_game = Game()
    run_game(new_game)

    
    
    
if __name__ == "__main__":
    main()
        
    
