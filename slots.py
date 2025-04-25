import tkinter as tk

from instant_solution import InstantSolutionRegistry
from stages import stage1, stage2, stage3
from animation_rotations import AnimationWindow


def handle_solve_btn(self, event):
    self.solve_btn.config(state=tk.DISABLED)

    # заполнение матрицы номерами цветов разобранного кубика
    mat = [
        [0, 0, self.cube_frames[0].current_color_id, self.cube_frames[1].current_color_id, 0, 0],
        [0, 0, self.cube_frames[2].current_color_id, self.cube_frames[3].current_color_id, 0, 0],
        [self.cube_frames[4].current_color_id, self.cube_frames[5].current_color_id, self.cube_frames[8].current_color_id, self.cube_frames[9].current_color_id, self.cube_frames[12].current_color_id, self.cube_frames[13].current_color_id],
        [self.cube_frames[6].current_color_id, self.cube_frames[7].current_color_id, self.cube_frames[10].current_color_id, self.cube_frames[11].current_color_id, self.cube_frames[14].current_color_id, self.cube_frames[15].current_color_id],
        [0, 0, self.cube_frames[16].current_color_id, self.cube_frames[17].current_color_id, 0, 0],
        [0, 0, self.cube_frames[18].current_color_id, self.cube_frames[19].current_color_id, 0, 0],
        [0, 0, self.cube_frames[20].current_color_id, self.cube_frames[21].current_color_id, 0, 0],
        [0, 0, self.cube_frames[22].current_color_id, self.cube_frames[23].current_color_id, 0, 0]
    ]
    self.set_solve_text()
    self.root.update()

    # Мгновенное решение
    instant_solution_registry = InstantSolutionRegistry()
    sequence = instant_solution_registry.get_sequence(mat)
    if sequence is None:
        self.instant_solution_lbl.config(text="МГНОВЕННОЕ РЕШЕНИЕ\n\nК сожалению, на данный момент, решения нет в базе данных.\n\nПроверка макета на ошибки невозможна.")
    else:
        text = "МГНОВЕННОЕ РЕШЕНИЕ\n\n"
        if len(sequence) == 1 and sequence[0] == "":
            text += "Кубик уже собран."
        else:
            text += "Макет построен без ошибок.\n\n"
            for s in sequence[::-1]:
                if "'" in s:
                    text += f"{s[:-1]} "
                else:
                    text += f"{s}' "
        self.instant_solution_lbl.config(text=text)
    
    text, mat = stage1(mat)
    self.stage1_lbl.config(text=text)
    self.root.update()
    text, mat = stage2(mat)
    self.stage2_lbl.config(text=text)
    self.root.update()
    text = stage3(mat)
    self.stage3_lbl.config(text=text)

    self.solve_btn.config(state=tk.NORMAL)


def handle_reset_btn(self, event):
    self.set_info_text()
    example_color_id_list = [5, 5, 5, 5, 2, 2, 2, 2, 1, 1, 1, 1, 3, 3, 3, 3, 4, 4, 4, 4, 6, 6, 6, 6]
    for i in range(len(self.cube_frames)):
        self.cube_frames[i].current_color_id = example_color_id_list[i]
        self.cube_frames[i].config(background=self.cube_colors[example_color_id_list[i]])


def handle_example_btn(self, event):
    self.set_info_text()
    example_color_id_list = [6, 4, 5, 4, 2, 6, 1, 1, 2, 3, 2, 3, 1, 1, 5, 6, 5, 6, 5, 3, 3, 4, 4, 2]
    for i in range(len(self.cube_frames)):
        self.cube_frames[i].current_color_id = example_color_id_list[i]
        self.cube_frames[i].config(background=self.cube_colors[example_color_id_list[i]])


def handle_animation_rotations_btn(self, event):
    AnimationWindow(self.root, "Анимация поворотов")
