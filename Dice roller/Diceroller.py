import tkinter as tk
import random

def roll_dice():
    result.set(random.randint(1, 6))

root = tk.Tk()
root.title("Dice Roller")

result = tk.StringVar()
result.set("Roll the Dice!")

label = tk.Label(root, textvariable = result, font = "Arial 24")
label.pack(pady = 20)

button = tk.Button(root, text = "Roll", font = "Arial 18", command = roll_dice)
button.pack(pady = 20)

root.mainloop()
