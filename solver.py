board = [
    [0,0,4, 0,5,0,  0,0,0],
    [0,0,6, 0,0,0,  0,3,0],
    [5,3,0, 7,0,0,  0,0,8],

    [1,2,0, 0,6,0,  0,8,0],
    [0,0,3, 0,0,0,  0,0,0],
    [0,0,0, 0,0,9,  0,0,7],

    [4,0,0, 0,0,0,  0,0,0],
    [8,5,0, 0,1,0,  0,2,0],
    [0,0,0, 6,0,0,  1,0,0]
]

board1 =  [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]


def valid(bo, num, pos):
    # Checks if i is in the row
    for i in range(len(bo[0])):
        if pos[1] != i and bo[pos[0]][i] == num:
            return False
    # Checks if i is in the column
    for i in range(len(bo)):
        if pos[0] != i and bo[i][pos[1]] == num:
            return False

    # Checks if i is in the box
    box_x = pos[1] // 3
    box_y = pos[0] // 3
    for i in range(box_y * 3, box_y *3 +3):
        for j in range(box_x * 3, box_x *3 +3):
            if bo[i][j] == num and (i,j) != pos:
                return False

    return True

def solve(bord):
    print(bord)
    find = find_empty(bord)
    if not find:
        return True
    else:
        row, col = find


    for integer in range(1,10):
        if valid(bord, integer, (row, col)):
            bord[row][col] = integer

            if solve(bord):
                return True

            bord[row][col] = 0

    return False

def print_board(bo):
    # Prints board neatly for a greater overview
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")

def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j]==0:
                return (i,j)
    return None

print_board(board)
solve(board)
print("")
print_board(board)
