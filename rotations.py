from copy import deepcopy


def use_simple_rotation(mat, new_mat, type_r):
    
    if type_r == "F":
        new_mat[3][0] = mat[6][3]
        new_mat[3][1] = mat[6][2]
        new_mat[3][2] = mat[3][0]
        new_mat[3][3] = mat[3][1]
        new_mat[3][4] = mat[3][2]
        new_mat[3][5] = mat[3][3]
        new_mat[4][2] = mat[5][2]
        new_mat[4][3] = mat[4][2]
        new_mat[5][2] = mat[5][3]
        new_mat[5][3] = mat[4][3]
        new_mat[6][2] = mat[3][5]
        new_mat[6][3] = mat[3][4]

    elif type_r == "L":
        new_mat[0][2] = mat[6][2]
        new_mat[1][2] = mat[7][2]
        new_mat[2][0] = mat[3][0]
        new_mat[2][1] = mat[2][0]
        new_mat[2][2] = mat[0][2]
        new_mat[3][0] = mat[3][1]
        new_mat[3][1] = mat[2][1]
        new_mat[3][2] = mat[1][2]
        new_mat[4][2] = mat[2][2]
        new_mat[5][2] = mat[3][2]
        new_mat[6][2] = mat[4][2]
        new_mat[7][2] = mat[5][2]

    elif type_r == "R":
        new_mat[0][3] = mat[2][3]
        new_mat[1][3] = mat[3][3]
        new_mat[2][3] = mat[4][3]
        new_mat[2][4] = mat[3][4]
        new_mat[2][5] = mat[2][4]
        new_mat[3][3] = mat[5][3]
        new_mat[3][4] = mat[3][5]
        new_mat[3][5] = mat[2][5]
        new_mat[4][3] = mat[6][3]
        new_mat[5][3] = mat[7][3]
        new_mat[6][3] = mat[0][3]
        new_mat[7][3] = mat[1][3]

    elif type_r == "R'":
        new_mat[0][3] = mat[6][3]
        new_mat[1][3] = mat[7][3]
        new_mat[2][3] = mat[0][3]
        new_mat[2][4] = mat[2][5]
        new_mat[2][5] = mat[3][5]
        new_mat[3][3] = mat[1][3]
        new_mat[3][4] = mat[2][4]
        new_mat[3][5] = mat[3][4]
        new_mat[4][3] = mat[2][3]
        new_mat[5][3] = mat[3][3]
        new_mat[6][3] = mat[4][3]
        new_mat[7][3] = mat[5][3]

    elif type_r == "U":
        new_mat[1][2] = mat[3][1]
        new_mat[1][3] = mat[2][1]
        new_mat[2][1] = mat[4][2]
        new_mat[2][2] = mat[3][2]
        new_mat[2][3] = mat[2][2]
        new_mat[2][4] = mat[1][2]
        new_mat[3][1] = mat[4][3]
        new_mat[3][2] = mat[3][3]
        new_mat[3][3] = mat[2][3]
        new_mat[3][4] = mat[1][3]
        new_mat[4][2] = mat[3][4]
        new_mat[4][3] = mat[2][4]

    elif type_r == "F'":
        new_mat[3][0] = mat[3][2]
        new_mat[3][1] = mat[3][3]
        new_mat[3][2] = mat[3][4]
        new_mat[3][3] = mat[3][5]
        new_mat[3][4] = mat[6][3]
        new_mat[3][5] = mat[6][2]
        new_mat[4][2] = mat[4][3]
        new_mat[4][3] = mat[5][3]
        new_mat[5][2] = mat[4][2]
        new_mat[5][3] = mat[5][2]
        new_mat[6][2] = mat[3][1]
        new_mat[6][3] = mat[3][0]

    elif type_r == "B'":
        new_mat[0][2] = mat[0][3]
        new_mat[0][3] = mat[1][3]
        new_mat[1][2] = mat[0][2]
        new_mat[1][3] = mat[1][2]
        new_mat[2][0] = mat[7][3]
        new_mat[2][1] = mat[7][2]
        new_mat[2][2] = mat[2][0]
        new_mat[2][3] = mat[2][1]
        new_mat[2][4] = mat[2][2]
        new_mat[2][5] = mat[2][3]
        new_mat[7][2] = mat[2][5]
        new_mat[7][3] = mat[2][4]

    elif type_r == "U'":
        new_mat[1][2] = mat[2][4]
        new_mat[1][3] = mat[3][4]
        new_mat[2][1] = mat[1][3]
        new_mat[2][2] = mat[2][3]
        new_mat[2][3] = mat[3][3]
        new_mat[2][4] = mat[4][3]
        new_mat[3][1] = mat[1][2]
        new_mat[3][2] = mat[2][2]
        new_mat[3][3] = mat[3][2]
        new_mat[3][4] = mat[4][2]
        new_mat[4][2] = mat[2][1]
        new_mat[4][3] = mat[3][1]

    elif type_r == "B":
        new_mat[0][2] = mat[1][2]
        new_mat[0][3] = mat[0][2]
        new_mat[1][2] = mat[1][3]
        new_mat[1][3] = mat[0][3]
        new_mat[2][0] = mat[2][2]
        new_mat[2][1] = mat[2][3]
        new_mat[2][2] = mat[2][4]
        new_mat[2][3] = mat[2][5]
        new_mat[2][4] = mat[7][3]
        new_mat[2][5] = mat[7][2]
        new_mat[7][2] = mat[2][1]
        new_mat[7][3] = mat[2][0]

    elif type_r == "L'":
        new_mat[0][2] = mat[2][2]
        new_mat[1][2] = mat[3][2]
        new_mat[2][0] = mat[2][1]
        new_mat[2][1] = mat[3][1]
        new_mat[2][2] = mat[4][2]
        new_mat[3][0] = mat[2][0]
        new_mat[3][1] = mat[3][0]
        new_mat[3][2] = mat[5][2]
        new_mat[4][2] = mat[6][2]
        new_mat[5][2] = mat[7][2]
        new_mat[6][2] = mat[0][2]
        new_mat[7][2] = mat[1][2]

    elif type_r == "D":
        new_mat[0][2] = mat[2][5]
        new_mat[0][3] = mat[3][5]
        new_mat[2][0] = mat[0][3]
        new_mat[2][5] = mat[5][3]
        new_mat[3][0] = mat[0][2]
        new_mat[3][5] = mat[5][2]
        new_mat[5][2] = mat[2][0]
        new_mat[5][3] = mat[3][0]
        new_mat[6][2] = mat[7][2]
        new_mat[6][3] = mat[6][2]
        new_mat[7][2] = mat[7][3]
        new_mat[7][3] = mat[6][3]

    elif type_r == "D'":
        new_mat[0][2] = mat[3][0]
        new_mat[0][3] = mat[2][0]
        new_mat[2][0] = mat[5][2]
        new_mat[2][5] = mat[0][2]
        new_mat[3][0] = mat[5][3]
        new_mat[3][5] = mat[0][3]
        new_mat[5][2] = mat[3][5]
        new_mat[5][3] = mat[2][5]
        new_mat[6][2] = mat[6][3]
        new_mat[6][3] = mat[7][3]
        new_mat[7][2] = mat[6][2]
        new_mat[7][3] = mat[7][2]


