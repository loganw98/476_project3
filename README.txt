Created by Logan Williams
Computer Science 476X
Due Thursday, March 5th, 2020 at 11:59 pm

Inside of this project are 4 files, 3 of which are runnable

Runnables:
rrtNoObstacles.py
rrt.py
rrtWithSolution.py


File Explanations:
graph.py is the file that contains all data structures (graph, vertex, and edges)

rrtNoObstacles runs the rapidly exploring search tree over the entire state space, with no regards to the obstacles

rrt runs the rapidly exploring search tree over the state space, with points stopping about .005 away from each obstacle.
There is no goal in this one, so it runs for however many iterations that you specify in file

rrtWithSolution does exactly what rrt does, but also periodically checks whether or not it can reach the goal node. If so,
it adds it to the graphical interface and ends the program. I have also written in a search algorithm that prints out an order
from start to finish, even though it was not specified in the assignment document


How to run the above files in linux (make sure to have pygame):

python3 rrtNoObstacles.py
python3 rrt.py
python3 rrtWithSolution.py