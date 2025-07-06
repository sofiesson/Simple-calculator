import tkinter as tk

# Create the window
window = tk.Tk()
window.title("My First Window")

# Create a label
label = tk.Label(window, text="Hello, Tkinter!")
label.pack()

# Run the app
window.mainloop()
