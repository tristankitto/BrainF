# Brainfuck Interpreter
# Read in a text file containing Brainfuck code and execute in the terminal.
# Usage: python brainfuck.py <filename>

import sys


def interpret(code):
    # Convert Brainfuck code to a list of commands
    commands = list(code)

    # Initialise variables
    tape = [0] * 30000  # 30,000 cells in the tape
    command_pointer = 0  # Start at the beginning of the code
    tape_pointer = 0  # Start at the first cell on the tape

    # Perform commands for each command in input file
    while command_pointer < len(commands):

        # Increment current cell value by one, or set to 0 if already at max value (255 for Extended ASCII)
        if commands[command_pointer] == "+":
            if tape[tape_pointer] < 255:
                tape[tape_pointer] += 1
            else:
                tape[tape_pointer] = 0

        # Decrement current cell value by one, or set to 255 if already at zero
        if commands[command_pointer] == "-":
            if tape[tape_pointer] > 0:
                tape[tape_pointer] -= 1
            else:
                tape[tape_pointer] = 255

        # Increment the tape pointer by one, moving the pointer to the cell to the right of the current position
        # If the pointer is already at the end of the tape then move to the beginning
        if commands[command_pointer] == ">":
            tape_pointer += 1
            if len(tape) == tape_pointer:
                tape_pointer = 0

        # Decrement the tape pointer by one, moving the pointer to the cell to the left of the current position
        # If the pointer is already at the beginning of the tape then move to the end
        if commands[command_pointer] == "<":
            tape_pointer -= 1
            if tape_pointer < 0:
                tape_pointer = len(tape) - 1

        # Increment the command pointer by one, moving on to the next command in the input code
        command_pointer += 1


if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: python brainfuck.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]

    try:
        file = open(filename, "r")
        code = file.read()
        interpret(code)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)
