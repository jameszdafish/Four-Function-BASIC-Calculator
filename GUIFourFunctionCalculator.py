from tkinter import *
from tkinter import messagebox
from tkinter import font
root = Tk()
root.title("Four Function BASIC Calculator")
root.geometry("225x475")

expression = ""


def on_check_press_event():
    messagebox.showinfo("Message", "This is your display value: " + str(expression))


def on_all_clear_press_event():
    global expression
    expression = ""
    display_label.config(text=expression)


def on_backspace_press_event():
    global expression
    expression = expression[:-1]
    display_label.config(text=expression)


def on_operation_press_event(operation_type):
    global expression
    if operation_type == 1:
        expression += "+"
    elif operation_type == 2:
        expression += "-"
    elif operation_type == 3:
        expression += "*"
    elif operation_type == 4:
        expression += "/"
    display_label.config(text=expression)


def on_digit_press_event(digit):
    global expression
    expression += str(digit)
    display_label.config(text=expression)


def add(list_input1, list_input2):
    temp_answer = int(list_input1) + int(list_input2)
    return temp_answer


def subtract(list_input1, list_input2):
    temp_answer = int(list_input1) - int(list_input2)
    return temp_answer


def divide(list_input1, list_input2):
    temp_answer = int(int(list_input1) / int(list_input2))
    return temp_answer


def multiply(list_input1, list_input2):
    temp_answer = int(list_input1) * int(list_input2)
    return temp_answer


def on_equal_press_event(input_string):
    steps = 0
    numbers = ""
    text = ""
    solving_list = []
    for i in input_string:
        if steps == 0:
            if i.isdigit():
                numbers += i
                steps += 1
            else:
                messagebox.showinfo("Message", "Please rerun the code with your expression starting with an integer.")
                exit()
        else:
            if i.isdigit():
                numbers += i
            else:
                solving_list.append(numbers)
                numbers = ""
                text += i
                solving_list.append(text)
                text = ""
    solving_list.append(numbers)

    while len(solving_list) > 1:
        stop_timer = 0

        if solving_list[1] == "+":
            calculated_value = add(solving_list[0], solving_list[2])
            solving_list = solving_list[3:]
            solving_list.insert(0, str(calculated_value))
        elif solving_list[1] == "-":
            calculated_value = subtract(solving_list[0], solving_list[2])
            solving_list = solving_list[3:]
            solving_list.insert(0, str(calculated_value))
        elif solving_list[1] == "/":
            calculated_value = divide(solving_list[0], solving_list[2])
            solving_list = solving_list[3:]
            solving_list.insert(0, str(calculated_value))
        elif solving_list[1] == "*":
            calculated_value = multiply(solving_list[0], solving_list[2])
            solving_list = solving_list[3:]
            solving_list.insert(0, str(calculated_value))
        else:
            stop_timer += 1
        if stop_timer == 1:
            break
    global expression
    expression = ""
    expression += solving_list[0]
    display_label.config(text=expression)


button_font = font.Font(family="Roboto", size=15)
label_font = font.Font(family="Roboto", size=30)

display_label = Label(text=expression, font=label_font, relief=RIDGE)
display_label.grid(row=0, columnspan=4, sticky="NSEW")

button0 = Button(text="0", font=button_font, command=lambda: on_digit_press_event(0))
button1 = Button(text="1", font=button_font, command=lambda: on_digit_press_event(1))
button2 = Button(text="2", font=button_font, command=lambda: on_digit_press_event(2))
button3 = Button(text="3", font=button_font, command=lambda: on_digit_press_event(3))
button4 = Button(text="4", font=button_font, command=lambda: on_digit_press_event(4))
button5 = Button(text="5", font=button_font, command=lambda: on_digit_press_event(5))
button6 = Button(text="6", font=button_font, command=lambda: on_digit_press_event(6))
button7 = Button(text="7", font=button_font, command=lambda: on_digit_press_event(7))
button8 = Button(text="8", font=button_font, command=lambda: on_digit_press_event(8))
button9 = Button(text="9", font=button_font, command=lambda: on_digit_press_event(9))

add_button = Button(text="+", font=button_font, command=lambda: on_operation_press_event(1))
subtract_button = Button(text="−", font=button_font, command=lambda: on_operation_press_event(2))
multiply_button = Button(text="×", font=button_font, command=lambda: on_operation_press_event(3))
divide_button = Button(text="÷", font=button_font, command=lambda: on_operation_press_event(4))

equals_button = Button(text="=", font=button_font, command=lambda: on_equal_press_event(expression))
all_clear_button = Button(text="AC", font=button_font, command=on_all_clear_press_event)
backspace_button = Button(text="⌫", font=button_font, command=on_backspace_press_event)
percentage_button = Button(text="%", font=button_font)
decimal_button = Button(text=".", font=button_font)

Grid.rowconfigure(root, 0, weight=1)
Grid.columnconfigure(root, 0, weight=1)
Grid.rowconfigure(root, 1, weight=1)
Grid.columnconfigure(root, 1, weight=1)
Grid.rowconfigure(root, 2, weight=1)
Grid.columnconfigure(root, 2, weight=1)
Grid.rowconfigure(root, 3, weight=1)
Grid.columnconfigure(root, 3, weight=1)
Grid.rowconfigure(root, 4, weight=1)
Grid.rowconfigure(root, 5, weight=1)

button0.grid(row=5, column=0, columnspan=2, sticky="NSEW")
button1.grid(row=4, column=0, sticky="NSEW")
button2.grid(row=4, column=1, sticky="NSEW")
button3.grid(row=4, column=2, sticky="NSEW")
button4.grid(row=3, column=0, sticky="NSEW")
button5.grid(row=3, column=1, sticky="NSEW")
button6.grid(row=3, column=2, sticky="NSEW")
button7.grid(row=2, column=0, sticky="NSEW")
button8.grid(row=2, column=1, sticky="NSEW")
button9.grid(row=2, column=2, sticky="NSEW")

add_button.grid(row=4, column=3, sticky="NSEW")
subtract_button.grid(row=3, column=3, sticky="NSEW")
multiply_button.grid(row=2, column=3, sticky="NSEW")
divide_button.grid(row=1, column=3, sticky="NSEW")
equals_button.grid(row=5, column=3, sticky="NSEW")

all_clear_button.grid(row=1, column=0, sticky="NSEW")
backspace_button.grid(row=1, column=1, sticky="NSEW")
percentage_button.grid(row=1, column=2, sticky="NSEW")
decimal_button.grid(row=5, column=2, sticky="NSEW")

root.mainloop()
