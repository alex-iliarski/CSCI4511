import sys 
sys.path.append('aima-python')
from logic import *

class HW6:
    def __init__(self):
        pass

    def problem_1(self):
        problem_1_list = ['A ==> A', 
                        '(A ==> B) ==> (~A ==> ~B)', 
                        'A | B | ~B', 
                        '(A ==> B) ==> (B ==> C)', 
                        '(A ==> C) ==> ((A & B) ==> C)'
                        ]
        results = [] # iteratively append the results to this
        #iterate over the problems and append the tt_true result to the list 
        for prob in problem_1_list:
            results.append(tt_true(prob))
        
        #return the list of results
        return results

    def problem_2(self):
        problem_2_list = [
            expr('E ==> E'),
            expr('E ==> F'),
            expr('(E & F) | ~F'),
            expr('((G | B) & (~B | A)) ==> (G | A)'),
            expr('(A ==> B) ==> (B ==> C)')
        ] 
        results = [] # iteratively append the results to this
        #iterate over the problems and append the dpll_satisfiable result to the list 
        for prob in problem_2_list:
            results.append(dpll_satisfiable(prob))
        
        #return the list of results
        return results

    def problem_3(self):
        KB = PropKB() #populate this with your statements
        KB.tell(expr('My ==> ~Mo'))
        KB.tell(expr('~My ==> (Mo & Ma)'))
        KB.tell(expr('(~Mo | Ma) ==> H'))
        KB.tell(expr('H ==> Mag'))
        
        alpha = expr('H') # checking if this is entailed in the KB
        
        #pass in your KB and alpha and return the pl_resolution result
        return pl_resolution(KB, alpha)

    def problem_4(self):
        KB = PropKB() # initialize knowledge base
        KB.tell(expr('PSM ==> ~JG'))
        KB.tell(expr('PSM | PLT'))
        KB.tell(expr('PLT ==> JGC'))
        
        alpha = expr('JG ==> JGC') # checking if this is entailed in the KB
        
        #return the pl_resolution result
        return pl_resolution(KB, alpha)



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
