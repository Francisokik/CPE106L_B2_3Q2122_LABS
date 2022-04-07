''' This is the main logic for a Tic-tac-toe game.
It is not optimised for a quality game it simply
generates random moves and checks the results of
a move for a winning line. Exposed functions are:
newGame()
saveGame()
restoreGame()
userMove()
computerMove()
'''

import os, random
import oxo_data

def nGame():
    return list(" " * 9)

def sGame(game):
    oxo_data.sGame(game)
    
def rGame():
    try:
        game = oxo_data.rGame()
        if len(game) == 9:
            return game
        else: return nGame()
    except IOError:
        return nGame()
    
def _genMove(game):
    options = [i for i in range(len(game)) if  game[i] == " "]
    if options:
       return random.choice(options)
    else: return -1
    
def _winningMove(game):
    wins = ((0,1,2), (3,4,5), (6,7,8),
            (0,3,6), (1,4,7), (2,5,8),
            (0,4,8), (2,4,6))

    for a,b,c in wins:
        chars = game[a] + game[b] + game[c]
        if chars == 'XXX' or chars == 'OOO':
            return True
    return False

def userMove(game,cell):
    if game[cell] != ' ':
        raise ValueError('Invalid cell')
    else:
        game[cell] = 'X'
    if _winningMove(game):
        return 'X'
    else:
        return ""

def compMove(game):
    cell = _genMove(game)
    if cell == -1:
        return 'D'
    game[cell] = 'O'
    if _winningMove(game):
        return 'O'
    else:
        return ""

class test(object): 
    result = ""
    game = nGame()
    while not result:
        print(game)
        try:
           result = userMove(game, _genMove(game))
        except ValueError:
            print("Oops, that shouldn't happen")
        if not result:
            result = compMove(game)
            
        if not result: continue
        elif result == 'D':
            print("Its a draw")
        else:
            print("Winner is:", result)
        print(game)

if __name__ == "__main__":
    test()

            
