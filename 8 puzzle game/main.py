def printBoard(board):
    print("-------------------")
    print("| ", board[0], " | ", board[1], " | ", board[2], " |")
    print("-------------------")
    print("| ", board[3], " | ", board[4], " | ", board[5], " |")
    print("-------------------")
    print("| ", board[6], " | ", board[7], " | ", board[8], " |")    
    print("-------------------\n")

def moveTile(currState, move):
    gap = currState.index(0)
    nextState = currState.copy()    
    # if move given is to move the gap upward
    # swap it with (gap - 3)th tile in the flattened board as that would be the tile right above the gap    
    if move == 'u':
        nextState[gap - 3], nextState[gap] = nextState[gap], nextState[gap - 3]
    elif move == 'd':
        nextState[gap + 3], nextState[gap] = nextState[gap], nextState[gap + 3]
    elif move == 'l':
        nextState[gap - 1], nextState[gap] = nextState[gap], nextState[gap - 1]
    elif move == 'r':
        nextState[gap + 1], nextState[gap] = nextState[gap], nextState[gap + 1]

    return nextState

def genPossibleStates(currState):
    gap = currState.index(0)
    possibleMoves = []
    possibleStates = []

    # if there is room to move the gap to top
    if gap not in [0, 1, 2]:
        possibleMoves.append('u')
    # if there is room to move the gap to bottom
    if gap not in [6, 7, 8]:
        possibleMoves.append('d')
    # if there is room to move the gap to left
    if gap not in [0, 3, 6]:
        possibleMoves.append('l')
    # if there is room to move the gap to right
    if gap not in [2, 5, 8]:
        possibleMoves.append('r')

    for move in possibleMoves:
        possibleStates.append(moveTile(currState, move))
    
    return possibleStates

def solve(src, dest):        
    numOfMoves = 0
    
    queue = []
    visited = []
    queue.append(src)

    while(len(queue) > 0):
        size = len(queue)

        # layer wise bfs
        while(size):
            currState = queue.pop(0)
            visited.append(currState)

            print("Current state:")
            printBoard(currState)            

            # if curr state is the dest state then break out
            if(currState == dest):
                print("-----------------")
                print("| Final state : |")
                print("-----------------")
                printBoard(currState)
                return numOfMoves

            # generate all possible states from current state
            possibleStates = genPossibleStates(currState)

            # print("--------------")
            # print("Possible state :")
            # print("--------------")
            # for state in possibleStates:
            #     printBoard(state)

            # insert all the possible states into the queue if not visited
            for state in possibleStates:
                if state not in visited and state not in queue:
                    queue.append(state)

            size -= 1

        # increment num of moves as each layer explores one possible move
        numOfMoves += 1

    # return -1 if board not solvable
    return -1

"""
0 denotes an empty space

src : -------------
      | 1 | 2 | 3 | 
      -------------   
      | 4 | 5 | 6 |
      -------------
      | 7 | 8 | 0 |
      -------------

dest : -------------
       | 1 | 2 | 3 | 
       -------------   
       | 0 | 4 | 5 |
       -------------
       | 7 | 8 | 6 |
       -------------

"""
# src flattened board config
src = [1,2,3,4,5,6,7,8,0]

# dest flattened board config
dest = [1,2,3,0,4,5,7,8,6]

# call solve function to start solving
numOfMoves = solve(src, dest)
print("Number of moves taken = ", numOfMoves)