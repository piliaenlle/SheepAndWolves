# Sheep and Wolves

INTRODUCTION

The Sheep and Wolves problem is an AI game that consists of a shepherd who has to cross a certain number of sheep and wolves across the river in a boat, following some rules:
- The number of wolves on either side of the river cannot outnumber the sheep.
- Wolves can be alone on either side of the river.
- Only one or two animals can be crossed in the boat at a time, not less nor more.


KEY DEFINITIONS

1.1 Initial and Goal state definition:

Before starting, it is important to set the initial and the goal state. They are both represented as a tuple (sheep, wolves, boat), being the initial state the arbitrary number of sheep and wolves given as input. Since the boat is on the left side (position 0), the goal state is to bring the specified number of sheep and wolves to the right, leaving empty the left side, thus, the goal state is represented as (0,0, 0). 

1.2 Move’s generation

It is important to determine all the possible movements of the current state, all delimited by the rules of the problem. These moves are represented as tuples, and since at least one animal has to be transported at a time, and no more than two should be moved in the same journey, the following are the only possible moves:

2 sheep, 0 wolves: (2,0)
1 sheep, 0 wolves: (1,0)
1 sheep, 1 wolf: (1,1)
0 sheep, 2 wolves: (0,2)
0 sheep, 1 wolf: (0,1)

Since the boat just changes from one side to the other, it doesn’t matter on which side it is, thus the move doesn’t consider it.

1.3 Change the current state into the following one

Though trivial, since the problem starts on the left side and its goal is to move all animals to the right side, the chosen move will be subtracted from the current state of animals. This way, the state represents the number of people on the left.

1.4 Tests

To reduce the number of possible moves the agent will try, several tests are run. This helps improve the agent’s productiveness and efficiency since the non-possible moves are removed before being tried by the agent.
Firstly, it is important to determine if the move is legal: there can’t be negative numbers of animals, and the number of sheep or wolves can’t exceed those of the initial state.
Once the ilegal moves are discarded, the agent must verify if the move is a failure and thus breaks the rules, meaning that the number of wolves on either side of the river outnumber the sheep. 

2 IMPORTANT ELEMENTS

The following elements are created to store important information:

to_search: A stack/queue to keep track of where to search next.
seen_states: A set to keep track of the states that were already seen. This avoids the agent to loop over the same solutions over and over again, being unproductive.
solutions: A list to keep track of the solutions that have already been seen.

3 AGENT

With all these definitions and elements determined, the solve method was created to follow the subsequent steps:
- Creates the initial state with initial sheep and wolves as input parameters.
- Starts the search with the initial state and loops until the to_search stack is empty or has exceeded a maximum number of loops (in this case is 10000) to avoid the agent being captured in an infinite loop.
- Gets the next possible states of the current state and applies the legality test to each of them. Once the next state passes that test, it checks if it has already been seen in the seen_states and if it is not the final solution, it appends it in the seen_states set. In case the next state is the goal state, it stores it in the solutions list. 
- Once it finishes iterating over all possible next states, it goes over each of the solutions stored in the solutions list and chooses the one with the least moves to the goal state, returning a list of tuples with all the moves used to solve the problem. In case no solution can be achieved, it returns an empty list.
- Since the agent consists of a smart tester, it doesn’t struggle on any particular case nor with an increasing number of initial sheep and wolves. It avoids a combinatorial explosion by discarding illegal, unproductive and not valid moves before exploring them. This helps to arrive to the solution in a more efficient and fast way. 
