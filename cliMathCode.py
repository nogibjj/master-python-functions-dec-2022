#!/usr/bin/env python3
"""
Build a click based CLI that uses the logic in mathcode.py
"""
import click
from funcLog.mathcode import add, subtract, multiply, divide


@click.group()
def cli():
    """A CLI app that uses the mathcode functions:

    Example:

    $ cliMathCode.py add 1 2

    $ cliMathCode.py subtract 1 2

    $ cliMathCode.py multiply 1 2

    $ cliMathCode.py divide 1 2
    """


@cli.command("add")
@click.argument("a", type=int)
@click.argument("b", type=int)
def add_cli(a, b):
    """Add two numbers

    Example:

    $ cliMathCode.py add 1 2
    """
    click.echo(add(a, b))


@cli.command("subtract")
@click.argument("a", type=int)
@click.argument("b", type=int)
def subtract_cli(a, b):
    """Subtract two numbers

    Example:

    $ cliMathCode.py subtract 1 2
    """
    click.echo(subtract(a, b))


@cli.command("multiply")
@click.argument("a", type=int)
@click.argument("b", type=int)
def multiply_cli(a, b):
    """Multiply two numbers

    Example:

    $ cliMathCode.py multiply 1 2
    """
    click.echo(multiply(a, b))


@cli.command("divide")
@click.argument("a", type=int)
@click.argument("b", type=int)
def divide_cli(a, b):
    """Divide two numbers

    Example:

    $ cliMathCode.py divide 1 2
    """
    click.echo(divide(a, b))


if __name__ == "__main__":
    cli()
