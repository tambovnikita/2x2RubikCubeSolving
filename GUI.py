import tkinter as tk

from slots import *


class GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('2x2 Rubik’s Cube Solving')
        self.root.geometry('1280x720+50+50')
        self.root.configure(background='#ccedf9')

        """
        1 - БЕЛЫЙ - #FFFFFF
        2 - СИНИЙ - #0000FF
        3 - ЗЕЛЁНЫЙ - #008000
        4 - ОРАНЖЕВЫЙ - #FFA500
        5 - КРАСНЫЙ - #FF0000
        6 - ЖЁЛТЫЙ - #FFFF00
        """

        self.cube_colors = {
            1: '#FFFFFF',
            2: '#0000FF',
            3: '#008000',
            4: '#FFA500',
            5: '#FF0000',
            6: '#FFFF00'
        }

        self.font_btn = ("Roboto", 16)
        self.font_description = ("Roboto", 12)
        self.font_description_bold = ("Roboto", 12, "bold")
        self.cube_frame_padx = 6
        self.cube_frame_pady = 6

        self.cube_container = tk.Frame(self.root, bg="#ccedf9")
        self.cube_frames = []
        self.create_cube_frames()
        self.create_description_widgets()
        self.set_info_text()
        self.create_btns()
    

    def create_cube_frames(self):
        # red cube frames
        for i in range(1, 5):
            frame = tk.Frame(self.cube_container, bg=self.cube_colors[5], bd=3, relief=tk.RIDGE, width=50, height=50)
            frame.id = i
            frame.current_color_id = 5
            frame.bind("<Button-1>", self.change_color)
            self.cube_frames.append(frame)

        self.cube_frames[0].grid(row=0, column=2, padx=self.cube_frame_padx, pady=self.cube_frame_pady)
        self.cube_frames[1].grid(row=0, column=3, padx=self.cube_frame_padx, pady=self.cube_frame_pady)
        self.cube_frames[2].grid(row=1, column=2, padx=self.cube_frame_padx, pady=self.cube_frame_pady)
        self.cube_frames[3].grid(row=1, column=3, padx=self.cube_frame_padx, pady=self.cube_frame_pady)

        # blue cube frames
        for i in range(5, 9):
            frame = tk.Frame(self.cube_container, bg=self.cube_colors[2], bd=3, relief=tk.RIDGE, width=50, height=50)
            frame.id = i
            frame.current_color_id = 2
            frame.bind("<Button-1>", self.change_color)
            self.cube_frames.append(frame)

        self.cube_frames[4].grid(row=2, column=0, padx=self.cube_frame_padx, pady=self.cube_frame_pady)
        self.cube_frames[5].grid(row=2, column=1, padx=self.cube_frame_padx, pady=self.cube_frame_pady)
        self.cube_frames[6].grid(row=3, column=0, padx=self.cube_frame_padx, pady=self.cube_frame_pady)
        self.cube_frames[7].grid(row=3, column=1, padx=self.cube_frame_padx, pady=self.cube_frame_pady)

        # white cube frames
        for i in range(9, 13):
            frame = tk.Frame(self.cube_container, bg=self.cube_colors[1], bd=3, relief=tk.RIDGE, width=50, height=50)
            frame.id = i
            frame.current_color_id = 1
            frame.bind("<Button-1>", self.change_color)
            self.cube_frames.append(frame)

        self.cube_frames[8].grid(row=2, column=2, padx=self.cube_frame_padx, pady=self.cube_frame_pady)
        self.cube_frames[9].grid(row=2, column=3, padx=self.cube_frame_padx, pady=self.cube_frame_pady)
        self.cube_frames[10].grid(row=3, column=2, padx=self.cube_frame_padx, pady=self.cube_frame_pady)
        self.cube_frames[11].grid(row=3, column=3, padx=self.cube_frame_padx, pady=self.cube_frame_pady)

        # green cube frames
        for i in range(13, 17):
            frame = tk.Frame(self.cube_container, bg=self.cube_colors[3], bd=3, relief=tk.RIDGE, width=50, height=50)
            frame.id = i
            frame.current_color_id = 3
            frame.bind("<Button-1>", self.change_color)
            self.cube_frames.append(frame)

        self.cube_frames[12].grid(row=2, column=4, padx=self.cube_frame_padx, pady=self.cube_frame_pady)
        self.cube_frames[13].grid(row=2, column=5, padx=self.cube_frame_padx, pady=self.cube_frame_pady)
        self.cube_frames[14].grid(row=3, column=4, padx=self.cube_frame_padx, pady=self.cube_frame_pady)
        self.cube_frames[15].grid(row=3, column=5, padx=self.cube_frame_padx, pady=self.cube_frame_pady)

        # orange cube frames
        for i in range(17, 21):
            frame = tk.Frame(self.cube_container, bg=self.cube_colors[4], bd=3, relief=tk.RIDGE, width=50, height=50)
            frame.id = i
            frame.current_color_id = 4
            frame.bind("<Button-1>", self.change_color)
            self.cube_frames.append(frame)

        self.cube_frames[16].grid(row=4, column=2, padx=self.cube_frame_padx, pady=self.cube_frame_pady)
        self.cube_frames[17].grid(row=4, column=3, padx=self.cube_frame_padx, pady=self.cube_frame_pady)
        self.cube_frames[18].grid(row=5, column=2, padx=self.cube_frame_padx, pady=self.cube_frame_pady)
        self.cube_frames[19].grid(row=5, column=3, padx=self.cube_frame_padx, pady=self.cube_frame_pady)

        # yellow cube frames
        for i in range(21, 25):
            frame = tk.Frame(self.cube_container, bg=self.cube_colors[6], bd=3, relief=tk.RIDGE, width=50, height=50)
            frame.id = i
            frame.current_color_id = 6
            frame.bind("<Button-1>", self.change_color)
            self.cube_frames.append(frame)

        self.cube_frames[20].grid(row=6, column=2, padx=self.cube_frame_padx, pady=self.cube_frame_pady)
        self.cube_frames[21].grid(row=6, column=3, padx=self.cube_frame_padx, pady=self.cube_frame_pady)
        self.cube_frames[22].grid(row=7, column=2, padx=self.cube_frame_padx, pady=self.cube_frame_pady)
        self.cube_frames[23].grid(row=7, column=3, padx=self.cube_frame_padx, pady=self.cube_frame_pady)

        self.cube_container.place(relx=0.05, rely=0.1)
    

    def create_description_widgets(self):
        self.description_text = tk.Text(self.root, height=18, width=40, padx=15, pady=12, wrap=tk.WORD, font=self.font_description, foreground='#000000', background='#edf5ff', highlightthickness=0, relief=tk.GROOVE, bd=3)
        self.description_text.tag_configure("bold", font=self.font_description_bold)
        self.description_text.grid(row=0, column=0, sticky="nsew")  # Растягиваем на весь Frame
        self.description_text.place(relx=0.4, rely=0.16)

        self.stages = tk.Frame(self.root, bg="#ccedf9")
        self.stage1_lbl = tk.Label(
            self.stages,
            wraplength=300,
            padx=15, pady=12,
            font=self.font_description,
            foreground='#000000', background='#edf5ff',
            justify=tk.LEFT, relief=tk.GROOVE, bd=3
        )
        self.stage1_lbl.pack(pady=(0, 10), anchor="w")
        self.stage2_lbl = tk.Label(
            self.stages,
            wraplength=300,
            padx=15, pady=12,
            font=self.font_description,
            foreground='#000000', background='#edf5ff',
            justify=tk.LEFT, relief=tk.GROOVE, bd=3
        )
        self.stage2_lbl.pack(pady=(0, 10), anchor="w")
        self.stage3_lbl = tk.Label(
            self.stages,
            wraplength=300,
            padx=15, pady=12,
            font=self.font_description,
            foreground='#000000', background='#edf5ff',
            justify=tk.LEFT, relief=tk.GROOVE, bd=3
        )
        self.stage3_lbl.pack(anchor="w")

        self.stages.place(relx=0.7, rely=0.16)

        self.instant_solution_lbl = tk.Label(
            self.root,
            wraplength=300,
            padx=15, pady=12,
            font=self.font_description,
            foreground='#000000', background='#fffce5',
            justify=tk.LEFT, relief=tk.GROOVE, bd=4
        )
        self.instant_solution_lbl.place(relx=0.4, rely=0.62)


    def create_btns(self):
        # Кнопка "Собрать"
        self.solve_btn = tk.Label(self.root, text='Собрать', padx=16, pady=5, font=self.font_btn)
        self.solve_btn.bind("<Button-1>", self.handle_solve_btn)
        self.solve_btn.place(relx=0.4, rely=0.05)

        # Кнопка "Сброс"
        self.reset_btn = tk.Label(self.root, text='Сброс', padx=16, pady=5, font=self.font_btn)
        self.reset_btn.bind("<Button-1>", self.handle_reset_btn)
        self.reset_btn.place(relx=0.49, rely=0.05)

        # Кнопка "Пример"
        self.example_btn = tk.Label(self.root, text='Пример', padx=16, pady=5, font=self.font_btn)
        self.example_btn.bind("<Button-1>", self.handle_example_btn)
        self.example_btn.place(relx=0.7, rely=0.05)

        # Кнопка "Анимация поворотов"
        self.animation_rotations_btn = tk.Label(self.root, text='Анимация поворотов', padx=16, pady=5, font=self.font_btn)
        self.animation_rotations_btn.bind("<Button-1>", self.handle_animation_rotations_btn)
        self.animation_rotations_btn.place(relx=0.79, rely=0.05)


    def change_color(self, event):
        frame = self.cube_frames[event.widget.id-1]
        frame.current_color_id += 1
        if frame.current_color_id > 6:
            frame.current_color_id = 1
        frame.config(background=self.cube_colors[frame.current_color_id])


    def set_info_text(self):
        text = (
            '\n\nДобро пожаловать в программу, которая создана для удобной и быстрой сборки Кубика Рубика 2x2.\n\n'
            'В блоках справа описаны основные шаги, которых будет достаточно, чтобы получить желаемый результат.\n\n'
            'После нажатия на кнопку "Пример" вы увидите кубик в разобранном состоянии. Если после этого нажмёте на "Собрать", то увидите этапы его сборки.\n\n'
            'Разработчик: Тамбов Никита\n'
            'Почта: tambovnikita@yandex.ru\n\n'
            '2025 г.'
        )
        self.description_text.config(state=tk.NORMAL)
        self.description_text.delete("1.0", tk.END)
        self.description_text.insert(tk.END, "ИНСТРУКЦИЯ", "bold")
        self.description_text.insert(tk.END, text)
        self.description_text.config(state=tk.DISABLED)  # Запрет редактирования
        self.stage1_lbl.config(text="Нажмите на нужные цветные квадраты, чтобы получилась расстановка как на вашем разобранном кубике.")
        self.stage2_lbl.config(text="В центре находится грань кубика, которая смотрит вверх (F). В собранном положении это грань белого цвета.\nПод этой гранью находится грань, которая смотрит на вас (F).")
        self.stage3_lbl.config(text='После того, как макет в левой части окна будет совпадать с гранями на кубике, нажмите на кнопку "Собрать" и ожидайте завершения работы алгоритма.')
        self.instant_solution_lbl.config(text='Здесь появится "Мгновенное решение" после клика по кнопке "Собрать"...')


    def set_solve_text(self):
        text = (
            '\n\nU - поворот верхней грани по часовой стрелке\n'
            'U\' - поворот верхней грани против часовой стрелки\n'
            'D - поворот нижней грани по часовой стрелке\n'
            'D\' - поворот нижней грани против часовой стрелки\n'
            'F - поворот передней грани по часовой стрелке\n'
            'F\' - поворот передней грани против часовой стрелки\n'
            'B - поворот задней грани по часовой стрелке\n'
            'B\' - поворот задней грани против часовой стрелки\n'
            'R - поворот правой грани по часовой стрелке\n'
            'R\' - поворот правой грани против часовой стрелки\n'
            'L - поворот левой грани по часовой стрелке\n'
            'L\' - поворот левой грани против часовой стрелки\n\n'
            'R U R\' U\' - формула ПИФ-ПАФ\n\n'
            'U R U\' R\' F R\' F\' R\' - формула'
        )
        self.description_text.config(state=tk.NORMAL)
        self.description_text.delete("1.0", "end")
        self.description_text.insert(tk.END, "ОБОЗНАЧЕНИЯ", "bold")
        self.description_text.insert(tk.END, text)
        self.description_text.config(state=tk.DISABLED)  # Запрет редактирования
        self.stage1_lbl.config(text="1 ЭТАП\n\nПоиск комбинаций...")
        self.stage2_lbl.config(text="2 ЭТАП\n\nПоиск комбинаций...")
        self.stage3_lbl.config(text="3 ЭТАП\n\nПоиск комбинаций...")


GUI.handle_solve_btn = handle_solve_btn
GUI.handle_reset_btn = handle_reset_btn
GUI.handle_example_btn = handle_example_btn
GUI.handle_animation_rotations_btn = handle_animation_rotations_btn
