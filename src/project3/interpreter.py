from typing import Iterator

from project3.datalogprogram import DatalogProgram
from project3.reporter import QueryReporter, RuleReporter, RuleOptimizedReporter


class Interpreter:
    __slots__ = ["datalog"]

    def __init__(self, datalog: DatalogProgram) -> None:
        self.datalog = datalog

    def eval_schemes(self) -> None:
        raise NotImplementedError

    def eval_facts(self) -> None:
        raise NotImplementedError

    def eval_queries(self) -> Iterator[QueryReporter]:
        raise NotImplementedError

    def eval_rules(self) -> Iterator[RuleReporter]:
        raise NotImplementedError

    def eval_rules_optimized(self) -> Iterator[RuleOptimizedReporter]:
        raise NotImplementedError
