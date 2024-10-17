from functools import reduce

from project3.datalogprogram import Predicate
from project3.relation import Relation


def _is_only_strings(predicate: Predicate) -> bool:
    return reduce(
        lambda is_only_string, parameter: is_only_string and parameter.is_string(),
        predicate.parameters,
        True,
    )


def _rtuple_to_str(header: Relation.rtuple, r: Relation.rtuple) -> str:
    assert len(header) == len(r)
    entries = [f"{i[0]}={i[1]}" for i in zip(header, r)]
    return ", ".join(entries)


class QueryReporter:
    __slots__ = ["query", "answer"]

    def __init__(self, query: Predicate, answer: Relation) -> None:
        self.query = query
        self.answer = answer

    def __repr__(self) -> str:
        return f"QueryReporter(query={self.query!r}, answer={self.answer!r})"

    def __str__(self) -> str:
        if len(self.answer.rtuples) == 0:
            return f"{self.query}? No"

        if _is_only_strings(self.query):
            return f"{self.query}? Yes({len(self.answer.rtuples)})"

        entries = [
            _rtuple_to_str(self.answer.header, row) for row in self.answer.rtuples
        ]
        entries_str = "\n  ".join(entries)
        return f"{self.query}? Yes({len(self.answer.rtuples)})\n  {entries_str}"


class RuleReporter:
    pass


class RuleOptimizedReporter:
    pass