def use_formula(mat, new_mat, type_f):

    if type_f == "U R U' R' F R' F' R":
        new_mat[1][2] = mat[1][3]
        new_mat[1][3] = mat[3][2]
        new_mat[2][1] = mat[2][3]
        new_mat[2][2] = mat[2][4]
        new_mat[2][3] = mat[3][1]
        new_mat[2][4] = mat[4][2]
        new_mat[3][1] = mat[2][1]
        new_mat[3][2] = mat[1][2]
        new_mat[4][2] = mat[2][2]
    
    elif type_f == "U' D":
        new_mat[0][2] = mat[2][5]
        new_mat[0][3] = mat[3][5]
        new_mat[1][2] = mat[2][4]
        new_mat[1][3] = mat[3][4]
        new_mat[2][0] = mat[0][3]
        new_mat[2][1] = mat[1][3]
        new_mat[2][2] = mat[2][3]
        new_mat[2][3] = mat[3][3]
        new_mat[2][4] = mat[4][3]
        new_mat[2][5] = mat[5][3]
        new_mat[3][0] = mat[0][2]
        new_mat[3][1] = mat[1][2]
        new_mat[3][2] = mat[2][2]
        new_mat[3][3] = mat[3][2]
        new_mat[3][4] = mat[4][2]
        new_mat[3][5] = mat[5][2]
        new_mat[4][2] = mat[2][1]
        new_mat[4][3] = mat[3][1]
        new_mat[5][2] = mat[2][0]
        new_mat[5][3] = mat[3][0]
        new_mat[6][2] = mat[7][2]
        new_mat[6][3] = mat[6][2]
        new_mat[7][2] = mat[7][3]
        new_mat[7][3] = mat[6][3]

    elif type_f == "R U R' U' R U R' U' R U R' U' R U R' U' D":
        new_mat[0][2] = mat[2][5]
        new_mat[0][3] = mat[6][3]
        new_mat[1][2] = mat[2][1]
        new_mat[1][3] = mat[2][3]
        new_mat[2][0] = mat[0][3]
        new_mat[2][1] = mat[2][2]
        new_mat[2][2] = mat[1][2]
        new_mat[2][3] = mat[2][4]
        new_mat[2][4] = mat[1][3]
        new_mat[2][5] = mat[3][5]
        new_mat[3][0] = mat[0][2]
        new_mat[3][3] = mat[3][4]
        new_mat[3][4] = mat[4][3]
        new_mat[3][5] = mat[5][2]
        new_mat[4][3] = mat[3][3]
        new_mat[5][2] = mat[2][0]
        new_mat[5][3] = mat[3][0]
        new_mat[6][2] = mat[7][2]
        new_mat[6][3] = mat[6][2]
        new_mat[7][2] = mat[7][3]
        new_mat[7][3] = mat[5][3]

    elif type_f == "R U R' U' R U R' U' D":
        new_mat[0][2] = mat[2][5]
        new_mat[0][3] = mat[5][3]
        new_mat[1][2] = mat[2][2]
        new_mat[1][3] = mat[2][4]
        new_mat[2][0] = mat[0][3]
        new_mat[2][1] = mat[1][2]
        new_mat[2][2] = mat[2][1]
        new_mat[2][3] = mat[1][3]
        new_mat[2][4] = mat[2][3]
        new_mat[2][5] = mat[6][3]
        new_mat[3][0] = mat[0][2]
        new_mat[3][3] = mat[4][3]
        new_mat[3][4] = mat[3][3]
        new_mat[3][5] = mat[5][2]
        new_mat[4][3] = mat[3][4]
        new_mat[5][2] = mat[2][0]
        new_mat[5][3] = mat[3][0]
        new_mat[6][2] = mat[7][2]
        new_mat[6][3] = mat[6][2]
        new_mat[7][2] = mat[7][3]
        new_mat[7][3] = mat[3][5]
    
    elif type_f == "U D'":
        new_mat[0][2] = mat[3][0]
        new_mat[0][3] = mat[2][0]
        new_mat[1][2] = mat[3][1]
        new_mat[1][3] = mat[2][1]
        new_mat[2][0] = mat[5][2]
        new_mat[2][1] = mat[4][2]
        new_mat[2][2] = mat[3][2]
        new_mat[2][3] = mat[2][2]
        new_mat[2][4] = mat[1][2]
        new_mat[2][5] = mat[0][2]
        new_mat[3][0] = mat[5][3]
        new_mat[3][1] = mat[4][3]
        new_mat[3][2] = mat[3][3]
        new_mat[3][3] = mat[2][3]
        new_mat[3][4] = mat[1][3]
        new_mat[3][5] = mat[0][3]
        new_mat[4][2] = mat[3][4]
        new_mat[4][3] = mat[2][4]
        new_mat[5][2] = mat[3][5]
        new_mat[5][3] = mat[2][5]
        new_mat[6][2] = mat[6][3]
        new_mat[6][3] = mat[7][3]
        new_mat[7][2] = mat[6][2]
        new_mat[7][3] = mat[7][2]

    elif type_f == "R U R' U' D":
        new_mat[0][2] = mat[2][5]
        new_mat[0][3] = mat[3][3]
        new_mat[1][2] = mat[2][4]
        new_mat[1][3] = mat[1][2]
        new_mat[2][0] = mat[0][3]
        new_mat[2][1] = mat[1][3]
        new_mat[2][2] = mat[2][3]
        new_mat[2][3] = mat[2][1]
        new_mat[2][4] = mat[2][2]
        new_mat[2][5] = mat[4][3]
        new_mat[3][0] = mat[0][2]
        new_mat[3][3] = mat[5][3]
        new_mat[3][4] = mat[3][5]
        new_mat[3][5] = mat[5][2]
        new_mat[4][3] = mat[6][3]
        new_mat[5][2] = mat[2][0]
        new_mat[5][3] = mat[3][0]
        new_mat[6][2] = mat[7][2]
        new_mat[6][3] = mat[6][2]
        new_mat[7][2] = mat[7][3]
        new_mat[7][3] = mat[3][4]

    elif type_f == "R U R' U' R U R' U' R U R' U' D":
        new_mat[0][2] = mat[2][5]
        new_mat[0][3] = mat[4][3]
        new_mat[1][2] = mat[2][3]
        new_mat[1][3] = mat[2][2]
        new_mat[2][0] = mat[0][3]
        new_mat[2][1] = mat[2][4]
        new_mat[2][2] = mat[1][3]
        new_mat[2][3] = mat[1][2]
        new_mat[2][4] = mat[2][1]
        new_mat[2][5] = mat[3][4]
        new_mat[3][0] = mat[0][2]
        new_mat[3][3] = mat[6][3]
        new_mat[3][4] = mat[5][3]
        new_mat[3][5] = mat[5][2]
        new_mat[4][3] = mat[3][5]
        new_mat[5][2] = mat[2][0]
        new_mat[5][3] = mat[3][0]
        new_mat[6][2] = mat[7][2]
        new_mat[6][3] = mat[6][2]
        new_mat[7][2] = mat[7][3]
        new_mat[7][3] = mat[3][3]


