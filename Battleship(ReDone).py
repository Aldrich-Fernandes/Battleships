class Player:
    def __init__(self, numb, board):
        self._playerNumber = numb
        self._playerBoard = board #Gameboard.createBoard()

    def Player(): # creates a new player object
        pass

    def getNumber(): # accessor for playerNumber
        pass

    def getBoard():# accessor for playerBoard
        pass

class HumanPlayer:
    def _placeShips(): # Places ships on board and relays success
        pass

    def takeShot(): # Allows a shot to be taken; relays sucess an allows retake for invalid target
        pass

    def _getColumn(): # gets valid column input
        pass

    def _getRow(): # gets vaild row input
        pass

class ComputerPlayer:
    def _placeShips():
        pass

    def takeShot():
        pass

    def _getColumn():
        pass

    def _getRow():
        pass

class Board:
    def __init__(self):
        self.__columns = 0
        self.__rows = 0
        self.__board = [] # holds each board
        self.__playerNumber = 0

    def Board(): # creates the board when called and return it to the player
        pass

    def display():
        pass

    def getWidth():
        pass

    def getHeight():
        pass

    def takeShot():
        pass

    def placeShip():
        pass

    def checkWinner():
        pass