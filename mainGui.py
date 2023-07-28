import tkinter as tk
from graphGui import GraphGUI
import subprocess

class mainGUI:
    def __init__(self, master):
        self.master = master
        master.title("Graph")
        master.configure(bg="#D6CACA")

        # Add a frame for the title
        title_frame = tk.Frame(master, bg="#D6CACA")
        title_frame.grid(row=0, column=0, columnspan=3)

        # Create a label for the title
        self.title_label = tk.Label(title_frame, text="The Problem Solving Toolbox", font=(
            "Belleza Regular", 20, "bold"), padx=50, bg="#D6CACA")
        self.title_label.pack(pady=10)

        main_frame = tk.Frame(master, bg="#D6CACA")
        main_frame.grid(row=1, column=0, rowspan=13, sticky="nsew")
        main_frame.grid_columnconfigure(0, weight=1)

        self.graph_button = tk.Button(
            main_frame, text="Graph Search", font=("Arial", 12), bg="#474747", fg="white",
            command=self.open_graph_gui  # Assign a command to the button
        )
        self.graph_button.grid(row=2, column=2, columnspan=3,
                               sticky="nsew", padx=20, pady=10)

        self.game_button = tk.Button(
            main_frame, text="Checkers Game", font=("Arial", 12), bg="#474747", fg="white",
            command=self.run_chess_game
        )
        self.game_button.grid(row=3, column=2, columnspan=3, sticky="nsew", padx=20, pady=10)

    def open_graph_gui(self):
        # Create the new window for the Graph GUI
        graph_gui_window = tk.Toplevel(self.master)
        graph_gui = GraphGUI(graph_gui_window)

    def run_chess_game(self):
        subprocess.call(['python', 'mainGame.py'])