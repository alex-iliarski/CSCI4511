import sys
sys.path.append('aima-python')
from search import *
import math

class HW4:

    def __init__(self):
        pass

    def example_problem_1(self, eight_puzzle, search):
        #EightPuzzle example with A*
        return search(eight_puzzle).solution()

    def problem_1a(self, eight_puzzle, search):
        '''
        problem 1a
        1. The start state of the 8 puzzle is (0, 1, 3, 4, 2, 5, 7, 8, 6)
        2. The goal state of the 8 puzzle is (1, 2, 3, 4, 5, 6, 7, 8, 0)
        3. Pass in the EightPuzzle object and use the A* search to solve.
        4. Return the solution.
        '''
        return search(eight_puzzle).solution()
    
    def problem_1b(self, eight_puzzle, search):
        '''
        problem 1b
        1. The start state of the 8 puzzle is (2,1,3,4,6,5,7,8,0)
        2. The goal state of the 8 puzzle is (1, 2, 3, 4, 0, 5, 6, 7, 8)
        3. Pass in the EightPuzzle object and use the A* search to solve.
        4. Return the solution.
        '''
        return search(eight_puzzle).solution() 

    def problem_2a(self, eight_puzzle, search):
        '''
        problem 2a - Example of code with question to answer in homework
        - see the code in the Homework 4 assignment and add it below
        1.  call search (A*) with 8-Puzzle and different heuristics (default and manhattan)
        2. return the solutions found by the search with default heuristic and
            search with the manhattan distance heuristic        
        
        '''
        default_sol = search(eight_puzzle).solution()
        manhattan_sol = search(eight_puzzle, h=self.manhattan).solution()
        return (default_sol, manhattan_sol)

    def problem_2b(self, eight_puzzle, search):
        '''
        problem 2b - Uses different eight puzzle start state than 2a 
        1.  call search (A*) with 8-Puzzle and different heuristics (default and manhattan)
        2. return the solutions found by the search with default heuristic and
            search with the manhattan distance heuristic 
        '''
        #  Put code for problem 2b here
        default_sol = search(eight_puzzle).solution()
        manhattan_sol = search(eight_puzzle, h=self.manhattan).solution()
        return (default_sol, manhattan_sol)
        
    def problem_3a(self):
     
        '''
        problem 3a
        1. create the the two romania graph problems specified in problem 3a
        2. create the list of search algorithms
        3. run each search algorithm on each problem and append the results to a list
        4. return each list of solutions (2 lists!)
        '''
    
        # Fill in the missing pieces 
        r_graph1_prob1 = GraphProblem("Timisoara", "Bucharest", romania_map)
        r_graph2_prob2 = GraphProblem("Hirsova", "Sibiu", romania_map)
        r1 = []
        r2 = []
        search_algorithms_list = [depth_first_graph_search, iterative_deepening_search, breadth_first_graph_search, uniform_cost_search, astar_search]
        for algorithm in search_algorithms_list:
            r1.append(algorithm(r_graph1_prob1).solution())
            r2.append(algorithm(r_graph2_prob2).solution())
        return r1, r2

    def problem_3b(self):
        '''
        1. read the documentation from: 
https://github.com/aimacode/aima-python/blob/master/search.py on compare_searchers
        2. return the result from the compare searchers for searchers
           specified in problem 3
        '''
        return compare_searchers([GraphProblem("Hirsova", "Sibiu", romania_map)], header=['Search Algorithm', 'romania_map(Hirsova, Sibiu)'])

    # This assumes that the goal state is (1, 2, 3, 4, 5, 6, 7, 8, 0)
    def manhattan(self,node):
        state = node.state
        index_goal = {0:[2,2], 1:[0,0], 2:[0,1], 3:[0,2], 4:[1,0], 5:[1,1], 6:[1,2], 7:[2,0], 8:[2,1]}

        index_state = {}
        index = [[0,0], [0,1], [0,2], [1,0], [1,1], [1,2], [2,0], [2,1], [2,2]]
        x, y = 0, 0
 
        for i in range(len(state)):
            index_state[state[i]] = index[i]
    
        mhd = 0
        for i in range(8):
            for j in range(2):
                mhd = abs(index_goal[i][j] - index_state[i][j]) + mhd
    
        return mhd
        
    def problem_4(self):
        '''
        problem 4
    
        Hill Climbing problem (Problem 4)
            1. create the two peak finding problems, one for part a, one for part b 
               (see tests/test_search.py in aima code for examples on how to do this)       
            2. return each result:
                - one for hill climbing on the 1st peak finding  problem (part a)
                - one for hill climbing on the 2nd peak finding problem(part b) 
            3.  Answer the questions for this problem in your HW4_YourName.pdf
        '''
        prob1 = PeakFindingProblem((0, 0),  [[1, 6, 11, 9],
                                           [-2, 8, 10, 20],
                                            [2, 3, 6, 12]])
        res1 = hill_climbing(prob1)
        
        prob2 = PeakFindingProblem((1, 1),  [[1, 6, 11, 9],
                                           [-2, 8, 10, 20],
                                            [2, 3, 6, 12]])
        res2 = hill_climbing(prob2)
        
        return res1, res2

