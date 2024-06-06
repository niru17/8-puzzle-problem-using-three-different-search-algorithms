import graphlib
from queue import Queue
import sys
import numpy as np
import heapq

traceFileName = "trace_file.txt"


def printAllSteps(path):
    stateArr = np.array(start_state)
    for move in path:
        zeroX, zeroY = np.where(stateArr == 0)
        tileValue = stateArr[move[0]][move[1]]
        direction = getDirection((zeroX[0], zeroY[0]), (move[0], move[1]))
        stateArr[zeroX[0]][zeroY[0]], stateArr[move[0]][move[1]] = stateArr[move[0]][move[1]], stateArr[zeroX[0]][zeroY[0]]
        print(f"\tMove {tileValue} {direction}")

def print_output(popped_nodes, expanded_nodes, generated_nodes, max_size_fringe, depth, path, cost):
    global traceFileName
    print(f"Nodes Popped: {popped_nodes}")
    print(f"Nodes Expanded: {expanded_nodes}")
    print(f"Nodes Generated: {generated_nodes}")
    print(f"Max Fringe Size: {max_size_fringe}")
    print(f"Solution Found at depth {depth} with cost of {cost}")
    print("Steps:")
    printAllSteps(path)
    if flag:
        with open(traceFileName, 'a') as traceFile:
                fileString = "Nodes Popped: "+str(popped_nodes)+"\nNodes Expanded: "+str(expanded_nodes)+"\nNodes Generated: "+str(generated_nodes)+ "\nSolution Found at depth "+ str(len(path)) + " with cost of "+ str(cost) + "\n"
                traceFile.write(fileString)

def getDirection(start_pos, end_pos):
    x = end_pos[0] - start_pos[0]
    y = end_pos[1] - start_pos[1]
    if y == 1:
        return "Left"
    elif y == -1:
        return "Right"
    elif x == 1:
        return "Up"
    elif x == -1:
        return "Down"
    else:
        return None


def read_input_file(filename):
    try:
        state = []
        with open(filename, "r") as f:
            for line in f:
                if "END OF FILE" in line:
                    break
                row = line.strip().split()
                row = [int(x) if x != "0" else 0 for x in row]
                state.append(row)
        return state
    except:
        print(f"Error reading file: {filename}")

def calculateCost(state, move):
    (x1, y1), (x2, y2) = move
    return abs(state[x2][y2] - state[x1][y1])


def findPosition(state, element):
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j] == element:
                return (i, j)

def ucs(start_state, goal_state):
    global traceFileName
    popped_nodes, expanded_nodes, generated_nodes, max_size_fringe = 0, 0, 0, 0
    fringe = []
    visited_nodes = set()
    heapq.heappush(fringe, (0, [], start_state))
    while len(fringe):
        max_size_fringe = max(max_size_fringe, len(fringe))
        cost, path, state = heapq.heappop(fringe)
        popped_nodes += 1
        if state == goal_state:
            depth = len(path)
            print_output(popped_nodes, expanded_nodes, generated_nodes, max_size_fringe,depth, path, cost)
            return path
        if str(state) in visited_nodes:
            continue
        visited_nodes.add(str(state))
        expanded_nodes += 1
        x, y = findPosition(state, 0)
        moves = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
        for move in moves:
            if 0 <= move[0] < 3 and 0 <= move[1] < 3:
                new_state = [row[:] for row in state]
                tempTile = new_state[move[0]][move[1]]
                new_state[x][y] = tempTile
                new_state[move[0]][move[1]] = 0
                move_cost = calculateCost(new_state, (move, (x, y)))
                generated_nodes += 1
                heapq.heappush(fringe, (cost + move_cost, path + [move], new_state))
    return None

