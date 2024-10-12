"""
This script is used to read input from the standard input.
This input are integer separated by space.
There might multiple lines of input.

The resulting output is the sum of all the integers.
"""
import argparse
from sys import stdin, stdout, stderr

from std_in_sum import split_lines, cast_to_integers


def read_lines(file_in) -> list:
    """
    Read lines from the standard input

       :param file_in: File object with input data
       :return: List of lines read from the standard input.
    """
    return file_in.read().splitlines()


def main() -> None:
    """
    Main function to read the input from the standard input and print the sum of the integers
    """
    parser = argparse.ArgumentParser(
        description="Sum integers from an input file"
        # file argument or stdin

    )
    parser.add_argument(
        "input",
        nargs="?",
        type=argparse.FileType("r"),
        default=stdin,
        help="File with integers separated by space, default is stdin"
    )
    parser.add_argument(
        "output",
        nargs="?",
        type=argparse.FileType("w"),
        default=stdout,
        help="File with the sum of the integers, default is stdout"
    )
    args = parser.parse_args()
    lines = read_lines(args.input)
    literals = split_lines(lines)
    integers = cast_to_integers(literals)
    print(sum(integers), file=args.output)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e, file=stderr)
        exit(1)
