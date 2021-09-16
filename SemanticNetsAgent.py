class State:
    def __init__(self, state_vars, num_moves=0, move=(0, 0), parent=None):
        self.state_vars = state_vars
        self.num_moves = num_moves
        self.parent = parent
        self.move = move

    @classmethod
    def initialState(cls, initialSheep, initialWolves):
        return cls((initialSheep, initialWolves, 1))

    def get_possible_moves(self):
        ''' return all possible moves in the problem as tuples
        possible moves
        '''
        moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]
        return moves

    def is_legal(self, initialSheep, initialWolves):
        sheep, wolves, boat = self.state_vars

        if sheep < 0 or sheep > initialSheep:
            return False
        elif wolves < 0 or wolves > initialWolves:
            return False
        return True

    def is_solution(self):
        if self.state_vars == (0, 0, 0):
            return True
        return False

    def is_failure(self, initialSheep, initialWolves):
        sheep, wolves, boat = self.state_vars

        if sheep > 0 and sheep < wolves:
            return True

        sheep_on_left = initialSheep - sheep
        wolves_on_left = initialWolves - wolves

        if sheep_on_left > 0 and sheep_on_left < wolves_on_left:
            return True
        return False

    def get_next_states(self, initialSheep, initialWolves):
        moves = self.get_possible_moves()
        all_states = list()
        sheep_right, wolves_right, boat_right = self.state_vars
        #If boat is on right, remove move from state
        #If boat is on left, add move to state
        for move in moves:
            change_sheep, change_wolves = move
            if boat_right == 1:
                new_state_vars = (sheep_right - change_sheep, wolves_right - change_wolves, 0)
            else:
                new_state_vars = (sheep_right + change_sheep, wolves_right + change_wolves, 1)

            # The number of moves increases by 1
            # Passing self to child.
            new_state = State(new_state_vars, self.num_moves + 1, move, self)
            if new_state.is_legal(initialSheep, initialWolves):
                all_states.append(new_state)

        return all_states, move


class SemanticNetsAgent:
    def __init__(self):
        pass

    def solve(self, initialSheep, initialWolves):

        from collections import deque
        initialState = State.initialState(initialSheep, initialWolves)
        to_search = deque()
        seen_states = set()
        solutions = list()

        to_search.append(initialState)

        #Avoid infinit loops
        loop_count = 0
        max_loop = 10000

        all_depths = []

        while len(to_search) > 0:
            loop_count += 1
            if loop_count > max_loop:
                print(len(to_search))
                print("Exiting long loop")
                break

            current_state = to_search.pop()
            next_states, move = current_state.get_next_states(initialSheep, initialWolves)

            for possible_next_state in next_states[::-1]:
                possible_state_vars = possible_next_state.state_vars
                if possible_state_vars not in seen_states:
                    all_depths.append(possible_next_state.num_moves)

                    if possible_next_state.is_failure(initialSheep, initialWolves):
                        continue
                    elif possible_next_state.is_solution():
                        solutions.append((possible_next_state, len(all_depths) - 1))
                        continue

                    to_search.append(possible_next_state)
                    seen_states.add(possible_state_vars)

        results = []
        if len(solutions) != 0:
            current_state = solutions[0][0]
            i = 0
            while current_state:
                current_state = current_state.parent
                i += 1
            lenmin = i
            min_state = solutions[0][0]
            respon = []
            for i in range(0, len(solutions)):
                j = 0
                current_state = solutions[i][0]
                respon.append(current_state)
                while current_state:
                    current_state = current_state.parent
                    j += 1
                if j < lenmin:
                    min_state = solutions[i][0]

            while min_state:
                results.append(min_state.move)
                min_state = min_state.parent
            results.remove((0, 0))
        return results