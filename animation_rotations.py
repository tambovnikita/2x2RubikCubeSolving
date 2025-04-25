import tkinter as tk
import cv2
from PIL import Image, ImageTk

from build_settings import resource_path


class VideoPlayer:
    def __init__(self, parent, video_path, name, bg_color):
        self.parent = parent
        self.video_path = video_path
        self.name = name
        self.bg_color = bg_color
        self.cap = cv2.VideoCapture(video_path)
        self.fps = max(self.cap.get(cv2.CAP_PROP_FPS), 1)  # Защита от нулевого FPS
        self.frame_delay = int(1000 / self.fps)
        self.is_playing = False
        self.video_loop = None
        
        self.create_widgets()
        self.start_playback()
    
    def create_widgets(self):
        self.label = tk.Label(self.parent, bg=self.bg_color)
        self.label.pack()
        tk.Label(self.parent, text=self.name, bg=self.bg_color, foreground='black', font=("Roboto", 14)).pack()

    def update_frame(self):
        if self.is_playing:
            ret, frame = self.cap.read()
            if ret:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                img = ImageTk.PhotoImage(Image.fromarray(frame))
                self.label.config(image=img)
                self.label.image = img
                self.video_loop = self.label.after(self.frame_delay, self.update_frame)
            else:
                self.restart_video()

    def restart_video(self):
        self.cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        if self.is_playing:
            self.video_loop = self.label.after(self.frame_delay, self.update_frame)

    def start_playback(self):
        if not self.is_playing:
            self.is_playing = True
            self.update_frame()

    def stop_playback(self):
        if self.is_playing:
            self.is_playing = False
            if self.video_loop:
                self.label.after_cancel(self.video_loop)
            self.cap.release()


class AnimationWindow:
    def __init__(self, parent, title):
        self.window = tk.Toplevel(parent)
        self.window.geometry("+80+80")
        self.window.title(title)
        self.bg_color = "white"
        self.window.configure(background=self.bg_color)
        self.players = []
        
        rotations = ["U", "U'", "D", "D'", "R", "R'", "L", "L'", "F", "F'", "B", "B'"]
        for row in range(3):
            for col in range(4):
                frame = tk.Frame(self.window, padx=15, pady=15, bg=self.bg_color)
                frame.grid(row=row, column=col)
                name = rotations[row * 4 + col]
                player = VideoPlayer(frame, resource_path(f"animations/{name}.mov"), name, self.bg_color)
                self.players.append(player)
        
        self.window.protocol("WM_DELETE_WINDOW", self.on_close)

    def on_close(self):
        for player in self.players:
            player.stop_playback()
        self.window.destroy()
