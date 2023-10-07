import sys 
sys.path.append('aima-python')
from search import *


def test_hill_climbing():
    prob1 = PeakFindingProblem((0, 0), [[0, 5, 10, 20],
                                       [-3, 7, 11, 5]])
    print("Problem 1 Max coords: ",hill_climbing(prob1))
    
    prob2 = PeakFindingProblem((0, 0), [[0, 5, 10, 8],
                                       [-3, 7, 9, 999],
                                       [1, 2, 5, 11]])
    print("Problem 2 Max coords: ",hill_climbing(prob2))
    
    prob3 = PeakFindingProblem((2, 0), [[0, 5, 10, 8],
                                       [-3, 7, 9, 999],
                                       [1, 2, 5, 11]])
    print("Problem 3 Max coords: ",hill_climbing(prob3))


def test_simulated_annealing():
   prob4 = PeakFindingProblem((0, 0), [[0, 5, 10, 20],
                                       [-3, 7, 11, 5]], directions4)
   sols = {prob4.value(simulated_annealing(prob4)) for _ in range(100)}
   print("Solutions, Simulated Annealing Problem 4: ", sols)
   print("Maximum = ", max(sols))
   sol = simulated_annealing_full(prob4)
   print("full simulated annealing = ", sol)

   check_ele = (0,3)
   x=list(filter(lambda i:(i==check_ele),sol))
   print("tuple (0, 3) occurs: ",len(x),"times")
   print("out of: ", len(sol), " items")
   

   
#    prob = PeakFindingProblem((0, 0), [[0, 5, 10, 8],
#                                       [-3, 7, 9, 999],
#                                       [1, 2, 5, 11]], directions8)
#   sols = {prob.value(simulated_annealing(prob)) for i in range(100)}
#    assert max(sols) == 999

#test_hill_climbing()