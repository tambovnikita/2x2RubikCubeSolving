from copy import deepcopy
import sqlite3
import json

from rotations import use_simple_rotation
from build_settings import resource_path


class InstantSolutionRegistry:
    def __init__(self, db_name="instant_solution.db"):
        self.conn = sqlite3.connect(resource_path(db_name))
        self._init_db()

    def _init_db(self):
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS matrices (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                sequence_num INTEGER NOT NULL UNIQUE,
                sequence TEXT NOT NULL UNIQUE,
                matrix_json TEXT NOT NULL UNIQUE
            )
        """)
        self.conn.commit()

    def add_matrix(self, sequence_num, sequence, matrix):
        sequence_json = json.dumps(sequence)
        matrix_json = json.dumps(matrix)
        cursor = self.conn.cursor()
        
        # Проверяем существование матрицы
        cursor.execute("SELECT id FROM matrices WHERE matrix_json = ?", (matrix_json,))
        existing = cursor.fetchone()
        if existing:
            return "-"
        
        # Добавляем новую матрицу
        cursor.execute("INSERT INTO matrices (sequence_num, sequence, matrix_json) VALUES (?, ?, ?)", (sequence_num, sequence_json, matrix_json))
        self.conn.commit()
        return cursor.lastrowid

    def get_sequence(self, matrix):
        matrix_json = json.dumps(matrix)
        cursor = self.conn.cursor()
        cursor.execute("SELECT sequence FROM matrices WHERE matrix_json = ?", (matrix_json,))
        result = cursor.fetchone()
        return result[0][2:-2].split('", "') if result else None
    
    def get_matrix(self, matrix_id):
        cursor = self.conn.cursor()
        cursor.execute("SELECT matrix_json FROM matrices WHERE id = ?", (matrix_id,))
        result = cursor.fetchone()
        print(result)
        print(type(result))
        return json.loads(result[0]) if result else None
    
    def close(self):
        self.conn.close()


def get_sequence(value):
    chars = ["0", "1", "2", "3", "4", "5"]
    designations = ["L", "R", "U", "D", "F", "B"]
    res_c = []
    res_d = []
    while value > 0:
        res_c.append(chars[value % 6])
        res_d.append(designations[value % 6])
        value //= 6
    return res_c[::-1] if res_c else ["0"], res_d[::-1] if res_d else ["L"]


def get_new_position(mat, sequence):
    new_mat = deepcopy(mat)
    # поворот граней
    for s in sequence:
        m = deepcopy(new_mat)
        use_simple_rotation(m, new_mat, s)
    return new_mat


def generating_solutions():
    mat = [
        [0, 0, 5, 5, 0, 0],
        [0, 0, 5, 5, 0, 0],
        [2, 2, 1, 1, 3, 3],
        [2, 2, 1, 1, 3, 3],
        [0, 0, 4, 4, 0, 0],
        [0, 0, 4, 4, 0, 0],
        [0, 0, 6, 6, 0, 0],
        [0, 0, 6, 6, 0, 0]
    ]

    try:
        registry = InstantSolutionRegistry()
        for i in range(700_000_000, 1_200_000_000):
            sequence, sequence_formatted = get_sequence(i)
            new_mat = deepcopy(mat)
            new_mat = get_new_position(new_mat, sequence_formatted)
            matrix_id = registry.add_matrix(sequence_num=i, sequence=sequence_formatted, matrix=new_mat)
            print(f"{i}) {sequence}\n{new_mat}")
            print(f"ID матрицы: {matrix_id}\n")
    finally:
        registry.close()


# generating_solutions()
