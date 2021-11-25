board = []
solution_board = []

move_x = [2, 1, -1, -2, -2, -1, 1, 2]
move_y = [1, 2, 2, 1, -1, -2, -2, -1]


def convert_print(new_board):
    index = 0

    for row in new_board:
        for column in row:
            board[index] = str(column).rjust(placeholder_size)
            index += 1
    print("\nHere's the solution!")
    print_board(board)


def print_board(new_board):
    # global placeholder_size
    if placeholder_size == 1:
        print(' ', end='')
    print(' '*(placeholder_size - 1), end='')
    print(f'{"-"*((placeholder_size + 1) * board_width + 3)}')
    for row in range(board_height, 0, -1):
        print(str(row).rjust(placeholder_size - 1), end="| ")
        for column in range(0, board_width):
            # print(f'Board height: {board_height}')
            # print(row, column)
            # print((row * board_width) - board_width + column)
            print(new_board[(row * board_width) - board_width + column], end=" ")
        print("|")
    if placeholder_size == 1:
        print(' ', end='')
    print(' ' * (placeholder_size - 1), end='')
    print(f'{"-"*((placeholder_size + 1) * board_width + 3)}')
    if placeholder_size == 1:
        print(' ', end='')
    print(" "*placeholder_size, end="")
    for index in range (1, board_width + 1):
        print(f'{str(index).rjust(placeholder_size + 1)}', end="")
    print()


def enter_move(x, y):
    # global board
    # global placeholder_size
    board[x - 1 + (y - 1) * board_width] = " " * (placeholder_size - 1) + "X"


def place_move(x, y):
    # print(x, y)
    if 0 < x <= board_width and 0 < y <= board_height:
        if x - 1 + (y - 1) * board_width < len(board):
            if board[x - 1 + (y - 1) * board_width] != "_"*placeholder_size:
                return 0
            num = check_possible_moves(x, y)
            board[x - 1 + (y - 1) * board_width] = " " * (placeholder_size - 1) + str(num)
            # print("true")
            return 1
        else:
            # print("false")
            return 0
    # print("FALSE")
    return 0


def calculate_possible_moves(pos_c, pos_r):
    for i in range(len(board)):
        if board[i].strip().isnumeric():
            board[i] = "_"*placeholder_size
    count = 0
    count += place_move(pos_c + 2, pos_r + 1)
    count += place_move(pos_c + 2, pos_r - 1)
    count += place_move(pos_c - 2, pos_r + 1)
    count += place_move(pos_c - 2, pos_r - 1)
    count += place_move(pos_c + 1, pos_r + 2)
    count += place_move(pos_c + 1, pos_r - 2)
    count += place_move(pos_c - 1, pos_r + 2)
    count += place_move(pos_c - 1, pos_r - 2)
    return count


def check_possible_moves(pos_c, pos_r):
    count = 0
    count += check_move(pos_c + 2, pos_r + 1)
    count += check_move(pos_c + 2, pos_r - 1)
    count += check_move(pos_c - 2, pos_r + 1)
    count += check_move(pos_c - 2, pos_r - 1)
    count += check_move(pos_c + 1, pos_r + 2)
    count += check_move(pos_c + 1, pos_r - 2)
    count += check_move(pos_c - 1, pos_r + 2)
    count += check_move(pos_c - 1, pos_r - 2)
    return count - 1


def check_move(x, y):
    if 0 < x <= board_width and 0 < y <= board_height:
        if x - 1 + (y - 1) * board_width < len(board):
            return 1
        else:
            # print("false")
            return 0
    # print("FALSE")
    return 0


def prepare_board_for_next_move():
    count = 0
    for i in range(len(board)):
        if board[i].strip().isnumeric():
            # board[i] = "_"*placeholder_size
            count += 1
    if count == 0:
        return False
    return True


def check_visited():
    count = 0
    for i in range(len(board)):
        if board[i] == " "*(placeholder_size - 1) + "X" or board[i] == " "*(placeholder_size - 1) + "*":
            count += 1
    return count


