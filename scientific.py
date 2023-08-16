import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedStyle
import math

def on_button_click(event):
    current = event.widget.cget("text")

    if current == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif current == "C":
        entry.delete(0, tk.END)
    elif current == "√":
        entry.insert(tk.END, "sqrt(")
    elif current == "x²":
        entry.insert(tk.END, "**2")
    elif current == "sin":
        entry.insert(tk.END, "math.sin(")
    elif current == "cos":
        entry.insert(tk.END, "math.cos(")
    elif current == "tan":
        entry.insert(tk.END, "math.tan(")
    elif current == "π":
        entry.insert(tk.END, "math.pi")
    else:
        entry.insert(tk.END, current)

# Create the main application window
root = tk.Tk()
root.title("Scientific Calculator")
root.geometry("400x500")
root.resizable(False, False)

# Apply the Material Design theme
style = ThemedStyle(root)
style.set_theme("equilux")

# Create the custom style for the buttons
style.configure("My.TButton", font=("Helvetica", 16, "bold"))

# Create the entry widget for displaying the input and result
entry = ttk.Entry(root, font="Helvetica 20 bold", justify="right")
entry.pack(fill=tk.BOTH, padx=10, pady=10)

# Create a frame to hold the buttons
button_frame = ttk.Frame(root)
button_frame.pack(padx=10, pady=5)

# Define the buttons
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "C", "0", "=", "+",
    "√", "x²", "sin", "cos",
    "tan", "π"
]

# Create and layout the buttons
row, col = 1, 0
for button_text in buttons:
    button = ttk.Button(button_frame, text=button_text, style="My.TButton")
    button.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)
    button.bind("<Button-1>", on_button_click)

    col += 1
    if col > 4:
        col = 0
        row += 1

# Make all buttons of equal size
button_frame.grid_columnconfigure(0, weight=1)
button_frame.grid_columnconfigure(1, weight=1)
button_frame.grid_columnconfigure(2, weight=1)
button_frame.grid_columnconfigure(3, weight=1)
button_frame.grid_columnconfigure(4, weight=1)

button_frame.grid_rowconfigure(0, weight=1)
button_frame.grid_rowconfigure(1, weight=1)
button_frame.grid_rowconfigure(2, weight=1)
button_frame.grid_rowconfigure(3, weight=1)
button_frame.grid_rowconfigure(4, weight=1)
button_frame.grid_rowconfigure(5, weight=1)
button_frame.grid_rowconfigure(6, weight=1)

# Start the main loop
root.mainloop()
