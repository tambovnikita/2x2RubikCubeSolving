from copy import deepcopy
from rotations import stage1_rotations, stage2_rotations, stage3_rotations


'''
Пример входных данных:

005500
005500
221133
221133
004400
004400
006600
006600

Пример выходных данных:

1 ЭТАП
1)  ( L )
2)  ( L )
3)  ( B )
4)  ( R )
Отчёт: Первый слой кубика полностью собран.

2 ЭТАП
1)  ( U' )
2)  ( U R U' R'  F R' F' R  U )
3)  ( U' )
Отчёт: Детали второго слоя встали на свои места, но не факт, что они правильно повёрнуты.

3 ЭТАП
1)  ( R U R' U'  R U R' U'  R U R' U'  R U R' U' + D )
2)  ( D )
3)  ( U D' )
4)  ( R U R' U'  R U R' U'  R U R' U'  R U R' U' + D )
5)  ( U D' )
6)  ( R U R' U'  R U R' U'  R U R' U'  R U R' U' + D )
Отчёт: Кубик полностью собран.
'''


def from_10_to_X(new_num_sys, value):
    chars = [str(i) for i in range(new_num_sys)]
    res = []
    while value > 0:
        res.append(chars[value % new_num_sys])
        value //= new_num_sys
    return res[::-1] if res else ['0']


def check_stage1(new_mat):
    # условие для первого этапа программы. Если оно выполняется, то заканчивается первый этап и начинается второй
    if (
        new_mat[0][2] == new_mat[0][3] and new_mat[2][0] == new_mat[3][0] and 
        new_mat[2][5] == new_mat[3][5] and new_mat[5][2] == new_mat[5][3] and
        new_mat[6][2] == new_mat[6][3] == new_mat[7][2] == new_mat[7][3]
    ):
        return True
    return False


def check_stage2(new_mat):
    # обозначение деталей второго слоя для выполнения условия
    el1 = [new_mat[1][2], new_mat[2][1], new_mat[2][2]]
    el2 = [new_mat[1][3], new_mat[2][3], new_mat[2][4]]
    el3 = [new_mat[3][1], new_mat[3][2], new_mat[4][2]]
    el4 = [new_mat[3][3], new_mat[3][4], new_mat[4][3]]

    # условие для второго этапа программы. Если оно выполняется, то заканчивается второй этап и начинается третий
    if (
        new_mat[0][2] == new_mat[0][3] and new_mat[0][2] in el1 and new_mat[0][3] in el2 and
        new_mat[2][0] == new_mat[3][0] and new_mat[2][0] in el1 and new_mat[3][0] in el3 and
        new_mat[2][5] == new_mat[3][5] and new_mat[2][5] in el2 and new_mat[3][5] in el4 and
        new_mat[5][2] == new_mat[5][3] and new_mat[5][2] in el3 and new_mat[5][3] in el4 and
        new_mat[6][2] == new_mat[6][3] == new_mat[7][2] == new_mat[7][3]
    ):
        return True
    return False


def check_stage3(new_mat):
    # условие для третьего этапа программы. Если оно выполняется, то выводится ответ и программа завершает работу
    if (
        new_mat[0][2] == new_mat[0][3] == new_mat[1][2] == new_mat[1][3] and
        new_mat[2][0] == new_mat[2][1] == new_mat[3][0] == new_mat[3][1] and
        new_mat[2][2] == new_mat[2][3] == new_mat[3][2] == new_mat[3][3] and
        new_mat[2][4] == new_mat[2][5] == new_mat[3][4] == new_mat[3][5] and
        new_mat[4][2] == new_mat[4][3] == new_mat[5][2] == new_mat[5][3] and
        new_mat[6][2] == new_mat[6][3] == new_mat[7][2] == new_mat[7][3]
    ):
        return True
    return False


# Первый этап. Сборка первого слоя.
def stage1(mat):
    text = ""
    new_mat = deepcopy(mat)
    sequence = []
    if check_stage1(new_mat):
        text += ('1 ЭТАП\n\n')
    else:
        i = 0
        while True:
            sequence = from_10_to_X(new_num_sys=12, value=i)
            
            # поворот граней
            for s in sequence:
                new_mat = stage1_rotations(new_mat, s)

            if check_stage1(new_mat):
                text += ('1 ЭТАП\n\n')
                break
            
            new_mat = deepcopy(mat)
            i += 1

    # Вывод для первого этапа программы
    designations = {
        "0": "F",
        "1": "L",
        "2": "R",
        "3": "R'",
        "4": "U",
        "5": "F'",
        "6": "B'",
        "7": "U'",
        "8": "B",
        "9": "L'",
        "10": "D",
        "11": "D'"
    }

    for i in range(len(sequence)):
        text += f"{i+1}. {designations[sequence[i]]}\n"
    text += '\nОтчёт: Первый слой кубика полностью собран.\n'

    return text, new_mat


# Второй этап. Установка деталей второго слоя на свои места.
def stage2(mat):
    text = ""
    new_mat = deepcopy(mat)
    sequence = []
    if check_stage2(new_mat):
        text += ('2 ЭТАП\n\n')
    else:
        i = 0
        while True:
            sequence = from_10_to_X(new_num_sys=5, value=i)
            
            # поворот граней
            for s in sequence:
                new_mat = stage2_rotations(new_mat, s)

            if check_stage2(new_mat):
                text += ('2 ЭТАП\n\n')
                break
            
            new_mat = deepcopy(mat)
            i += 1

    # Вывод для второго этапа программы
    designations = {
        "0": "U R U' R'  F R' F' R",
        "1": "U'",
        "2": "D",
        "3": "U",
        "4": "D'",
    }
   
    for i in range(len(sequence)):
        text += f"{i+1}. {designations[sequence[i]]}\n"
    text += '\nОтчёт: Детали второго слоя встали на свои места, но не факт, что они правильно повёрнуты.\n'

    return text, new_mat


# Третий этап. Окончательная сборка кубика.
def stage3(mat):
    text = ""
    new_mat = deepcopy(mat)
    sequence = []
    if check_stage3(new_mat):
        text += ('3 ЭТАП\n\n')
    else:
        i = 0
        while True:
            sequence = from_10_to_X(new_num_sys=7, value=i)

            # поворот граней
            for s in sequence:
                new_mat = stage3_rotations(new_mat, s)

            if check_stage3(new_mat):
                text += ('3 ЭТАП\n\n')
                break
            
            new_mat = deepcopy(mat)
            i += 1

    # Вывод для третьего этапа программы
    designations = {
        "0": "U' D",
        "1": "R U R' U'  R U R' U'  R U R' U'  R U R' U'  D",
        "2": "R U R' U'  R U R' U'  D",
        "3": "D",
        "4": "U D'",
        "5": "R U R' U'  D",
        "6": "R U R' U'  R U R' U'  R U R' U'  D"
    }
    
    for i in range(len(sequence)):
        text += f"{i+1}. {designations[sequence[i]]}\n"
    text += '\nОтчёт: Кубик полностью собран.'

    return text
