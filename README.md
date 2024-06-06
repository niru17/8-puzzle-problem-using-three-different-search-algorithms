# 8-puzzle-problem-using-three-different-search-algorithms

This program is solving the 8-puzzle problem using three different search algorithms: Breadth-First Search (BFS), Depth-First Search (DFS), and Uniform-Cost Search (UCS). Here's a breakdown of what the code is doing:

Overview

The 8-puzzle is a sliding puzzle that consists of a 3x3 grid with tiles numbered 1 to 8 and a blank space (represented by 0). The goal is to move the tiles around until they match a specified goal configuration.

Key Functions

printAllSteps(path): This function prints each move taken to reach the goal state from the start state. It updates the state array and prints the direction and tile moved.

print_output(popped_nodes, expanded_nodes, generated_nodes, max_size_fringe, depth, path, cost): This function prints the statistics of the search process (e.g., nodes popped, expanded, generated, max fringe size, etc.) and the steps to reach the goal. It optionally writes these details to a trace file.

getDirection(start_pos, end_pos): This function returns the direction of the move (left, right, up, or down) based on the start and end positions.

read_input_file(filename): This function reads a state configuration from a file. The state is represented as a 2D list.

calculateCost(state, move): This function calculates the cost of a move. The cost is the absolute difference between the tile values of the start and end positions.

findPosition(state, element): This function finds the position of a given element (e.g., the blank space) in the state.

ucs(start_state, goal_state): This function implements the Uniform-Cost Search algorithm. It uses a priority queue (min-heap) to explore nodes with the lowest cumulative cost first.

bfs(start_state, goal_state): This function implements the Breadth-First Search algorithm. It uses a queue to explore nodes level by level.

dfs(start_state, goal_state): This function implements the Depth-First Search algorithm. It uses a stack to explore nodes as deep as possible before backtracking.

Main Execution

The script is designed to be run from the command line with three arguments:

- src_file: The file containing the start state configuration.
- dest_file: The file containing the goal state configuration.
- algo: The algorithm to use (bfs, dfs, or ucs).
- Optionally, a fourth argument true can be provided to enable logging to the trace file.
  
Execution Flow

- Reading the Input Files: The start and goal states are read from the specified files using the read_input_file function.
- Selecting the Algorithm: Based on the third command line argument, the appropriate search algorithm is executed (BFS, DFS, or UCS).
- Search Process: Each search algorithm function (e.g., bfs, dfs, ucs) attempts to find a path from the start state to the goal state. During this process, nodes are popped, expanded, and generated, and their statistics are tracked.

Output: If a solution is found, the print_output function is called to display the results and optionally log them to a trace file.

Example Command Line Execution

python puzzle_solver.py start.txt goal.txt bfs

This command runs the BFS algorithm to solve the puzzle defined by start.txt and goal.txt.
