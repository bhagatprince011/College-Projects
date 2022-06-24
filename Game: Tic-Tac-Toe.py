import random

  


def play():

      # Lets the player type which letter they want to be.

      # Returns a list with the player’s letter as the first item, and the computer's letter as the second.

      letter = ''

      while not (letter == 'X' or letter == 'O'):

         letter= input('\n\t\tDo you want to be X or O? :').upper()

         

 

      # the first element in the list is the player’s letter, the second is the computer's letter.

      if letter == 'X':

          return ['X', 'O']

      else:

          return ['O', 'X']

def startfirst():

      # Randomly choose the player who goes first.

      if random.randint(0, 1) == 0:

          return 'computer'

      else:

          return 'player'


def getPlayerMove(board):

      # Let the player type in their move.

      move = ' '

      while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):

        move=  input('\n\t\tWhat is your next move? (1-9): ')

          

      return int(move)



def playboard(board):

       # This function prints out the board that it was passed.

  

       # "board" is a list of 10 strings representing the board (ignore index 0)

      print('                          |   |'    )

      print('                        ' + board[1] + ' | ' + board[2] + ' | ' + board[3])

      print('                          |   |'    )

      print('                     --------------'  )

      print('                          |   |'    )

      print('                        ' + board[4] + ' | ' + board[5] + ' | ' + board[6])

      print('                          |   |'    )

      print('                     --------------' )

      print('                          |   |'    )

      print('                        ' + board[7] + ' | ' + board[8] + ' | ' + board[9])

      print('                          |   |'    )


 

 

def makeMove(board, letter, move):

      board[move] = letter

 

def winner(board, letr):

      # Given a board and a player’s letter, this function returns True if that player has won.

      # We use board in place of board-list and letr instead of letter so we don’t get confuse as much.

      return ((board[1] == letr and board[2] == letr and board[3] == letr) or # across the top

      (board[4] == letr and board[5] == letr and board[6] == letr) or # across the middle
      (board[7] == letr and board[8] == letr and board[9] == letr) or # across the bottom

      (board[1] == letr and board[4] == letr and board[7] == letr) or # down the left side

      (board[2] == letr and board[5] == letr and board[8] == letr) or # down the middle

      (board[3] == letr and board[6] == letr and board[9] == letr) or # down the right side

      (board[1] == letr and board[5] == letr and board[9] == letr) or # diagonal

      (board[3] == letr and board[5] == letr and board[7] == letr)) # diagonal

 

def getBoardCopy(board):

      # Make a duplicate of the board list and return it the duplicate.

      dupeBoard = []

 

      for i in board:

          dupeBoard.append(i)

 

      return dupeBoard


 

 

def randommove(board, movesList):

      # Returns a valid move from the passed list on the passed board.

      # Returns None if there is no valid move.

      possibleMoves = []

      for i in movesList:

          if isSpaceFree(board, i):

              possibleMoves.append(i)

 

      if len(possibleMoves) != 0:

          return random.choice(possibleMoves)

      else:

         return None



def computermove(board, computerLetter):

     # Given a board and the computer's letter, determine where to move and return that move.

     if computerLetter == 'X':

         playerLetter = 'O'

     else:

         playerLetter = 'X'



     # Here is our algorithm for our Tic Tac Toe AI:

     # First, check if we can win in the next move

     for i in range(1, 10):

         copy = getBoardCopy(board)

         if isSpaceFree(copy, i):

             makeMove(copy, computerLetter, i)

             if winner(copy, computerLetter):

                 return i



     # Check if the player could win on their next move, and block them.

     for i in range(1, 10):

         copy = getBoardCopy(board)

         if isSpaceFree(copy, i):

             makeMove(copy, playerLetter, i)

             if winner(copy, playerLetter):

                 return i



     # Try to take one of the corners, if they are free.

     move = randommove(board, [1, 3, 7, 9])

     if move != None:

         return move



     # Try to take the center, if it is free.

     if isSpaceFree(board, 5):

         return 5



     # Move on one of the sides.
     return randommove(board, [2, 4, 6, 8])


def isSpaceFree(board, move):

      # Return true if the passed move is free on the passed board.

      return board[move] == ' '


def isBoardFull(board):

     # Return True if every space on the board has been taken. Otherwise return False.

     for i in range(1, 10):

         if isSpaceFree(board, i):

             return False

     return True


def playanothertime():

      # This function returns True if the player wants to play again, otherwise it returns False.

      print('\n\t\tDo you want to play again? (yes or no)')

      return input().lower().startswith('y')

print('\n\t\tWelcome to Tic Tac Toe!\n')


while True:

     # Reset the board

     theBoard = [' '] * 10

     playerLetter, computerLetter = play()

     turn = startfirst()

     print('\n\t\tThe ' + turn + ' will go first.\n\n')

     gameIsPlaying = True



     while gameIsPlaying:

         if turn == 'player':

             # Player’s turn.

             playboard(theBoard)

             move = getPlayerMove(theBoard)

             makeMove(theBoard, playerLetter, move) 



             if winner(theBoard, playerLetter):

                 playboard(theBoard)

                 print('\n\t\tHooray! You have won the game!')

                 gameIsPlaying = False

             else:

                 if isBoardFull(theBoard):

                     playboard(theBoard)

                     print('\n\t\tThe game is a tie!')

                     break

                 else:

                     turn = 'computer'



         else:

             # Computer’s turn.

             move = computermove(theBoard, computerLetter)

             makeMove(theBoard, computerLetter, move)

 
             if winner(theBoard, computerLetter):

                 playboard(theBoard)

                 print('\n\t\tThe computer has beaten you! You lose.')

                 gameIsPlaying = False

             else:

                 if isBoardFull(theBoard):

                     playboard(theBoard)

                     print('\n\t\tThe game is a tie!')

                     break

                 else:

                     turn = 'player'



     if not playanothertime():

         break


