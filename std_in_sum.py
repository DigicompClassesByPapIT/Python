"""
This script is used to read input from the standard input.
This input are integer separated by space.
There might multiple lines of input.

The resulting output is the sum of all the integers.
"""
from sys import stdin, stdout, stderr


def read_lines() -> list:
    """
    Read lines from the standard input

       :return: list of lines read from the standard input.
    """
    return stdin.read().splitlines()


def split_lines(lines: list) -> list:
    """
    Split the lines into literals

       :param lines: A list of lines
       :return: A list of literals
    """
    return [line.split() for line in lines]


def cast_to_integers(literals: list) -> list:
    """
    Cast the literals to integers

       :param literals: A list of of list of literals
       :return: A list of sums, one by line
    """
    return [sum([int(l) for l in literal]) for literal in literals]


def main() -> None:
    """
    Main function to read the input from the standard input and print the sum of the integers
    """
    lines = read_lines()
    literals = split_lines(lines)
    integers = cast_to_integers(literals)
    # print(sum(integers), file=stdout)
    stdout.write(str(sum(integers)) + "\n")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        # print(e, file=stderr)
        stderr.write(e)
        exit(1)