# Функция, поворачивающая грани кубика, для первого этапа программы
def stage1_rotations(mat, x):

    new_mat = deepcopy(mat)

    if x == '0':  # F
        use_simple_rotation(mat, new_mat, "F")
    elif x == '1':  # L
        use_simple_rotation(mat, new_mat, "L")
    elif x == '2':  # R
        use_simple_rotation(mat, new_mat, "R")
    elif x == '3':  # R'
        use_simple_rotation(mat, new_mat, "R'")
    elif x == '4':  # U
        use_simple_rotation(mat, new_mat, "U")
    elif x == '5':  # F'
        use_simple_rotation(mat, new_mat, "F'")
    elif x == '6':  # B'
        use_simple_rotation(mat, new_mat, "B'")
    elif x == '7':  # U'
        use_simple_rotation(mat, new_mat, "U'")
    elif x == '8':  # B
        use_simple_rotation(mat, new_mat, "B")
    elif x == '9':  # L'
        use_simple_rotation(mat, new_mat, "L'")
    if x == '10':  # D
        use_simple_rotation(mat, new_mat, "D")
    elif x == '11':  # D'
        use_simple_rotation(mat, new_mat, "D'")
    
    return new_mat


# Функция, поворачивающая грани кубика, для второго этапа программы
def stage2_rotations(mat, x):

    new_mat = deepcopy(mat)

    if x == '0':  # Формула (U R U' R' F R' F' R)
        use_formula(mat, new_mat, "U R U' R' F R' F' R")
    elif x == '1':  # U'
        use_simple_rotation(mat, new_mat, "U'")
    elif x == '2':  # D
        use_simple_rotation(mat, new_mat, "D")
    elif x == '3':  # U
        use_simple_rotation(mat, new_mat, "U")
    elif x == '4':  # D'
        use_simple_rotation(mat, new_mat, "D'")
    
    return new_mat


# Функция, поворачивающая грани кубика, для третьего этапа программы
def stage3_rotations(mat, x):

    new_mat = deepcopy(mat)

    if x == '0':  # Формула (U' D)
        use_formula(mat, new_mat, "U' D")
    elif x == '1':  # Формула (R U R' U' R U R' U' R U R' U' R U R' U' D)
        use_formula(mat, new_mat, "R U R' U' R U R' U' R U R' U' R U R' U' D")
    elif x == '2':  # Формула (R U R' U' R U R' U' D)
        use_formula(mat, new_mat, "R U R' U' R U R' U' D")
    elif x == '3':  # D
        use_simple_rotation(mat, new_mat, "D")
    elif x == '4':  # Формула (U D')
        use_formula(mat, new_mat, "U D'")
    elif x == '5':  # Формула (R U R' U' D)
        use_formula(mat, new_mat, "R U R' U' D")
    elif x == '6':  # Формула (R U R' U' R U R' U' R U R' U' D)
        use_formula(mat, new_mat, "R U R' U' R U R' U' R U R' U' D")
    
    return new_mat
