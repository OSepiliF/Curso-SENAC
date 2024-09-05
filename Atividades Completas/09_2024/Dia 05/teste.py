from tkinter import *
from tkinter import Tk, ttk

# Function to evaluate the expression
def evaluate_expression():
    try:
        expression = entrada.get()
        result = eval(expression.replace('÷', '/').replace('x', '*').replace(',', '.'))
        entrada.delete(0, 'end')
        entrada.insert('end', result)
    except Exception as e:
        entrada.delete(0, 'end')
        entrada.insert('end', 'Error')

# Function to handle button presses
def button_click(value):
    current_text = entrada.get()
    if value == 'AC':
        entrada.delete(0, 'end')
    elif value == '=':
        evaluate_expression()
    else:
        entrada.insert('end', value)

# Create the main window
calculadora = Tk()
calculadora.title("Calculadora")
calculadora.geometry("400x400")

# Style for buttons
style = ttk.Style()
style.configure('custom.TButton', background='red', font=('Arial', 16), padding=4, width=4)

# Create a frame for the buttons
frame_buttons = Frame(calculadora, bg='gray18', width=400, height=400)
frame_buttons.place(relx=0.5, rely=0.5, anchor='center')

# Create an entry widget
entrada = Entry(frame_buttons, font=("Arial", 20), width=22)
entrada.place(relx=0.5, rely=0.2, anchor='center')

# Create a label
marca = Label(frame_buttons, text="FELELP's", font=("Titan One", 12, "bold"), bg='gray18', fg='white')
marca.place(relx=0.18, rely=0.1, anchor='center')

# Button layout and creation
buttons = [
    ('AC', '1', '2', '3', '÷'),
    ('4', '5', '6', 'x', '√'),
    ('7', '8', '9', '-', '%'),
    (',', '0', '=', '+')
]

for row_index, row in enumerate(buttons):
    for col_index, label in enumerate(row):
        button = ttk.Button(frame_buttons, style='custom.TButton', text=label, command=lambda l=label: button_click(l))
        button.grid(row=row_index, column=col_index, padx=5, pady=5, sticky='nsew')

# Make sure the grid expands correctly
for i in range(len(buttons)):
    frame_buttons.grid_rowconfigure(i, weight=1)
for i in range(len(buttons[0])):
    frame_buttons.grid_columnconfigure(i, weight=1)

# Run the application
calculadora.mainloop()
