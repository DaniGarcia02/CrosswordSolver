# CrosswordSolver

This is an exercise I made at University to learn about Backtracking and Forwardchecking.

The exercise consists in finding a solution to a crossword puzzle, we have a board where we have to add words and a dictionary with all the words to try. To solve this problem we make a Backtracking algorithm that uses Forward Checking to reduce the options we have to try and optimize the time in which we arrive at the solution. 

To optimize even further the search we use a Minimum Remaining Values heuristic, this means that in each step of the algorithm we will always choose the option that has the least amount of options to try to avoid making unnecessary steps.
