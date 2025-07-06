import tkinter as tk


def click(event):
    global expression
    expression += str(event.widget.cget("text"))
    result_var.set(expression)


def clear():
    global expression
    expression = ""
    result_var.set(expression)


def evaluate():
    global expression
    try:
        result = eval(expression)
        result_var.set(result)
        expression = str(result)
    except:
        result_var.set("Error")
        expression = ""


expression = ""
root = tk.Tk()
root.title("Simple Calculator")

result_var = tk.StringVar()
entry = tk.Entry(root, textvariable=result_var, font="Arial 20", bd=10, relief=tk.RIDGE, justify="right")
entry.pack(fill=tk.BOTH, ipadx=8)

button_frame = tk.Frame(root)
button_frame.pack()

buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '=', '+']
]

for row in buttons:
    button_row = tk.Frame(button_frame)
    button_row.pack(expand=True, fill="both")
    for btn_text in row:
        button = tk.Button(button_row, text=btn_text, font="Arial 18",
                           relief=tk.GROOVE, height=2, width=5)
        button.pack(side="left", expand=True, fill="both")
        if btn_text == "=":
            button.bind("<Button-1>", lambda e: evaluate())
        else:
            button.bind("<Button-1>", click)

clear_button = tk.Button(root, text="Clear", font="Arial 18", relief=tk.GROOVE,
                         command=clear)
clear_button.pack(fill="both")

root.mainloop()