def bfs(start_state, goal_state):
    global traceFileName
    popped_nodes, expanded_nodes, generated_nodes, max_size_fringe = 0, 0, 0, 0
    fringe = Queue()
    visited_nodes = set()
    fringe.put((start_state, [], 0))
    while not fringe.empty():
        max_size_fringe = max(max_size_fringe, fringe.qsize())
        state, path, cost = fringe.get()
        popped_nodes += 1
        if state == goal_state:
            depth = len(path)
            print_output(popped_nodes, expanded_nodes, generated_nodes, max_size_fringe,depth, path, cost)
            return path
        if str(state) in visited_nodes:
            continue
        visited_nodes.add(str(state))
        expanded_nodes += 1
        x, y = findPosition(state, 0)
        moves = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
        for move in moves:
            if 0 <= move[0] < 3 and 0 <= move[1] < 3:
                new_state = [row[:] for row in state]
                tempTile = new_state[move[0]][move[1]]
                new_state[x][y] = tempTile
                new_state[move[0]][move[1]] = 0
                move_cost = calculateCost(new_state, (move, (x, y)))
                generated_nodes += 1
                fringe.put((new_state, path + [move], cost + move_cost))
    return None





def dfs(start_state, goal_state):
    global traceFileName
    popped_nodes, expanded_nodes, generated_nodes, max_size_fringe = 0, 0, 0, 0
    stack = [(start_state, [], 0)]
    visited_nodes = set()
    while stack:
        max_size_fringe = max(max_size_fringe, len(stack))
        state, path, cost = stack.pop()
        popped_nodes += 1
        if state == goal_state:
            depth = len(path)
            print_output(popped_nodes, expanded_nodes, generated_nodes, max_size_fringe,depth, path, cost)
            return path
        if str(state) in visited_nodes:
            continue
        visited_nodes.add(str(state))
        expanded_nodes += 1
        x, y = findPosition(state, 0)
        moves = [(x, y+1),(x, y-1), (x+1, y),(x-1, y)]
        for move in moves:
            if 0 <= move[0] < 3 and 0 <= move[1] < 3:
                new_state = [row[:] for row in state]
                tempTile = new_state[move[0]][move[1]]
                new_state[x][y] = tempTile
                new_state[move[0]][move[1]] = 0
                move_cost = calculateCost(new_state, (move, (x, y)))
                generated_nodes += 1
                stack.append((new_state, path + [move], cost + move_cost))

def bfs(start_state, goal_state):
    popped_nodes, expanded_nodes, generated_nodes, max_size_fringe = 0, 0, 0, 0
    fringe = Queue()
    visited_nodes = set()
    fringe.put((start_state, [], 0))
    while not fringe.empty():
        max_size_fringe = max(max_size_fringe, fringe.qsize())
        state, path, cost = fringe.get()
        popped_nodes += 1
        if state == goal_state:
            depth = len(path)
            print_output(popped_nodes, expanded_nodes, generated_nodes, max_size_fringe,depth, path, cost)
            return path
        if str(state) in visited_nodes:
            continue
        visited_nodes.add(str(state))
        expanded_nodes += 1
        x, y = findPosition(state, 0)
        moves = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
        for move in moves:
            if 0 <= move[0] < 3 and 0 <= move[1] < 3:
                new_state = [row[:] for row in state]
                tempTile = new_state[move[0]][move[1]]
                new_state[x][y] = tempTile
                new_state[move[0]][move[1]] = 0
                move_cost = calculateCost(new_state, (move, (x, y)))
                generated_nodes += 1
                print(move)
                fringe.put((new_state, path + [move], cost + move_cost))
    return None


if __name__=="__main__":
    src_file= sys.argv[1]
    # src_file='start.txt'
    dest_file= sys.argv[2]
    # dest_file='goal.txt'

    start_state = read_input_file(src_file)
    goal_state = read_input_file(dest_file)

    algo=sys.argv[3]
    flag=False
    if(len(sys.argv) == 5 and sys.argv[4] == "true"):
        flag= True


if algo=="bfs":
    bfs(start_state, goal_state)
elif algo=="dfs":
     dfs(start_state, goal_state)
elif algo=="ucs":
     ucs(start_state, goal_state)
else:
    print("Unknown algorithm")