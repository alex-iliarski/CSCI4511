import sys
sys.path.append('aima-python')
from search import *
# statement below is from test_search.py
# all classes, functions, and data structures used
# are found in search.py.
# For this example, the important entites are:
# Important classes: Node, GraphProblem
# Important data structures - romania_map
# Important method/function - breadth_first_graph_search
romania_problem = GraphProblem('Arad', 'Bucharest', romania_map) # from test_search.py
print(breadth_first_graph_search(romania_problem).solution()) # from test_search.py