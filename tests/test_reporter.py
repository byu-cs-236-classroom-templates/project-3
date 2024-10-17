# type: ignore
import pytest
from sortedcontainers import SortedSet

from project3.datalogprogram import Parameter, Predicate
from project3.relation import Relation
from project3.reporter import QueryReporter

input_literals_no = QueryReporter(
    Predicate("SK", [Parameter.string("'c'"), Parameter.string("'c'")]),
    Relation("SK", ("X", "Y"), SortedSet()),
)
expect_literals_no = "SK('c','c')? No"


input_literals_yes = QueryReporter(
    Predicate("SK", [Parameter.string("'b'"), Parameter.string("'c'")]),
    Relation("SK", ("X", "Y"), SortedSet([("'b'", "'c'")])),
)
expect_literals_yes = "SK('b','c')? Yes(1)"


input_mixed_no = QueryReporter(
    Predicate("SK", [Parameter.id("A"), Parameter.string("'c'")]),
    Relation("SK", ("A",), SortedSet()),
)
expect_mixed_no = "SK(A,'c')? No"


input_mixed_yes = QueryReporter(
    Predicate("SK", [Parameter.id("A"), Parameter.string("'c'")]),
    Relation("SK", ("A",), SortedSet([("'a'",), ("'b'",)])),
)
expect_mixed_yes = """SK(A,'c')? Yes(2)
  A='a'
  A='b'"""

input_id_yes = QueryReporter(
    Predicate("SK", [Parameter.id("A"), Parameter.string("B")]),
    Relation(
        "SK", ("A", "B"), SortedSet([("'a'", "'b'"), ("'a'", "'c'"), ("'b'", "'c'")])
    ),
)
expect_id_yes = """SK(A,B)? Yes(3)
  A='a', B='b'
  A='a', B='c'
  A='b', B='c'"""


@pytest.mark.parametrize(
    argnames=("input", "expect"),
    argvalues=(
        (input_literals_no, expect_literals_no),
        (input_literals_yes, expect_literals_yes),
        (input_mixed_no, expect_mixed_no),
        (input_mixed_yes, expect_mixed_yes),
        (input_id_yes, expect_id_yes),
    ),
    ids=[
        "literals_no",
        "literals_yes",
        "mixed_no",
        "mixed_yes",
        "id_yes",
    ],
)
def test_given_query_reporter_when_str_then_match_expect(input, expect):
    # given
    # input, expect

    # when
    answer = str(input)

    # then
    assert expect == answer
