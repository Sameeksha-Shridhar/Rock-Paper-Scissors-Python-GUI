import tkinter as tk
import random
import time

# Create the main window
root = tk.Tk()
root.title("Rock-Paper-Scissors")
root.geometry("500x500")
root.config(bg="#d6eaf8")

# Scores
user_score = 0
comp_score = 0

# Choices
choices = ["Rock", "Paper", "Scissors"]

# Labels
title_label = tk.Label(root, text="Rock Paper Scissors", font=("Arial", 16, "bold"), bg="#d6eaf8")
title_label.pack(pady=10)

result_label = tk.Label(root, text="Make your move!", font=("Arial", 12), bg="#d6eaf8")
result_label.pack(pady=5)

score_label = tk.Label(root, text=f"Score → You: {user_score} | Computer: {comp_score}", font=("Arial", 12), bg="#d6eaf8")
score_label.pack(pady=5)

# Function to play the game
def play(user_choice):
    global user_score, comp_score
    result_label.config(text="Computer is choosing...")
    root.update()
    time.sleep(0.5)

    comp_choice = random.choice(choices)

    if user_choice == comp_choice:
        result = "It's a Tie!"
    elif (user_choice == "Rock" and comp_choice == "Scissors") or \
         (user_choice == "Paper" and comp_choice == "Rock") or \
         (user_choice == "Scissors" and comp_choice == "Paper"):
        result = "You Win!"
        user_score += 1
    else:
        result = "Computer Wins!"
        comp_score += 1

    result_label.config(text=f"You: {user_choice} | Computer: {comp_choice} → {result}")
    score_label.config(text=f"Score → You: {user_score} | Computer: {comp_score}")

# Buttons
button_frame = tk.Frame(root, bg="#d6eaf8")
button_frame.pack(pady=20)

rock_btn = tk.Button(button_frame, text="Rock", width=10, command=lambda: play("Rock"))
rock_btn.grid(row=0, column=0, padx=5)

paper_btn = tk.Button(button_frame, text="Paper", width=10, command=lambda: play("Paper"))
paper_btn.grid(row=0, column=1, padx=5)

scissors_btn = tk.Button(button_frame, text="Scissors", width=10, command=lambda: play("Scissors"))
scissors_btn.grid(row=0, column=2, padx=5)

# Restart button
def restart():
    global user_score, comp_score
    user_score = 0
    comp_score = 0
    result_label.config(text="Make your move!")
    score_label.config(text=f"Score → You: {user_score} | Computer: {comp_score}")

restart_btn = tk.Button(root, text="Restart Game", command=restart)
restart_btn.pack(pady=10)

# Start the GUI
root.mainloop()