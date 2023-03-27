import csv
import tkinter as tk
from tkinter import messagebox

import numpy as np
import pandas as pd
import pandastable as pt
from constants import IMAGES, WINDOW_TITLE


class MemoryGame:
    def __init__(self, rows: int, columns: int, username: str, level: str):
        self.rows = rows
        self.columns = columns
        self.moves = 0
        self.buttons = []
        self.first_button_row = None
        self.first_button_col = None
        self.unfound = self.columns * self.rows // 2
        self.username = username
        self.cards = self.generate_card_distribution()
        self.create_window()
        self.level = level

    def generate_card_distribution(self):
        assert self.rows * self.columns % 2 == 0, "cols * rows must be divisible by 2!"
        n_pairs = self.rows * self.columns // 2

        cards = list(range(n_pairs)) + list(range(n_pairs))

        cards = np.array(cards)

        # shuffle pairs
        np.random.shuffle(cards)

        # reshape arrays
        cards = np.reshape(cards, (self.rows, self.columns))

        return cards

    def generate_buttons(self):
        for row in range(self.rows):
            button_row = []
            for col in range(self.columns):
                button = tk.Button(
                    self.window,
                    text="",
                    font=("Arial", 20),
                    width=5,
                    height=2,
                    command=lambda r=row, c=col: self.reveal(r, c),
                )
                button.grid(row=row + 1, column=col)
                button_row.append(button)
            self.buttons.append(button_row)

    def create_window(self):
        self.window = tk.Tk()
        self.window.title(WINDOW_TITLE)

        # center window on screen
        self.window.geometry(
            f"+{self.window.winfo_screenwidth() // 2}+{self.window.winfo_screenheight() // 2 - 100}"
        )

        # Create moves label
        self.moves_label = tk.Label(self.window, text=f"Moves: {self.moves}")
        self.moves_label.grid(row=0, column=0, columnspan=self.columns)

        self.generate_buttons()

    def reveal(self, row, col):
        button = self.buttons[row][col]
        image_id = self.cards[row][col]
        button.config(text=IMAGES[image_id], state="disabled")
        if self.first_button_row is None:
            self.first_button_row = row
            self.first_button_col = col
        else:
            self.moves += 1
            self.moves_label.config(text=f"Moves: {self.moves}")
            if (
                self.cards[row][col]
                == self.cards[self.first_button_row][self.first_button_col]
            ):
                self.first_button_row = None
                self.first_button_col = None
                self.unfound -= 1
                if self.unfound == 0:
                    self.window.after(
                        500,
                        lambda: self.game_over(),
                    )

            else:
                first_button = self.buttons[self.first_button_row][
                    self.first_button_col
                ]
                self.first_button_row = None
                self.first_button_col = None
                self.window.after(
                    500,
                    lambda: self.hide(
                        first_button,
                        button,
                    ),
                )

    def hide(self, button1, button2):
        button1.config(text="", state="normal")
        button2.config(text="", state="normal")

    def save_score(self):
        scores_file = "scores.csv"
        new_score = pd.DataFrame(
            {"user": [self.username], "level": self.level, "score": [self.moves]}
        )
        scores = pd.read_csv(scores_file, index_col=False)
        scores = scores[["user", "level", "score"]]
        scores = pd.concat([scores, new_score])
        scores = scores.sort_values(by="score")
        scores.to_csv(scores_file)

    def game_over(self):
        self.save_score()
        print("SAVED!")
        messagebox.showinfo(
            "Game over",
            f"Congratulations {self.username}!, you have matched all pairs! \n Moves: {self.moves}",
        )

        self.window.destroy()

    def start_game(self):
        self.window.mainloop()


class StartMenu:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Memory Game")

        # center window on screen
        self.window.geometry(
            f"+{self.window.winfo_screenwidth() // 2}+{self.window.winfo_screenheight() // 2 - 100}"
        )

        # Add new game button
        self.new_game_button = tk.Button(
            self.window, text="New Game", command=self.new_game
        )
        self.new_game_button.pack()

        # Add high scores button
        self.high_scores_button = tk.Button(
            self.window, text="Show Highscores", command=self.show_high_scores
        )
        self.high_scores_button.pack()

    def new_game(self):
        # create new window for entering username and difficulty level
        new_game_window = tk.Toplevel(self.window)
        new_game_window.title("New Game")

        # center window on screen
        new_game_window.geometry(
            f"+{self.window.winfo_screenwidth() // 2}+{self.window.winfo_screenheight() // 2 - 100}"
        )
        new_game_window.geometry("280x250")

        # Add username label and entry
        self.username_label = tk.Label(new_game_window, text="Enter your username:")
        self.username_label.pack()
        self.username_entry = tk.Entry(new_game_window)
        self.username_entry.pack()

        # Add difficulty level options
        self.difficulty_label = tk.Label(
            new_game_window, text="Select difficulty level:"
        )
        self.difficulty_label.pack()
        self.difficulty_options = [("Easy", 2, 2), ("Medium", 4, 2), ("Hard", 4, 4)]
        self.difficulty_var = tk.StringVar()
        self.difficulty_var.set(self.difficulty_options[0][0])
        for option, _, _ in self.difficulty_options:
            tk.Radiobutton(
                new_game_window,
                text=option,
                variable=self.difficulty_var,
                value=option,
            ).pack()

        # Add start button
        self.start_button = tk.Button(
            new_game_window,
            text="Start Game",
            command=lambda: self.start_game(),
        )
        self.start_button.pack()

    def show_high_scores(self):
        high_scores_window = tk.Toplevel(self.window)
        high_scores_window.title("High Scores")

        # center window on screen
        high_scores_window.geometry(
            f"+{self.window.winfo_screenwidth() // 2}+{self.window.winfo_screenheight() // 2}"
        )
        high_scores_window.geometry("280x150")

        # read high scores from CSV file
        scores = pd.read_csv("scores.csv", index_col=False)

        scores.reset_index(inplace=True)
        scores = scores[["user", "level", "score"]]

        scores_table = pt.Table(
            high_scores_window,
            dataframe=scores,
            showtoolbar=False,
            showstatusbar=False,
            width=280,
        )
        scores_table.autoResizeColumns()

        scores_table.show()

    def start_game(self):
        username = self.username_entry.get()
        selected_difficulty = self.difficulty_var.get()
        (level, rows, columns) = [
            tup for tup in self.difficulty_options if tup[0] == selected_difficulty
        ][0]
        if not username:
            messagebox.showerror("Error", "Please enter a username.")
            return
        self.window.destroy()
        game = MemoryGame(rows=rows, columns=columns, username=username, level=level)
        game.start_game()

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    start_menu = StartMenu()
    start_menu.run()
