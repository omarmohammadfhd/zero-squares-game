import copy

from board import game

class prepare :
    def prepare_bfs_inputs(self, game):
        graph = {}
        start_positions = game.positions
        goals = []


        for i in range(len(game.puzzle)):
            for j in range(len(game.puzzle[i])):
                cup = game.puzzle[i][j]
                if cup.goal == 1:
                    goals.append((i, j))


        queue = [(copy.deepcopy(game), tuple(game.positions))]
        visited_states = set()

        while queue:
            current_game, current_positions = queue.pop(0)
            if current_positions in visited_states:
                continue
            visited_states.add(current_positions)


            possible_moves = current_game.next_state()
            graph[current_positions] = []

            for cube_color, direction, new_position in possible_moves:

                new_game = current_game.move(direction)
                new_positions = tuple(new_game.positions)
                if new_positions not in visited_states:
                    graph[current_positions].append(new_positions)
                    queue.append((new_game, new_positions))

        return graph, tuple(start_positions), goals
