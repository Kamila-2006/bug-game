import random

SIZE = 5  # размер поля 5x5
NUM_LEAVES = 5  # количество листочков
MAX_TURNS = 15  # максимум ходов до дождя


def create_board():
    board = [['.' for _ in range(SIZE)] for _ in range(SIZE)]
    leaves = set()
    while len(leaves) < NUM_LEAVES:
        x, y = random.randint(0, SIZE - 1), random.randint(0, SIZE - 1)
        if (x, y) != (0, 0):
            leaves.add((x, y))
    for (x, y) in leaves:
        board[x][y] = 'L'
    board[SIZE - 1][SIZE - 1] = 'U'  # укрытие
    return board, leaves


def print_board(board, bug_pos):
    for i in range(SIZE):
        row = ''
        for j in range(SIZE):
            if (i, j) == bug_pos:
                row += 'B '
            else:
                row += board[i][j] + ' '
        print(row)
    print()


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


def game():
    board, leaves = create_board()
    bug_pos = (0, 0)
    turns = 0
    print("Игра «Жучок собирает листочки»")
    print("Управление: w - вверх, s - вниз, a - влево, d - вправо")
    print("Собери все листочки (L) и доберись до укрытия (U) до дождя!")
    print_board(board, bug_pos)

    while turns < MAX_TURNS:
        move = input("Твой ход (w/a/s/d): ").lower()
        if move not in ['w', 'a', 's', 'd']:
            print("Некорректный ход, попробуй ещё.")
            continue
        bug_pos = move_bug(bug_pos, move)
        turns += 1

        if bug_pos in leaves:
            leaves.remove(bug_pos)
            print("Ты собрал листочек!")
            board[bug_pos[0]][bug_pos[1]] = '.'
        print_board(board, bug_pos)
        print(f"Осталось листочков: {len(leaves)}. Ходов осталось до дождя: {MAX_TURNS - turns}")

        if len(leaves) == 0:
            print("Все листочки собраны! Теперь доберись до укрытия.")

        if len(leaves) == 0 and bug_pos == (SIZE - 1, SIZE - 1):
            print("Ты успешно добрался до укрытия и выиграл! Поздравляю!")
            return

    # если дошли сюда, дождь начался
    if bug_pos == (SIZE - 1, SIZE - 1) and len(leaves) == 0:
        print("Ты успел спрятаться до дождя! Победа!")
    else:
        print("Начался дождь, и ты не успел добраться до укрытия. Проигрыш.")


if __name__ == "__main__":
    game()