def check_possible_square(x, y):
    if 0 < x <= board_width and 0 < y <= board_height:
        if x - 1 + (y - 1) * board_width < len(board) and board[x - 1 + (y - 1) * board_width].strip().isnumeric():
            print('true')
            return True
        else:
            # print(board[x - 1 + (y - 1) * board_width].strip())
            # print("false")
            return False
    # print("FALSE")
    return False


def clear_x():
    for index in range(len(board)):
        if board[index] == " "*(placeholder_size - 1) + "X":
            board[index] = " "*(placeholder_size - 1) + "*"


def ask_user():
    answer = ""
    while answer != 'n' and answer != 'y':
        answer = input("Do you want to try the puzzle? (y/n): ")
        if answer != 'n' and answer != 'y':
            print('Invalid option!', end=" ")
    return answer == 'y'


def validate_move(bo, row, col):
    if row < board_height and row >= 0 and col < board_width and col >= 0 and bo[row][col] == 0:
        return True


def solve(bo, row, col, n, counter):
    for i in range(8):
        if counter >= len(board) + 1:
            return True
        new_x = row + move_x[i]
        new_y = col + move_y[i]
        if validate_move(bo, new_x, new_y):
            bo[new_x][new_y] = counter
            if solve(bo, new_x, new_y, n, counter + 1):
                return True
            # print(bo)
            bo[new_x][new_y] = 0
    return False


first_move = True
invalid_board = True
possible_moves = True
user_solve = True
solution_possible = True
while possible_moves and user_solve and solution_possible:
    while invalid_board:
        board_dimensions = input("Enter your board dimensions: ").split()
        if len(board_dimensions) != 2:
            print("Invalid dimensions!")
        elif board_dimensions[0].isnumeric() and board_dimensions[1].isnumeric():
            board_width = int(board_dimensions[0])
            board_height = int(board_dimensions[1])
            if board_width <= 0 or board_height <= 0:
                print("Invalid dimensions!")
            else:
                size = board_width * board_height
                placeholder_size = len(str(size))
                board = ["_" * placeholder_size] * size
                invalid_board = False
        else:
            print("Invalid dimensions!")

    invalid = True
    while invalid:
        if first_move:
            coordinates = input("Enter the knight's starting position: ").split()
        else:
            coordinates = input("Enter your next move: ").split()
        if len(coordinates) != 2:
            print("Invalid dimensions!")
        elif coordinates[0].isnumeric() and coordinates[1].isnumeric():
            c = int(coordinates[0])
            r = int(coordinates[1])
            if 0 < c <= board_width and 0 < r <= board_height:
                if not first_move:
                    if check_possible_square(c, r):
                        invalid = False
                        clear_x()
                        enter_move(c, r)
                    else:
                        print("Invalid move!", end=" ")
                else:
                    invalid = False
                    enter_move(c, r)
                    first_move = False
                    user_solve = ask_user()
                    if board_width >= 4 or board_height >= 4:
                        pass
                    else:
                        solution_possible = False
            else:
                print("Invalid move!", end=" ")
        else:
            print("Invalid position!")

    if not invalid and solution_possible and user_solve:
        # print("Here are the possible moves:")
        if calculate_possible_moves(c, r) == 0:
            possible_moves = False
        print_board(board)
        print()
        if not prepare_board_for_next_move():
            possible_moves = False

if not solution_possible:
    print("No solution exists!")
elif user_solve:
    number_visited = check_visited()
    if number_visited == len(board):
        print("What a great tour! Congratulations!")
    else:
        print("No more possible moves!")
        print(f'Your knight visited {number_visited} squares!')
else:
    solution_board = [[0] * board_width for x in range(board_height)]
    # print(solution_board)
    solution_board[r - 1][c - 1] = 1
    # print(solution_board)
    solve(solution_board, r - 1, c - 1, 8, 2)
    convert_print(solution_board)
