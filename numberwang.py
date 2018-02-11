#!/usr/bin/env python3
"""
A recreation of Numberwang, but in Python.
"""
import sys
import random


__version__ = '0.0.1'


def is_that_numberwang(sentence):
    """
    Given a sentence, will return a boolean indication if the sentence is
    numberwang.

    A valid sentence must contain a number.

    If the sentence is invalid, a ValueError exception is generated.
    """
    if any(char.isdigit() for char in sentence):
        return random.randint(0, 4) == 0
    else:
        raise ValueError('Invalid sentence: missing a number.')


def main():
    """
    Reads input from arguments passed into the script and prints the
    output (should there be any) to stdout.
    """
    args = sys.argv[1:]
    sentence = ' '.join(args)
    try:
        if is_that_numberwang(sentence):
            print("That's Numberwang!")
    except ValueError:
        print("Input must contain a number.")


if __name__ == '__main__':  # pragma: no cover
    main()
