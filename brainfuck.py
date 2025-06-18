# Brainfuck Interpreter
# Read in a text file containing Brainfuck code and execute in the terminal.
# Usage: python brainfuck.py <filename>

import sys

if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage: python brainfuck.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]

    try:
        with open(filename, "r") as file:
            code = file.read()
            # TODO: Add code to interpret the BF code
            print(f"Printing code from {filename}:\n{code}")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)
