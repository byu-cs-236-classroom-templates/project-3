from sys import argv
from typing import Iterator

from project3.interpreter import Interpreter
from project3.datalogprogram import DatalogProgram
from project3.lexer import lexer
from project3.parser import parse, UnexpectedTokenException
from project3.reporter import query_report
from project3.token import Token


def project3(input_string: str) -> str:
    token_iterator: Iterator[Token] = lexer(input_string)
    try:
        datalog_program: DatalogProgram = parse(token_iterator)
        interpreter: Interpreter = Interpreter(datalog_program)
        interpreter.eval_schemes()
        interpreter.eval_facts()
        answer = "\n".join([query_report(i, j) for i, j in interpreter.eval_queries()])
        return answer
    except UnexpectedTokenException as e:
        return "Failure!\n  " + str(e.token)


def project3cli() -> None:
    """Answer queries in a Datalog program

    `project3cli` is only called from the command line in the integrated terminal.
    Prints the results of each query in the Datalog program to the terminal.

    Args:
        argv (list[str]): Generated from the command line and needs to name the input file.

    Examples:

    ```
    $ cat prog.txt
    Schemes:
      SK(X,Y)
    Facts:
      SK('a','a').
    Rules:
      SK(A,B) :- SK(A,B).
    Queries:
      SK(D,C)?
      SK(A,'c')?

    $ project3 prog.txt
    SK(D,C)? Yes(1)
      D='a', C='a'
    SK(A,'c')? No
    ```
    """
    if len(argv) == 2:
        input_file = argv[1]
        with open(input_file, "r") as f:
            input_string = f.read()
            result = project3(input_string)
            print(result)
    else:
        print("usage: project3 <input file>")
