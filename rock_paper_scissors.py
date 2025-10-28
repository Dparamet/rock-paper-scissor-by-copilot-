"""rock_paper_scissors.py

Simple Rock-Paper-Scissors game with a Tkinter GUI.

Controls:
- Click Rock, Paper or Scissors to play a round against the computer.
- Scores are tracked and shown on the window.
- Use Restart to reset scores, Quit to exit.

This file is standalone and uses only the Python standard library.
"""

import random
import tkinter as tk
from tkinter import messagebox


CHOICES = ["Rock", "Paper", "Scissors"]

def determine_winner(player, computer):
    """Return 'Player', 'Computer' or 'Tie' depending on winner."""
    if player == computer:
        return "Tie"
    # Define winning combinations for player
    wins = {
        "Rock": "Scissors",
        "Paper": "Rock",
        "Scissors": "Paper",
    }
    return "Player" if wins[player] == computer else "Computer"


class RPSApp:
    def __init__(self, master):
        self.master = master
        master.title("Rock Paper Scissors")
        master.resizable(False, False)

        self.player_score = 0
        self.computer_score = 0

        # Top info frame
        top = tk.Frame(master, padx=10, pady=10)
        top.pack(fill=tk.BOTH)

        self.score_label = tk.Label(top, text=self._score_text(), font=(None, 12), fg="#333")
        self.score_label.pack()

        # Choices display
        disp = tk.Frame(master, padx=10, pady=6)
        disp.pack(fill=tk.BOTH)

        self.player_choice_label = tk.Label(disp, text="Your choice: -", font=(None, 11))
        self.player_choice_label.grid(row=0, column=0, padx=8, pady=4)

        self.computer_choice_label = tk.Label(disp, text="Computer: -", font=(None, 11))
        self.computer_choice_label.grid(row=0, column=1, padx=8, pady=4)

        # Result label
        self.result_label = tk.Label(master, text="Make your move!", font=(None, 12, 'bold'), pady=6)
        self.result_label.pack()

        # Buttons for moves
        btn_frame = tk.Frame(master, padx=10, pady=10)
        btn_frame.pack()

        for i, choice in enumerate(CHOICES):
            b = tk.Button(btn_frame, text=choice, width=10, command=lambda c=choice: self.play(c))
            b.grid(row=0, column=i, padx=6)

        # Control buttons
        ctrl = tk.Frame(master, pady=8)
        ctrl.pack()

        restart = tk.Button(ctrl, text="Restart", command=self.reset_scores)
        restart.grid(row=0, column=0, padx=6)

        quit_btn = tk.Button(ctrl, text="Quit", command=self.master.quit)
        quit_btn.grid(row=0, column=1, padx=6)

        # Keyboard bindings for convenience (R, P, S)
        master.bind('<r>', lambda e: self.play('Rock'))
        master.bind('<p>', lambda e: self.play('Paper'))
        master.bind('<s>', lambda e: self.play('Scissors'))

    def _score_text(self):
        return f"Player: {self.player_score}   Computer: {self.computer_score}"

    def play(self, player_choice):
        computer_choice = random.choice(CHOICES)
        winner = determine_winner(player_choice, computer_choice)

        # Update displays
        self.player_choice_label.config(text=f"Your choice: {player_choice}")
        self.computer_choice_label.config(text=f"Computer: {computer_choice}")

        if winner == "Tie":
            self.result_label.config(text="It's a tie!", fg="#444")
        elif winner == "Player":
            self.player_score += 1
            self.result_label.config(text="You win this round!", fg="green")
        else:
            self.computer_score += 1
            self.result_label.config(text="Computer wins this round.", fg="red")

        self.score_label.config(text=self._score_text())

    def reset_scores(self):
        if messagebox.askyesno("Restart", "Reset scores and start over?"):
            self.player_score = 0
            self.computer_score = 0
            self.score_label.config(text=self._score_text())
            self.player_choice_label.config(text="Your choice: -")
            self.computer_choice_label.config(text="Computer: -")
            self.result_label.config(text="Make your move!", fg="#000")


def main():
    root = tk.Tk()
    app = RPSApp(root)
    root.mainloop()


if __name__ == '__main__':
    main()
