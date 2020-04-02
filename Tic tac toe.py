from random import randint, choice
DICTS = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

# функция возвращает размерность доски, введеную пользователем (есть проверка ввода)
def start() -> int:
    print("Добро пожаловать в игру 'Крестики нолики'!")
    print("Введите размерность доски (от 3 до 5)")
    while True:
        n = input()
        if not n.isnumeric():
            print("Некорректный ввод. Попробуйте снова: ")
        elif 3 <= int(n) <= 5:
            break
        else:
            print("Число не в диапазоне. Попробуйте снова")
    return int(n)

# в зависимости от размерности доски возвращается список выигрышных комбинаций
def winComb(n: int) -> tuple:
    combinations = ()
    for i in range(N):
        gor = ()
        ver = ()
        diag = ()
        for j in range(N):
            gor += (i * N + j,)
            ver += (i + j * N,)
            if i == 0 or i == 1:
                diag += ((j + i) * (N + (-1) ** i),)
        combinations += (gor, ver,)
        if i == 0 or i == 1:
            combinations += (diag,)
    return combinations

def who():
    print("С кем вы хотите сыграть? C другом (f) или компьютером (с)?")
    option = ''
    options = {'f': True, 'c': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()
    return options[option]

def valuesOfDict(n: int) -> list:
    mylist = []
    for i in DICTS.values():
        mylist.append(i)
    return mylist[:n]


def keysOfDict(n: int) -> list:
    mylist = []
    for i in DICTS.keys():
        mylist.append(i)
    return mylist[:n]

def printBoard(arr: list, n: int):  # функция для отрисовки доски
    keys = (' ', 'a', 'b', 'c', 'd', 'e')
    values = ('1', '2', '3', '4', '5')
    massiv = []
    for i in range(n):
        start = i * n
        end = (i + 1) * n
        massiv.append(arr[start:end])    
    for i in range(n + 1):
        if i == 0:  # вывод 1 строки
            str1 = keys[i] + ' | '
            for j in range(n):
                str1 = str1 + values[j] + ' | '
            print(str1)
        else:
            str2 = keys[i] + ' | '
            for j in range(n):
                if massiv[i - 1][j] == '':
                    str2 = str2 + '_' + ' | '
                else:
                    str2 = str2 + massiv[i - 1][j] + ' | '
            print("-" * N * 5)
            print(str2)

def can_move(arr: list, move, n: int) -> bool:  # проверка, может ли игрок сходить на эту клетку
    if len(move) == 2:
        if move[1].isnumeric():
            if (move[0] in keysOfDict(n)) and (int(move[1]) in valuesOfDict(n)):
                if arr[(DICTS.get(move[0]) - 1) * n + int(move[1]) - 1] == '':
                    return True
    return False

def make_move(arr: list, move: str, n: int, player: str):
    arr[(DICTS.get(move[0]) - 1) * n + int(move[1]) - 1] = player

def checkWin(arr: list, n: int, char: str) -> bool:
    win = winComb(n)
    pobeda = False
    for i in range(len(win)):
        h = 0
        for j in range(N):
            if arr[win[i][j]] == char:
                h += 1
        if h == n:
            pobeda = True
    return pobeda
    
def player_move(arr: list, n: int, player: str, players: int):
    s = "Ход игрока " + players + " - " + player
    print("\033[1m {} \033[0m".format(s))
    print("Введите ячейку в формате 'a1': ")
    while True:
        move = input()
        if can_move(arr, move, n):
            make_move(arr, move, n, player)
            return
        else:
            print("Некорректный ввод. Попробуйте еще раз:")

def select_random(foe) :
    if foe:
        players = ('Player 1', 'Player 2')
    else:
        players = ('Player 1', 'Computer')
    if randint(0,1) == 0:
        return players[::-1]
    return players

def computer_move(arr: list, n: int, player: str):
    s = "Ход компьютера" + " - " + player
    print("\033[1m {} \033[0m".format(s))
    new_arr = list(arr)
    code = ('X', 'O')
    for i in range(len(code)):
        if code[i] != player:
            playerAnother = code[i]
    freeCells = []
    for i in range(n**2):
        if arr[i] == '':
            freeCells.append(i)
    for i in freeCells: #пройдемся по свободным ячейкам, если мы можем выиграть то ставим сюда
        new_arr[i] = player
        if checkWin(new_arr, n, player):
            arr[i] = player
            return
        else:
            new_arr[i] = ''
    for i in freeCells:
        new_arr[i] = playerAnother
        if checkWin(new_arr, n, playerAnother):
            arr[i] = player
            return   
        else:
            new_arr[i] = ''
    arr[choice(freeCells)] = player

if __name__ == '__main__':
    N = start()
    arr = (['']) * N ** 2
    foe = who()  #True - играем с другом, False - с компьютером 
    print("\033[1m {} \033[0m".format("Подбрасываем монетку, кто будет ходить первым (первыми ходят [Х])"))
    players = select_random(foe)
    print("[X] ходит %s, [O] ходит %s" % (players[0], players[1]))    
    printBoard(arr, N)
    k = 0
    #while k < 1:
    while k < N ** 2:
        if k % 2 == 0:
            if players[0] == 'Computer':
                computer_move(arr, N, 'X')
            else:
                player_move(arr, N, 'X', players[0])
            printBoard(arr, N)
            if checkWin(arr, N, 'X'):
                print("\033[1m {} \033[0m".format("Выиграл  %s" % players[0]))
                break
        else:
            if players[1] == 'Computer':
                computer_move(arr, N, 'O')
            else:
                player_move(arr, N, 'O', players[1])
            printBoard(arr, N)
            if checkWin(arr, N, 'O'):
                print("\033[1m {} \033[0m".format("Выиграл %s" % players[1]))
                break
        k += 1
        if k == N ** 2:
            print('Ничья!')
