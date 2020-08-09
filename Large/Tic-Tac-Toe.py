SIZE = 3
board = [] #Start with an empty list
for y in range(SIZE):
    #Each element in the board will also be a list
    board.append([])
    for x in range(SIZE):
        # Fill our inner list with the coordinates:
        board[y].append("[%d][%d]" % (y, x))

#Print the board as a grid
for row in board:
    for column in row:
        print("%s " % column, end="")
    print("\n")

#Adding gameplay
print("\n\nPlayer X is moving.\n\n")
board[0][2] = "X" #<--- Placing an X at this coordinate

#Print the board as a grid
for row in board:
    for column in row:
        print("%s " % column, end="")
    print("\n")

#We added nested for-loops, and since we wanted the values (instead of the indexes), we did not use the range() function.

print("\n\nPlayer Y is moving.\n\n")
board[1][1] = "Y"

#Print the board as a grid again
for row in board:
    for column in row:
        print("%s " % column, end="")
    print("\n")

print("\n\nPlayer X is moving.\n\n")
board[1][2] = "X"

for row in board:
    for column in row:
        print("%s " % column, end="")
    print("\n")

print("\n\nPlayer Y is moving.\n\n")
board[2][2] = "Y"

for row in board:
    for column in row:
        print("%s " % column, end="")
    print("\n")

print("\n\nPlayer X is moving.\n\n")
board[0][0] = "X"

for row in board:
    for column in row:
        print("%s " % column, end="")
    print("\n")

print("\n\nPlayer Y is moving.\n\n")
board[0][1] = "Y"

for row in board:
    for column in row:
        print("%s " % column, end="")
    print("\n")

print("\n\nPlayer X is moving.\n\n")
board[2][1] = "X"

for row in board:
    for column in row:
        print("%s " % column, end="")
    print("\n")

print("\n\nPlayer Y is moving.\n\n")
board[1][0] = "Y"

for row in board:
    for column in row:
        print("%s " % column, end="")
    print("\n")

print("\n\nPlayer X is moving.\n\n")
board[2][0] = "X"

for row in board:
    for column in row:
        print("%s " % column, end="")
    print("\n")
