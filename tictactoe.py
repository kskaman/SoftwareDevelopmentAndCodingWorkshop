import random

board = [[" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]]
    


available_boxes = []
for i  in range(0, 3):
    for j in range(0, 3):
        available_boxes.append([i, j])


def isFilled(row, col):
    if (board[row][col] == " "):
        return False
    return True

def fill_box(row, col, user):
    if (user == 1):
        board[row][col] = "o"
    else:
        board[row][col] = "x"
    available_boxes.remove([row, col])

def comp_move():
    box = random.choice(available_boxes)
    row = box[0]
    col = box[1]

    fill_box(row, col, 0)


def player_move(user):
    
    if (user == 0):
        comp_move()
        return
    
    print("\nYour move.\nEnter row and column number of box you want to enter : ")
    while (True):
        row = int(input("Enter row number (choose from 1, 2 or 3): "))
        col = int(input("Enter column number (choose from 1, 2 or 3): "))
        if ((row < 1 or row > 3) or (col < 1 or col > 3)):
            print("\nPlease make a valid selection\n")
            continue

        if (not isFilled(row-1, col-1)):
            fill_box(row-1, col-1, user)
            break
        else:
            print("Please choose an empty box to fill.")
            continue


def boardFilled():
    for i in range(0, 3):
        for j in range(0, 3):
            if (board[i][j] == " "):
                return False
    return True

def print_board():
    print("\n\n")
    print("-------------")
    for i in range(0, 3):
        print("| ", end="")
        for j in range(0, 3):
            print(board[i][j] + " | ", end="")
        print("\n-------------")
    print("\n\n")


def finished():
    
    for i in range(0, 3):
        if (board[0][i] == board[1][i] == board[2][i] != " "):
            return board[0][i]
        
    for i in range(0, 3):
        if (board[i][0] == board[i][1] == board[i][2] != " "):
            return board[i][0]

    
    if (board[0][0] == board[1][1] == board[2][2] != " "):
        return board[0][0]
    if (board[0][2] == board[1][1] == board[2][0] != " "):
        return board[0][2]

    return None



def main():
    print("LET'S START.")
    
    print("Type 'single' to play against computer. Enter 'double' to pay against a fellow.")
    c = input()
    type = c.strip()
    while (type != 'single' and type != 'double'):
        print("You made invalid selection. Please enter 'single' or 'double' in lower case only.")
        c = input()
        type = c
    
    if (type == 'double'):
        user2 = 2
    else :
        user2 = 0
    
    print_board()

    isfinished = finished()
    isBoardFilled = boardFilled
    while(isfinished == None):
        print("Player 1's turn : ")
        player_move(1)
        print_board()
        isfinished = finished()

        isBoardFilled = boardFilled()
        if (isBoardFilled):
            break
        if (user2 == 2):
            print("Player 2's turn : ")
        else:
            print("\n\nComputer's turn : \n\n")
        player_move(user2)
        print_board()
        isfinished = finished()
        isBoardFilled = boardFilled()
        if (isBoardFilled):
            break

    if (isBoardFilled):
        print("\n\nIt's a DRAW.\n\n")
        return
    
    if (isfinished == "o"):
        print("\n\nPlayer 1 WON.\n\n")
    else:
        if (user2 == 2):
            print("\nPlayer 2 WON.\n\n")
        else:
            print("Computer WON.\n\n")

main()
