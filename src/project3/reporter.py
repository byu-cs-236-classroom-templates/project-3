from functools import reduce

from project3.datalogprogram import Predicate
from project3.relation import Relation


def _is_only_strings(predicate: Predicate) -> bool:
    return reduce(
        lambda is_only_string, parameter: is_only_string and parameter.is_string(),
        predicate.parameters,
        True,
    )


def _tuple_to_str(header: Relation.RelationTuple, r: Relation.RelationTuple) -> str:
    assert len(header) == len(r)
    entries = [f"{i[0]}={i[1]}" for i in zip(header, r)]
    return ", ".join(entries)


def query_report(query: Predicate, answer: Relation) -> str:
    tuples: list[Relation.RelationTuple] = sorted(answer.set_of_tuples)
    if len(tuples) == 0:
        return f"{query}? No"

    if _is_only_strings(query):
        return f"{query}? Yes({len(tuples)})"

    entries = [_tuple_to_str(answer.header, row) for row in tuples]
    entries_str = "\n  ".join(entries)
    return f"{query}? Yes({len(tuples)})\n  {entries_str}"
