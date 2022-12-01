import random, os

class Player:
    def __init__(self, numb, board):
        self.playerNumber = numb
        self.playerBoard = board
        self.ships = ["Carrier", "Battleship", "Destroyer", "Submarines", "Patrol Boat"]

        self.maxColumn = len(self.playerBoard[0]) - 1
        self.letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.maxLetter = self.letters[len(self.playerBoard) - 2]

    def player(self):
        print("\nPlayer: ", self.playerNumber)

    def getNumber(self):
        return self.playerNumber

    def getBoard(self):
        return self.playerBoard

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

class HumanPlayer(Player):
    def __init__(self, numb, board):
        super().__init__(numb, board)

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
                rowIndex = self.letters.index(self.getRow(size,direc)) + 1  #placing
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
        return self.playerBoard

    def takeShot(self):  # gets vaild coordinates - sends to gameboard.takeshot() - relays results of shot
        x = int(input(f"Enter column to shoot (1-{self.maxColumn}): "))
        while x < 1 or x > self.maxColumn:
            x = int(input(f"Invalid column. Re-enter column number for the ship's front (1-{self.maxColumn}): "))

        y = input(f"Enter row letter for ship's front (A-{self.maxLetter}): ").upper()
        while not (y >= "A" or y <= self.maxLetter):
            y = input(
                f"Invalid column. Re-enter column number for the ship's front (A-{self.maxLetter}): ").upper()
        y = self.letters.index(y) + 1

        return x, y

    def getColumn(self, size, direc):  # gets valid column
        while True:
            try:
                if direc == 2:  # part of placing the ships
                    newMaxColumn = (self.maxColumn - size) + 1
                else:
                    newMaxColumn = self.maxColumn
                x = int(input(f"Enter column number for the ship's front (1-{newMaxColumn}): "))
                while x < 1 or x > newMaxColumn:
                    x = int(
                        input(f"Invalid column. Re-enter column number for the ship's front (1-{newMaxColumn}): "))
                return x
            except:
                print("Not a interger. Try again: ")

    def getRow(self, size, direc):  # gets valid row
        while True:
            try:
                if direc == 1:
                    newMaxLetter = self.letters[(self.letters.index(self.maxLetter) - size) + 1]
                else:
                    newMaxLetter = self.maxLetter
                y = input(f"Enter row Letter for the ship's front (A-{newMaxLetter}): ").upper()
                while not ((y >= "A" or y <= newMaxLetter)):
                    y = input(f"Invalid column. Re-enter column number for the ship's front (A-{newMaxLetter}):").upper()
                return y
            except:
                print("Not a letter. Try again")

class ComputerPlayer(Player):

    def placeShips(self):

        for x in range(len(self.ships)):
            direc = random.randint(1, 2)
            size = 5 - x

            while True:
                column = self.getColumn(size, direc)  # placeing
                rowIndex = self.letters.index(self.getRow(size,direc)) + 1  #placing
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
        return self.playerBoard

    def takeShot(self):
        x = random.randint(1, self.maxColumn)
        y = random.randint(1, self.letters.index(self.maxLetter))
        return x, y

    def getColumn(self, size, direc):
        if direc == 2:  # part of placing the ships
            newMaxColumn = (self.maxColumn - size) + 1
        else:
            newMaxColumn = self.maxColumn
        x = random.randint(1, newMaxColumn)
        return x

    def getRow(self, size, direc):  # gets valid row
        if direc == 1:
            newMaxLetter = self.letters[(self.letters.index(self.maxLetter) - size) + 1]
        else:
            newMaxLetter = self.maxLetter
        y = self.letters[random.randint(1, self.letters.index(newMaxLetter))]
        return y

class GameBoard:
    def __init__(self):
        self.columns, self.rows = self.BoardSize()
        self.PlayerBoard = self.CreateBoard()
        self.displayBoard = self.CreateBoard()
        self.ComputerBoard = self.CreateBoard()

        self.players = [self.PlayerBoard, self.ComputerBoard]

    def BoardSize(self):
        self.columns = int(input("\nEnter the number of columns: ")) + 1
        while self.columns < 11 or self.columns > 27:
            self.columns = int(
                input("Invalid input. Re-enter the number of columns: ")) + 1

        self.rows = int(input("\nEnter the number of rows: ")) + 1
        while self.rows < 11 or self.rows > 27:
            self.rows = int(
                input("Invalid input. Re-enter the number of rows: ")) + 1

        return self.columns, self.rows

    def CreateBoard(self):
        letters = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        board = []
        for y in range(self.rows):
            board.append([])
            board[y].append(letters[y])
            for x in range(self.columns - 1):
                if y == 0:
                    board[y].append(str(x + 1))
                else:
                    board[y].append(" ")
        board[0][0] = " "
        return board

    def display(self):  # displays player's board
        os.system('cls')
        print("\n Player's Board:")
        for y in range(len(self.PlayerBoard)):
            for x in range(len(self.PlayerBoard[y])):
                if y == 0:
                    print(self.PlayerBoard[y][x], end="   ")
                else:
                    print(self.PlayerBoard[y][x], end=" | ")
            print("\n" + "  " + "-" * ((self.columns * 4) - 2))

        print("\n Enemy Board status: ")
        for y in range(len(self.displayBoard)):
            for x in range(len(self.displayBoard[y])):
                if y == 0:
                    print(self.displayBoard[y][x], end="   ")
                else:
                    print(self.displayBoard[y][x], end=" | ")
            print("\n" + "  " + "-" * ((self.columns * 4) - 2))

    def getWidth(self):
        return self.columns

    def getHight(self):
        return self.rows

    def takeShot(self, playerNum, x, y):  # takes shot a recived coordinates and returns results
        if playerNum == 1:
            TargetBoard = self.ComputerBoard
        else:
            TargetBoard = self.PlayerBoard
        if TargetBoard[y][x] == "S":
            status = "H"
            print("hit")
        else:
            status = "X"
            print("miss")

        TargetBoard[y][x] = status
        if playerNum == 1:
            self.displayBoard[y][x] = status

    def placeShips(self, HumanBoard, ComputerBoard):  # places ships on respective boards and updates all boards
        self.PlayerBoard = HumanBoard
        self.ComputerBoard = ComputerBoard

    def checkWinner(self, numb):  # tests if all ships(S) are hit(X)
        if numb == 1:
            CheckBoard = ComputerPlayer.getBoard()
        else:
            CheckBoard = HumanPlayer.getBoard()
        print(f"\n\n{CheckBoard}\n\n")
        hits = [x for y in range(1, len(CheckBoard)) for x in range(1, len(CheckBoard[y])) if CheckBoard[y][x] == "H"]
        print(hits)
        print(f"Player {numb}: {len(hits)} hits")
        if len(hits) == 15:
            print(f"Player {numb} wins!")
            os.system('quit')


GameBoard = GameBoard()
HumanPlayer = HumanPlayer(1, GameBoard.PlayerBoard)
ComputerPlayer = ComputerPlayer(2, GameBoard.ComputerBoard)
players = [HumanPlayer, ComputerPlayer]

GameBoard.display()
GameBoard.placeShips(HumanPlayer.placeShips(), ComputerPlayer.placeShips())

while True:
    for player in players:
        if player == HumanPlayer:
            GameBoard.display()
        GameBoard.checkWinner(player.getNumber())
        x, y = player.takeShot()
        GameBoard.takeShot(player.getNumber(), x, y)
