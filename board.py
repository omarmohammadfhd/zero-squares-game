import copy
from puzzle import puzzle
from dfs_and_bfs_algorithm import bfs,dfs
def prepare_bfs_inputs(game):
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

class PuzzleGame:
    def __init__(self, puzzle):
        self.puzzle = puzzle
        self.positions = self.find_initial_positions()


    def find_initial_positions(self):
        red_pos = blue_pos = green_pos = pink_pos = None
        for i in range(len(self.puzzle)):
            for j in range(len(self.puzzle[i])):
                cup = self.puzzle[i][j]
                if cup.color == 'red' and cup.goal == 0:
                    red_pos = (i, j)
                elif cup.color == 'blue' and cup.goal == 0:
                    blue_pos = (i, j)
                elif cup.color == 'green' and cup.goal == 0:
                    green_pos = (i, j)
                elif cup.color == 'pink' and cup.goal == 0:
                    pink_pos = (i, j)
        return [pos for pos in [red_pos, blue_pos, pink_pos, green_pos] if pos is not None]

    def print_puzzle(self):
        for row in self.puzzle:
            for cup in row:
                if cup.color == 'black':
                    print("    X    ", end=" | ")
                elif cup.color == 'white' and cup.goal == 1 and cup.frame_color == 'red':
                    print("  goal   ", end=" | ")
                elif cup.color == 'red' and cup.goal == 0:
                    print("   r     ", end=" | ")
                elif cup.color == 'white' and cup.goal == 1 and cup.frame_color == 'blue':
                    print(" blue te ", end=" | ")
                elif cup.color == 'blue' and cup.goal == 0:
                    print("    b    ", end=" | ")
                elif cup.color == 'green' and cup.goal == 1:
                    print("    G    ", end=" | ")
                elif cup.color == 'green' and cup.goal == 0:
                    print(" Tar gre ", end=" | ")
                elif cup.color == 'pink' and cup.goal == 1:
                    print("    p    ", end=" | ")
                elif cup.color == 'pink' and cup.goal == 0:
                    print(" T pink  ", end=" | ")
                elif cup.color == 'white':
                    print("         ", end=" | ")
                else:
                    print("         ", end=" | ")
            print("\n" + "-" * (len(row) * 12))

    def check_right(self):
        for i, j in self.positions:
            if j + 1 < len(self.puzzle[0]) and self.puzzle[i][j + 1].color == 'white'and puzzle[i][j].is_reach==False:
                return True
        return False

    def check_left(self):
        for i, j in self.positions:
            if j - 1 >= 0 and self.puzzle[i][j - 1].color == 'white'and puzzle[i][j].is_reach==False:
                return True
        return False

    def check_up(self):
        for i, j in self.positions:
            if i - 1 >= 0 and self.puzzle[i - 1][j].color == 'white' and puzzle[i][j].is_reach==False:
                return True
        return False

    def check_down(self):
        for i, j in self.positions:
            if i + 1 < len(self.puzzle) and self.puzzle[i + 1][j].color == 'white'and puzzle[i][j].is_reach==False:
                return True
        return False
    def move_right(self):
        if self.check_right():
            update_pos = []
            for i, j in self.positions:
                new_i_pos, now_j_pos = i, j + 1
                while now_j_pos < len(self.puzzle[0]) and self.puzzle[new_i_pos][now_j_pos].color == 'white':
                    self.puzzle[new_i_pos][now_j_pos].color = self.puzzle[i][j].color
                    self.puzzle[i][j].color = 'white'
                    i, j = new_i_pos, now_j_pos
                    now_j_pos += 1
                update_pos.append((i, j))
            self.positions = update_pos
        else:
            print("you can't move right")


    def move_left(self):
        if self.check_left():
            update_pos = []
            for i, j in self.positions:
                new_i_pos, now_j_pos = i, j - 1
                while now_j_pos >= 0 and self.puzzle[new_i_pos][now_j_pos].color == 'white':
                    self.puzzle[new_i_pos][now_j_pos].color = self.puzzle[i][j].color
                    self.puzzle[i][j].color = 'white'
                    i, j = new_i_pos, now_j_pos
                    now_j_pos -= 1
                update_pos.append((i, j))
            self.positions = update_pos
        else:
            print("you can't move left")


    def move_up(self):
        if self.check_up():
            update_pos = []
            for i, j in self.positions:
                new_i_pos, now_j_pos = i - 1, j
                while new_i_pos >= 0 and self.puzzle[new_i_pos][now_j_pos].color == 'white':
                    self.puzzle[new_i_pos][now_j_pos].color = self.puzzle[i][j].color
                    self.puzzle[i][j].color = 'white'
                    i, j = new_i_pos, now_j_pos
                    new_i_pos -= 1
                update_pos.append((i, j))
            self.positions = update_pos
        else:
            print("you can't move up")


    def move_down(self):
        if self.check_down():
            update_pos = []
            for i, j in self.positions:
                new_i_pos, now_j_pos = i + 1, j
                while new_i_pos < len(self.puzzle) and self.puzzle[new_i_pos][now_j_pos].color == 'white':
                    self.puzzle[new_i_pos][now_j_pos].color = self.puzzle[i][j].color
                    self.puzzle[i][j].color = 'white'
                    i, j = new_i_pos, now_j_pos
                    new_i_pos += 1
                update_pos.append((i, j))
            self.positions = update_pos
        else:
            print("you can't move down")

    def check_reach_goal(self):
        for i, j in self.positions:
            cup = self.puzzle[i][j]
            if cup.goal == 1:
                if cup.frame_color == cup.color:
                    for cube_x, cube_y in self.positions:
                        if (cube_x, cube_y) == (i, j):
                            cube = self.puzzle[cube_x][cube_y]
                            if not cube.is_reach:
                                cube.is_reach = True

                else:
                    cup.is_reach = False

    def move(self, direction):
        new_puzzle = copy.deepcopy(self)

        if direction == 'right':
            new_puzzle.move_right()
        elif direction == 'left':
            new_puzzle.move_left()
        elif direction == 'up':
            new_puzzle.move_up()
        elif direction == 'down':
            new_puzzle.move_down()
        else:
            print("Invalid direction")
            return new_puzzle

        new_puzzle.check_reach_goal()

        new_puzzle.positions = [
            (x, y) for x, y in new_puzzle.positions
            if not new_puzzle.puzzle[x][y].is_reach
        ]

        return new_puzzle


    def next_state(self):
        possible_moves = []

        for x, y in self.positions:

            cube_color = self.puzzle[x][y].color

            def continue_in_direction(dx, dy):
                new_x, new_y = x, y
                while 0 <= new_x + dx < len(self.puzzle) and 0 <= new_y + dy < len(self.puzzle[0]):
                    new_x += dx
                    new_y += dy


                    if self.puzzle[new_x][new_y].color == 'black':
                        new_x -= dx
                        new_y -= dy
                        break


                    if self.puzzle[new_x][new_y].goal and self.puzzle[new_x][new_y].color != self.puzzle[x][y].color:
                        continue

                return new_x, new_y

            if self.check_right():
                final_x, final_y = continue_in_direction(0, 1)
                possible_moves.append((cube_color, "right", (final_x, final_y)))

            if self.check_left():
                final_x, final_y = continue_in_direction(0, -1)
                possible_moves.append((cube_color, "left", (final_x, final_y)))

            if self.check_up():
                final_x, final_y = continue_in_direction(-1, 0)
                possible_moves.append((cube_color, "up", (final_x, final_y)))

            if self.check_down():
                final_x, final_y = continue_in_direction(1, 0)
                possible_moves.append((cube_color, "down", (final_x, final_y)))

        return possible_moves





game = PuzzleGame(puzzle)
# game.print_puzzle()
# game=game.move('up')

# game=game.move('right')
# game.print_puzzle()

#
# game=game.move('down')
# game=game.move('right')

# game=game.move('up')

# game=game.move('left')
# game=game.move('down')
# game=game.move('left')
# game=game.move('down')
# game=game.move('right')

# # game.print_puzzle()
#
# # game.print_puzzle()
# #
# game=game.move('up')
#
game.print_puzzle()

possible_moves = game.next_state()
print(possible_moves)
# # print("Can move right:", game.check_right())
#

graph, start, goals = prepare_bfs_inputs(game)

path, visited = bfs(graph, start, goals)
# path,visited = dfs(graph, start, goals)
print(path)

print(visited)
print(len(visited))