from tabulate import tabulate

from typing import Any


class IncompatibleOperandError(Exception):
    def __init__(self, msg: str) -> None:
        super().__init__(msg)


class Relation:
    __slots__ = ["header", "set_of_tuples"]

    RelationTuple = tuple[str, ...]

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, Relation):
            return False
        return self.header == other.header and self.set_of_tuples == other.set_of_tuples

    def __init__(self, header: list[str], set_of_tuples: set[RelationTuple]):
        self.header = list(header)
        self.set_of_tuples: set[Relation.RelationTuple] = set()
        for i in set_of_tuples:
            self.add_tuple(i)

    def __repr__(self) -> str:
        return f"Relation(header={self.header!r}, set_of_tuples={self.set_of_tuples!r})"

    def __str__(self) -> str:
        sorted_tuples = sorted(self.set_of_tuples)
        value: str = tabulate(iter(sorted_tuples), self.header, tablefmt="pretty")
        return value

    def add_tuple(self, r: RelationTuple) -> None:
        if len(self.header) != len(r):
            raise IncompatibleOperandError(
                f"Error: {r} is not compatible with header {self.header} in Relation.add_tuple"
            )
        if not isinstance(r, tuple) or any(not isinstance(i, str) for i in r):
            raise IncompatibleOperandError(
                f"Error: {r} is not type compatible with Relation.RelationTuple in Relation.add_tuple"
            )
        self.set_of_tuples.add(r)

    def difference(self, right_operand: "Relation") -> "Relation":
        if self.header != right_operand.header:
            raise IncompatibleOperandError(
                f"Error: headers {self.header} and {right_operand.header} are not compatible in Relation.difference"
            )
        r = Relation(
            self.header,
            self.set_of_tuples.difference(right_operand.set_of_tuples),
        )
        return r

    def intersection(self, right_operand: "Relation") -> "Relation":
        raise NotImplementedError

    def join(self, right_operand: "Relation") -> "Relation":
        raise NotImplementedError

    def project(self, to: RelationTuple) -> "Relation":
        raise NotImplementedError

    def rename(self, to: RelationTuple) -> "Relation":
        raise NotImplementedError

    def select_eq_col(self, src: str, col: str) -> "Relation":
        raise NotImplementedError

    def select_eq_lit(self, src: str, lit: str) -> "Relation":
        raise NotImplementedError

    def union(self, right_operand: "Relation") -> "Relation":
        raise NotImplementedError