def main():
    
    # Create object, hw4, of datatype HW4.
    hw4 = HW4()
 
    #=======================
    # A* with 8-Puzzle 
    # An example for you to follow to get you started on the EightPuzzle
    puzzle = EightPuzzle((2, 4, 3, 1, 5, 6, 7, 8, 0))
    # Checks whether the initialized configuration is solvable or not
    # comment out before submitting!!!
    # puzzle.check_solvability((2, 4, 3, 1, 5, 6, 7, 8, 0))
    print("A* with default heuristic")
    print(hw4.example_problem_1(puzzle, astar_search))
    

    #=======================
  
    print("Problem 1a")
    # Put code for problem 1a here
    puzzle = EightPuzzle((0, 1, 3, 4, 2, 5, 7, 8, 6), (1, 2, 3, 4, 5, 6, 7, 8, 0))
    print(hw4.problem_1a(puzzle, astar_search))

    #=======================
  
    print("Problem 1b")
    # Put code for problem 1b here
    puzzle = EightPuzzle((2,1,3,4,6,5,7,8,0), (1, 2, 3, 4, 0, 5, 6, 7, 8))
    print(hw4.problem_1b(puzzle, astar_search))

    #=======================
    '''
    problem 2a - Example of code with question to answer in homework
    1.  A* with 8-Puzzle and different heuristics (default and manhattan)
        - add the code given in the Homework 4 writeup for the main
          method after the print statement below

    2.  Answer the question for this problem in your HW2_YourName.pdf
    '''
    print("Problem 2a")
    puzzle = EightPuzzle((0, 1, 3, 4, 2, 5, 7, 8, 6))
    # Checks whether the initialized configuration is solvable or not
    puzzle.check_solvability((0, 1, 3, 4, 2, 5, 7, 8, 6))
    default, manhattan = hw4.problem_2a(puzzle, astar_search)
    print("Default Heuristic Solution: ", default)
    print("Manhattan Heuristic Solution: ", manhattan)

    '''
    problem 2b - Use different start state (from question 1 b)
    '''
    print("Problem 2b")
    #  Put code for problem 2b here - format should be the same as 2a
    puzzle = EightPuzzle((2, 1, 3, 4, 6, 5, 7, 8, 0))
    puzzle.check_solvability((2, 1, 3, 4, 6, 5, 7, 8, 0))
    default, manhattan = hw4.problem_2b(puzzle, astar_search)
    print("Default Heuristic Solution: ", default)
    print("Manhattan Heuristic Solution: ", manhattan)
    
    print("Problem 3a")
    #  Call method for Problem 3a here - format should be the same as 2a
    solution1, solution2 = hw4.problem_3a()
    print(solution1)
    print(solution2)
    

    print("Problem 3b")
    #  Call method for Problem 3b here
    print(hw4.problem_3b())
    
    #  Put code for Problem 4 here
    print("Problem 4")
    hc_Prob1, hc_Prob2 = hw4.problem_4()
    #print row, column of solution for each problem
    print(hc_Prob1)
    print(hc_Prob2)

    
 

    
    

    
    
    

    
if __name__ == "__main__":
    main()


