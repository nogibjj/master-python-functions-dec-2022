#!/usr/bin/env python3
"""
Builds a command line interface for the math functions in mathCode.py.
Uses python fire to build the CLI.
"""
import fire
from funcLog.mathcode import add, subtract, multiply, divide


def main():
    fire.Fire(
        {"add": add, "subtract": subtract, "multiply": multiply, "divide": divide}
    )


if __name__ == "__main__":
    main()
