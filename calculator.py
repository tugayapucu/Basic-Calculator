from tkinter import Tk, Entry, Button, StringVar
import operator

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")
        master.config(bg="gray")
        master.resizable(False, False)

        self.equation = StringVar()
        self.entry_value = ""
        Entry(master, width=17, bg="#fff", font=("Arial Bold", 28), textvariable=self.equation).grid(row=0, column=0, columnspan=4, ipadx=8, ipady=8)

        buttons = [
            ('(', 1, 0), (')', 1, 1), ('%', 1, 2), ('+', 1, 3),
            ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3),
            ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('*', 3, 3),
            ('7', 4, 0), ('8', 4, 1), ('9', 4, 2), ('/', 4, 3),
            ('.', 5, 0), ('0', 5, 1), ('C', 5, 2), ('=', 5, 3),
            ('M+', 6, 0), ('M-', 6, 1), ('MR', 6, 2), ('MC', 6, 3)
        ]

        for (text, row, col) in buttons:
            self.create_button(text, row, col)

        self.memory = 0
        self.bind_keys()

    def create_button(self, text, row, col):
        if text == 'C':
            Button(self.master, width=10, height=3, text=text, relief='flat', bg='white', command=self.clear).grid(row=row, column=col, padx=5, pady=5)
        elif text == '=':
            Button(self.master, width=10, height=3, text=text, relief='flat', bg='white', command=self.solve).grid(row=row, column=col, padx=5, pady=5)
        elif text in ['M+', 'M-', 'MR', 'MC']:
            Button(self.master, width=10, height=3, text=text, relief='flat', bg='white', command=lambda t=text: self.memory_function(t)).grid(row=row, column=col, padx=5, pady=5)
        else:
            Button(self.master, width=10, height=3, text=text, relief='flat', bg='white', command=lambda t=text: self.show(t)).grid(row=row, column=col, padx=5, pady=5)

    def show(self, value):
        self.entry_value += str(value)
        self.equation.set(self.entry_value)

    def clear(self):
        self.entry_value = ''
        self.equation.set(self.entry_value)

    def solve(self):
        try:
            result = self.safe_eval(self.entry_value)
            self.equation.set(result)
            self.entry_value = str(result)
        except ZeroDivisionError:
            self.equation.set("Error: Division by zero")
            self.entry_value = ""
        except Exception as e:
            self.equation.set("Error")
            self.entry_value = ""

    def safe_eval(self, expression):
        allowed_operators = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv, '%': operator.mod}
        stack = []
        num = ""
        for char in expression:
            if char.isdigit() or char == '.':
                num += char
            else:
                if num:
                    stack.append(float(num))
                    num = ""
                if char in allowed_operators:
                    stack.append(char)
        if num:
            stack.append(float(num))

        def apply_operator(operators, values):
            operator = operators.pop()
            right = values.pop()
            left = values.pop()
            values.append(allowed_operators[operator](left, right))

        operators = []
        values = []
        i = 0
        while i < len(stack):
            if isinstance(stack[i], float):
                values.append(stack[i])
            else:
                while (operators and operators[-1] in allowed_operators and
                       allowed_operators[operators[-1]].__code__.co_argcount > allowed_operators[stack[i]].__code__.co_argcount):
                    apply_operator(operators, values)
                operators.append(stack[i])
            i += 1

        while operators:
            apply_operator(operators, values)

        return values[0] if values else "Error"

    def memory_function(self, func):
        try:
            if func == 'M+':
                self.memory += float(self.entry_value)
            elif func == 'M-':
                self.memory -= float(self.entry_value)
            elif func == 'MR':
                self.equation.set(self.memory)
                self.entry_value = str(self.memory)
            elif func == 'MC':
                self.memory = 0
        except ValueError:
            pass

    def bind_keys(self):
        self.master.bind('<Return>', lambda event: self.solve())
        self.master.bind('<BackSpace>', lambda event: self.clear())
        for key in '1234567890+-*/().%':
            self.master.bind(key, lambda event, char=key: self.show(char))

root = Tk()
calculator = Calculator(root)
root.mainloop()
