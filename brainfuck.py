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

    call_stack = []  # Create an empty call stack for looping

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

        # Print the character representation of the current cell value
        if commands[command_pointer] == ".":
            print(chr(tape[tape_pointer]), end="")

        # Read a character from standard in and store it in the current cell
        if commands[command_pointer] == ",":
            tape[tape_pointer] = ord(sys.stdin.read(1))

        # Start a loop if the current cell value is not 0, otherwise skip to the matching close bracket
        if commands[command_pointer] == "[":
            if tape[tape_pointer] == 0:
                open_counter = 0
                while command_pointer < len(commands):
                    command_pointer += 1
                    if command_pointer == len(commands):
                        print("Mismatched looping brackets!", file=sys.stderr)
                        sys.exit(1)
                    if commands[command_pointer] == "[":
                        open_counter += 1
                    if commands[command_pointer] == "]":
                        if open_counter == 0:
                            break
                        else:
                            open_counter -= 1

            else:
                call_stack.append(command_pointer)

        # End a loop if the current cell value is 0, otherwise jump back to the matching open bracket
        if commands[command_pointer] == "]":
            if tape[tape_pointer] != 0:
                command_pointer = call_stack[-1]
            elif len(call_stack) != 0:
                call_stack.pop()

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
