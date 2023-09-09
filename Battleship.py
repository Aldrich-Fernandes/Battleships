import random, os

class Player:
    def __init__(self, numb, board):
        self.__playerNumber = numb
        self.playerBoard = board
        self.ships = ["Carrier", "Battleship", "Destroyer", "Submarines", "Patrol Boat"]

    def player(self):
        print("\nPlayer: ", self.__playerNumber)

    def getNumber(self):
        return self.__playerNumber

    def getBoard(self):
        return self.playerBoard
    
    def setBoard(self, board):
        self.playerBoard = board

    def testValid(self, direc, size, x, y):  # Tests if ship placement is valid
        try:
            if direc == 1:
                for i in range(size):
                    if self.playerBoard[y + i][x] != " ":
                        return False
            elif direc == 2:
                for i in range(size):
                    if self.playerBoard[y][x + i] != " ":
                        return False
        except:
            return False
        return True
    
    def display(self, column):
        os.system('cls')
        print("\n Your Board:")
        for y in range(len(self.playerBoard)):
            for x in range(len(self.playerBoard[y])):
                if y == 0:
                    print(self.playerBoard[y][x], end="   ")
                else:
                    print(self.playerBoard[y][x], end=" | ")
            print("\n" + "  " + "-" * ((column * 4) - 2))

class HumanPlayer(Player):
    def __init__(self, numb, board):
        super().__init__(numb, board)

        self.__maxColumn = len(self.playerBoard[0]) - 1
        self.__letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.__maxLetter = self.__letters[len(self.playerBoard) - 2]

        self.placeShips()

    def placeShips(self):  #gets valid ship placements - replays to gameboard  - Display confriming message that all ships are placed
        print("\nWelcome captain! Your fleet consists of: \n - A Carrier (size:5) \n - A Battleships (size:4) \n - A Destroyer (size:3) \n - A Submarine (size:2) \n - A Patrol Boat (size:1)")
        for x, shipName in enumerate(self.ships):
            while True:
                try:
                    direc = int(input(f"\n How do you want to place your {shipName}: \n1). Verticle \n2). Horizontal \nChoice: "))
                    if direc == 1 or direc == 2:
                        break
                except:
                    print("Not an interger.")
            size = 5 - x

            while True:
                column = self.getColumn(size, direc)  # placeing
                rowIndex = self.__letters.index(self.getRow(size,direc)) + 1  #placing
                if self.testValid(direc, size, column, rowIndex) == True:
                    if direc == 1:  # this is part of placing the ships
                        for i in range(size):
                            try:
                                self.playerBoard[rowIndex + i][column] = "S"
                            except:
                                pass
                    elif direc == 2:
                        for i in range(size):
                            try:
                                self.playerBoard[rowIndex][column + i] = "S"
                            except:
                                pass
                    break
                else:
                    print("Ships collide. Please enter new coordintes.")
        

    def takeShot(self):  # gets vaild coordinates - sends to gameboard.takeshot() - relays results of shot
        x = int(input(f"Enter column to shoot (1-{self.__maxColumn}): "))
        while x < 1 or x > self.__maxColumn:
            x = int(input(f"Invalid column. Re-enter column number for the ship's front (1-{self.__maxColumn}): "))

        y = input(f"Enter row letter for ship's front (A-{self.__maxLetter}): ").upper()
        while not (y >= "A" or y <= self.__maxLetter):
            y = input(f"Invalid column. Re-enter column number for the ship's front (A-{self.__maxLetter}): ").upper()
        y = self.__letters.index(y) + 1

        return x, y

    def getColumn(self, size, direc):  # gets valid column
        while True:
            try:
                if direc == 2:  # part of placing the ships
                    newMaxColumn = (self.__maxColumn - size) + 1
                else:
                    newMaxColumn = self.__maxColumn
                x = int(input(f"Enter column number for the ship's front (1-{newMaxColumn}): "))
                while x < 1 or x > newMaxColumn:
                    x = int(
                        input(f"Invalid column. Re-enter column number for the ship's front (1-{newMaxColumn}): "))
                return x
            except:
                print("Not a interger. Try again. ")

    def getRow(self, size, direc):  # gets valid row
        while True:
            try:
                if direc == 1:
                    newMaxLetter = self.__letters[(self.__letters.index(self.__maxLetter) - size) + 1]
                else:
                    newMaxLetter = self.__maxLetter
                y = input(f"Enter row Letter for the ship's front (A-{newMaxLetter}): ").upper()
                while not ((y >= "A" or y <= newMaxLetter)):
                    y = input(f"Invalid column. Re-enter column number for the ship's front (A-{newMaxLetter}):").upper()
                return y
            except:
                print("Not a letter. Try again")

