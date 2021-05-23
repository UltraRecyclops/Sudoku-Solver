import numpy as np

Sudoku = np.array([(0, 0, 6, 1, 0, 0, 3, 4, 5),
                   (8, 0, 1, 0, 4, 0, 7, 2, 0),
                   (0, 0, 3, 6, 0, 2, 8, 9, 1),
                   (5, 6, 0, 0, 2, 0, 9, 1, 3),
                   (3, 4, 2, 0, 0, 9, 0, 8, 7),
                   (0, 0, 7, 3, 0, 0, 0, 0, 0),
                   (0, 8, 0, 0, 0, 1, 4, 7, 0),
                   (0, 1, 0, 4, 6, 7, 0, 0, 0),
                   (0, 0, 0, 0, 0, 0, 0, 0, 0)])


Sudoku1 = np.array([(1, 0, 5, 0, 0, 4, 0, 0, 0),
                    (0, 4, 0, 8, 0, 6, 0, 0, 0),
                    (0, 0, 0, 0, 0, 9, 2, 5, 0),
                    (0, 5, 0, 0, 7, 3, 0, 6, 2),
                    (0, 0, 0, 0, 0, 0, 0, 7, 0),
                    (6, 0, 0, 9, 0, 0, 0, 3, 0),
                    (0, 8, 1, 6, 0, 0, 0, 4, 0),
                    (0, 3, 0, 1, 0, 0, 7, 0, 0),
                    (5, 0, 0, 0, 0, 7, 0, 9, 0)
                    ])


testSudoku = np.array([(1, 2, 3),
                       (4, 5, 6),
                       (7, 8, 9)])

Standard = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])



# shows True if the space is empty
def emptyspaces(Sudoku, y, x):
    if Sudoku[y][x] == 0:
        return True
    else:
        return False

def CannotBe(Set, y, x):
    cannotbey = []
    cannotbex = []
    cannotbe = []
    n = 9
    #first we will do the y values, or using a constant x (vertical lines)
    for a in range(n):
        if a == y:
            continue
        if emptyspaces(Set, a, x) == True:
            continue
        else:
            cannotbex.append(Set[a][x])

    #now we will do the y values, or using a constant y (horizontal lines)
    for b in range(n):
        if b == x:
            continue
        if emptyspaces(Set, y, b) == True:
            continue
        else:
            cannotbey.append(Set[y][b])
    cannotbe += cannotbex + cannotbey

    #SQUARES
    if y < 3:
        if x < 3:
            for i in range(0, 3):
                for j in range(0, 3):
                    cannotbe.append(Set[i][j])
        if x > 2 and x < 6:
            for i in range(0, 3):
                for j in range(3, 6):
                    cannotbe.append(Set[i][j])
        if x > 5:
            for i in range(0, 3):
                for j in range(6, 9):
                    cannotbe.append(Set[i][j])
    if y < 6 and y > 2:
        if x < 3:
            for i in range(3, 6):
                for j in range(0, 3):
                    cannotbe.append(Set[i][j])
        if x > 2 and x < 6:
            for i in range(3, 6):
                for j in range(3, 6):
                    cannotbe.append(Set[i][j])
        if x > 5:
            for i in range(3, 6):
                for j in range(6, 9):
                    cannotbe.append(Set[i][j])
    if y > 5:
        if x < 3:
            for i in range(6, 9):
                for j in range(0, 3):
                    cannotbe.append(Set[i][j])
        if x > 2 and x < 6:
            for i in range(6, 9):
                for j in range(3, 6):
                    cannotbe.append(Set[i][j])
        if x > 5:
            for i in range(6, 9):
                for j in range(6, 9):
                    cannotbe.append(Set[i][j])



    cannotbe += cannotbex + cannotbey
    return cannotbe

#returns True if there are still unsolved points
def CheckIfSolved(Sudoku):
    if 0 in Sudoku:
        return True
    else:
        return False


count = 0
depth = 0
maxdepth = 0
def RecSolver(Sudoku):
    global count, depth, maxdepth
    if maxdepth < depth:
        maxdepth = depth

    for y in range(9):
        for x in range(9):
            if emptyspaces(Sudoku, y, x) == False:
                continue
            else:
                CB = set(CannotBe(Sudoku, y, x))# set gets rid of duplicates
                CB1 = np.array(list(CB))
                CanBe = np.setdiff1d(Standard, CB1)
                #print(CanBe)
                #if len(CanBe) == 1:
                 #   Sudoku[y][x] = CanBe
                  #  print(str(x) + str(y))
                   # print(Sudoku)
                if len(CanBe) == 0:
                    #print("error with CanBe values", "Cell (y, x) (" + str(y) + ", " + str(x) + ")")
                    #print(Sudoku)
                    return
                else:
                    for i in CanBe:
                        Sudoku[y][x] = i
                        count += 1
                        depth += 1
                        RecSolver(Sudoku)
                        depth -= 1
                        if CheckIfSolved(Sudoku) == False:
                            print(Sudoku)
                    Sudoku[y][x] = 0
                    return



RecSolver(Sudoku1)
print("count: " + str(count))
print("depth: " + str(depth))
print("maxdepth: " + str(maxdepth))
















