from sortedcontainers import SortedSet  # type: ignore
from tabulate import tabulate

from typing import Any


class IncompatibleOperandError(Exception):
    def __init__(self, msg: str) -> None:
        super().__init__(msg)


class Relation:
    __slots__ = ["name", "header", "rtuples"]

    rtuple = tuple[str, ...]

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, Relation):
            return False
        return (
            self.name == other.name
            and self.header == other.header
            and self.rtuples == other.rtuples
        )

    def __init__(self, name: str, header: rtuple, rtuples: SortedSet[rtuple]):
        self.name = name
        self.header = header
        self.rtuples = SortedSet()
        for i in rtuples:
            self.add_rtuple(i)

    def __repr__(self) -> str:
        return f"Relation(name={self.name!r}, header={self.header!r}, rtuples={self.rtuples!r})"

    def __str__(self) -> str:
        value: str = tabulate(iter(self.rtuples), self.header, tablefmt="pretty")
        return value

    def add_rtuple(self, r: rtuple) -> None:
        if len(self.header) != len(r):
            raise IncompatibleOperandError(
                f"Error: {r} is not compatible with header {self.header} in Relation.add_rtuple"
            )
        self.rtuples.add(r)

    def difference(self, right_operand: "Relation") -> "Relation":
        if self.header != right_operand.header:
            raise IncompatibleOperandError(
                f"Error: headers {self.header} and {right_operand.header} are not compatible in Relation.difference"
            )
        r = Relation(
            self.name, self.header, self.rtuples.difference(right_operand.rtuples)
        )
        return r

    def intersection(self, right_operand: "Relation") -> "Relation":
        raise NotImplementedError

    def join(self, right_operand: "Relation") -> "Relation":
        raise NotImplementedError

    def project(self, to: rtuple) -> "Relation":
        raise NotImplementedError

    def rename(self, to: rtuple) -> "Relation":
        raise NotImplementedError

    def select_eq_col(self, src: str, col: str) -> "Relation":
        raise NotImplementedError

    def select_eq_lit(self, src: str, lit: str) -> "Relation":
        raise NotImplementedError

    def union(self, right_operand: "Relation") -> "Relation":
        raise NotImplementedError