class ComputerPlayer(Player):
    def __init__(self, numb, board):
        super().__init__(numb, board)

        self.__maxColumn = len(self.playerBoard[0]) - 1
        self.__letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.__maxLetter = self.__letters[len(self.playerBoard) - 2]

        self.placeShips()

    def placeShips(self):

        for x in range(len(self.ships)):
            direc = random.randint(1, 2)
            size = 5 - x

            while True:
                column = self.getColumn(size, direc)  # placeing
                rowIndex = self.__letters.index(self.getRow(size,direc)) + 1  #placing
                if self.testValid(direc, size, column, rowIndex) == True:
                    if direc == 1:  # this is part of placing the ships
                        for i in range(size):
                            try:
                                self.playerBoard[rowIndex + i][column] = "S"
                            except:
                                pass
                    elif direc == 2:
                        for i in range(size):
                            try:
                                self.playerBoard[rowIndex][column + i] = "S"
                            except:
                                pass
                    break
                else:
                    pass

    def takeShot(self):
        x = random.randint(1, self.__maxColumn)
        y = random.randint(1, self.__letters.index(self.__maxLetter))
        return x, y

    def getColumn(self, size, direc):
        if direc == 2:  # part of placing the ships
            newMaxColumn = (self.__maxColumn - size) + 1
        else:
            newMaxColumn = self.__maxColumn
        x = random.randint(1, newMaxColumn)
        return x

    def getRow(self, size, direc):  # gets valid row
        if direc == 1:
            newMaxLetter = self.__letters[(self.__letters.index(self.__maxLetter) - size) + 1]
        else:
            newMaxLetter = self.__maxLetter
        y = self.__letters[random.randint(1, self.__letters.index(newMaxLetter))]
        return y

class GameBoard:
    def __init__(self):
        self.__columns, self.__rows = self.BoardSize()

        self.__displayBoard = self.CreateBoard()

    def BoardSize(self):
        self.__columns = int(input("\nEnter the number of columns (11-27): ")) + 1
        while self.__columns < 11 or self.__columns > 27:
            self.__columns = int(
                input("Invalid input. Re-enter the number of columns (11-27): ")) + 1

        self.__rows = int(input("\nEnter the number of rows (11-27): ")) + 1
        while self.__rows < 11 or self.__rows > 27:
            self.__rows = int(
                input("Invalid input. Re-enter the number of rows (11-27): ")) + 1

        return self.__columns, self.__rows

    def CreateBoard(self):
        self.__letters = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        board = []
        for y in range(self.__rows):
            board.append([])
            board[y].append(self.__letters[y])
            for x in range(self.__columns - 1):
                if y == 0:
                    board[y].append(str(x + 1))
                else:
                    board[y].append(" ")
        board[0][0] = " "
        return board

    def display(self):  # displays player's board

        print("\n Enemy Board status: ")
        for y in range(len(self.__displayBoard)):
            for x in range(len(self.__displayBoard[y])):
                if y == 0:
                    print(self.__displayBoard[y][x], end="   ")
                else:
                    print(self.__displayBoard[y][x], end=" | ")
            print("\n" + "  " + "-" * ((self.__columns * 4) - 2))

    def getWidth(self):
        return self.__columns

    def getHight(self):
        return self.__rows

    def takeShot(self, player, x, y):  # takes shot a recived coordinates and returns results
        targetBoard = player.getBoard()
        if targetBoard[y][x] == "S":
            status = "H"
            print("hit")
        else:
            status = "X"
            print("miss")

        targetBoard[y][x] = status
        player.setBoard(targetBoard)

        if player.getNumber() == 2:
            self.__displayBoard[y][x] = status

    def checkWinner(self, playerNum, enemyBoard):  # tests if all ships(S) are hit(X)
        CheckBoard = enemyBoard
        hits = [x for y in range(1, len(CheckBoard)) for x in range(1, len(CheckBoard[y])) if CheckBoard[y][x] == "H"]
        print(f"Player {playerNum}: {len(hits)} hits")
        if len(hits) == 15:
            print(f"Player {playerNum} wins!")
            os.system('quit')


GameBoard = GameBoard()
HumanPlayer = HumanPlayer(1, GameBoard.CreateBoard())
ComputerPlayer = ComputerPlayer(2, GameBoard.CreateBoard())
players = [HumanPlayer, ComputerPlayer]

while True:
    for player in players:
        EnemyPlayer = ComputerPlayer if player == HumanPlayer else HumanPlayer
        GameBoard.checkWinner(player.getNumber(), EnemyPlayer.getBoard())

        if player == HumanPlayer:
            player.display(GameBoard.getWidth())
            GameBoard.display()
        
        x, y = player.takeShot()
        GameBoard.takeShot(EnemyPlayer, x, y)
