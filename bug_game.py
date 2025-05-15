import random

SIZE = 7  # размер поля 7x7
NUM_LEAVES = 6  # количество листочков
NUM_OBSTACLES = 5  # количество препятствий
NUM_BONUSES = 2  # количество бонусов
MAX_TURNS = 26  # максимум ходов до дождя


# Подготовка поля
def create_board():
    board = [['.' for _ in range(SIZE)] for _ in range(SIZE)]
    leaves = set()
    obstacles = set()
    bonuses = set()

    # Препятствия
    while len(obstacles) < NUM_OBSTACLES:
        x, y = random.randint(0, SIZE - 1), random.randint(0, SIZE - 1)
        if (x, y) != (0, 0) and (x, y) != (SIZE - 1, SIZE - 1):
            obstacles.add((x, y))

    # Листочки
    while len(leaves) < NUM_LEAVES:
        x, y = random.randint(0, SIZE - 1), random.randint(0, SIZE - 1)
        if (x, y) != (0, 0) and (x, y) != (SIZE - 1, SIZE - 1) and (x, y) not in obstacles:
            leaves.add((x, y))

    # Бонусы
    while len(bonuses) < NUM_BONUSES:
        x, y = random.randint(0, SIZE - 1), random.randint(0, SIZE - 1)
        if (x, y) != (0, 0) and (x, y) != (SIZE - 1, SIZE - 1) and (x, y) not in obstacles and (x, y) not in leaves:
            bonuses.add((x, y))

    for (x, y) in obstacles:
        board[x][y] = '🚧'
    for (x, y) in leaves:
        board[x][y] = '☘️'
    for (x, y) in bonuses:
        board[x][y] = '🎁'

    board[SIZE - 1][SIZE - 1] = '🌳'  # укрытие
    return board, leaves, obstacles, bonuses


# Поле
def print_board(board, bug_pos):
    for i in range(SIZE):
        row = ''
        for j in range(SIZE):
            if (i, j) == bug_pos:
                row += '🐞 '
            else:
                row += board[i][j] + ' '
        print(row)
    print()

# Передвижение
def move_bug(pos, direction):
    x, y = pos
    if direction == 'w' and x > 0:
        x -= 1
    elif direction == 's' and x < SIZE - 1:
        x += 1
    elif direction == 'a' and y > 0:
        y -= 1
    elif direction == 'd' and y < SIZE - 1:
        y += 1
    else:
        print("Нельзя так ходить!")
    return (x, y)

# Игра
def game():
    board, leaves, obstacles, bonuses = create_board()
    bug_pos = (0, 0)
    turns = 0
    max_turns = MAX_TURNS
    print("Игра «Жучок собирает листочки»")
    print("Управление: w - вверх, s - вниз, a - влево, d - вправо")
    print("Собери все листочки (☘️) и доберись до укрытия (🌳) до дождя!")
    print(f"Будь осторожен: препятствия (🚧) заставляют пропускать ход.")
    print(f"Найди бонус (🎁), чтобы получить +2 хода.")
    print_board(board, bug_pos)

    skip_next_turn = False

    while turns < max_turns:
        if skip_next_turn:
            print("Ты пропускаешь ход из-за препятствия!")
            skip_next_turn = False
            turns += 1
            print(f"Ходов осталось до дождя: {max_turns - turns}")
            continue

        move = input("Твой ход (w/a/s/d): ").lower()
        if move not in ['w', 'a', 's', 'd']:
            print("Некорректный ход, попробуй ещё.")
            continue

        new_pos = move_bug(bug_pos, move)

        if new_pos == bug_pos:
            continue

        bug_pos = new_pos
        turns += 1

        if bug_pos in leaves:
            leaves.remove(bug_pos)
            print("Ты собрал листочек!")
            board[bug_pos[0]][bug_pos[1]] = '.'

        elif bug_pos in obstacles:
            print("Ой, ты наткнулся на препятствие и пропускаешь следующий ход!")
            skip_next_turn = True

        elif bug_pos in bonuses:
            print("Ура! Ты нашёл бонус и получил +2 хода!")
            max_turns += 2
            bonuses.remove(bug_pos)
            board[bug_pos[0]][bug_pos[1]] = '.'

        print_board(board, bug_pos)
        print(f"Осталось листочков: {len(leaves)}. Ходов осталось до дождя: {max_turns - turns}")

        if len(leaves) == 0:
            print("Все листочки собраны! Теперь доберись до укрытия.")

        if len(leaves) == 0 and bug_pos == (SIZE - 1, SIZE - 1):
            print("Ты успешно добрался до укрытия и выиграл! Поздравляю!")
            return

    if bug_pos == (SIZE - 1, SIZE - 1) and len(leaves) == 0:
        print("Ты успел спрятаться до дождя! Победа!")
    else:
        print("Начался дождь, и ты не успел добраться до укрытия. Проигрыш.")


if __name__ == "__main__":
    game()