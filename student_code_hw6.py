import sys 
sys.path.append('aima-python')
from logic import *

class HW6:
    def __init__(self):
        pass

    def problem_1(self):
        problem_1_list = [] #placeholder, populate this with your statements
        results = [] # iteratively append the results to this
        #iterate over the problems and append the tt_true result to the list 
        #return the list of results
        return results

    def problem_2(self):
        problem_2_list = [] #placeholder, populate this with your statements
        results = [] # iteratively append the results to this
        #iterate over the problems and append the dpll_satisfiable result to the list 
        #return the list of results
        return results

    def problem_3(self):
        KB = None #placeholder, populate this with your statements
        alpha = None #placeholder, populate this with your statements
        #pass in your KB and alpha and return the pl_resolution result
        return None #placeholder

    def problem_4(self):
        KB = None
        alpha = None
        #return the pl_resolution result
        return None #placeholder


def main():

    hw = HW6()

    #problem 1
    print(hw.problem_1())

    #problem 2
    print(hw.problem_2())

    #problem 3
    print(hw.problem_3())

    #problem 4
    print(hw.problem_4())
    

if __name__ == '__main__':
    main()
