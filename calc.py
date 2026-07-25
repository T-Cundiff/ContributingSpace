import math
import tkinter as tk

# Initialize main application window
wind = tk.Tk()
wind.geometry("270x430")
wind.resizable(False, False)
wind.title("Basic Calculator")

# Entry Display
text = tk.Entry(wind, font=("arial", 16), justify="right")
text.pack(fill=tk.X, padx=5, pady=5, ipady=5)


def addToText(n):
    text.insert(tk.END, n)


def calculate():
    """Evaluates the expression in the entry box safely."""
    try:
        expression = text.get()
        if not expression:
            return
        result = eval(expression)
        text.delete(0, tk.END)
        text.insert(0, result)
    except Exception:
        text.delete(0, tk.END)
        text.insert(0, "Error")


def button_clear():
    text.delete(0, tk.END)


# Frame container for buttons
frame = tk.Frame(wind)
frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

# Grid Configuration for main buttons (0-9, ., =)
buttons = [
    ("1", 0, 0),
    ("2", 0, 1),
    ("3", 0, 2),
    ("4", 1, 0),
    ("5", 1, 1),
    ("6", 1, 2),
    ("7", 2, 0),
    ("8", 2, 1),
    ("9", 2, 2),
    (".", 3, 0),
    ("0", 3, 1),
    ("=", 3, 2),
]

# Dynamically generate key grid
for char, row, col in buttons:
    cmd = calculate if char == "=" else lambda c=char: addToText(c)
    btn = tk.Button(
        frame,
        text=char,
        fg="black",
        bg="#696969",
        width=7,
        height=3,
        command=cmd,
    )
    btn.grid(row=row, column=col, sticky="nsew")

# Right Frame for Operator Buttons
rightFrame = tk.Frame(frame)
rightFrame.grid(row=0, column=3, rowspan=4, sticky="nsew")

operators = [("/", "/"), ("x", "*"), ("-", "-"), ("+", "+"), ("%", "%")]

for op_text, op_val in operators:
    btn = tk.Button(
        rightFrame,
        text=op_text,
        fg="black",
        bg="#696969",
        width=5,
        height=2,
        command=lambda v=op_val: addToText(v),
    )
    btn.pack(fill=tk.BOTH, expand=True)

# Clear Button Frame
frame5 = tk.Frame(wind)
frame5.pack(fill=tk.X)

btnclear = tk.Button(
    frame5,
    text="C",
    fg="black",
    bg="#696969",
    height=2,
    command=button_clear,
)
btnclear.pack(fill=tk.X, padx=5, pady=2)

wind.mainloop()