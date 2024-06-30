# Calculator App

This is a simple calculator application built using Python and Tkinter.

## Features

- Basic arithmetic operations: addition, subtraction, multiplication, division, and modulo
- Memory functions: M+, M-, MR, and MC to store and recall values
- Clear button to reset the input
- Evaluate button to calculate the result
- Support for decimal points
- Keyboard input support
- Responsive grid layout for better user experience

## How to Run

Ensure you have Python installed on your system.

1. Save the code in a file named `calculator.py`.
2. Open a terminal or command prompt and navigate to the directory where the file is saved.
3. Run the file using Python:
python calculator.py


## Requirements

- Python 3.x
- Tkinter (usually comes pre-installed with Python)


## Code Structure
- Calculator class: Initializes the calculator, handles button creation, and defines methods for calculator functionality.
- create_button method: Creates and places buttons using the grid layout.
- show method: Updates the entry value with the button pressed.
- clear method: Clears the entry value.
- solve method: Evaluates the expression and displays the result.
- safe_eval method: Safely evaluates the mathematical expression.
- memory_function method: Handles memory functions (M+, M-, MR, MC).
- bind_keys method: Binds keyboard keys to calculator functions.

## License
This project is licensed under the MIT License. See the LICENSE file for details.