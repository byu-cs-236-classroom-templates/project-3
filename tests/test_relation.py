# type: ignore
import pytest
from sortedcontainers import SortedSet
from project3.relation import IncompatibleOperandError, Relation


def test_given_empty_relation_when_add_rtuple_then_tuple_in_relation():
    # given
    name = "f"
    header = ("a", "b", "c")
    relation = Relation(name, header, SortedSet())
    input = ("'1'", "'2'", "'3'")

    # when
    relation.add_rtuple(input)

    # then
    assert 1 == len(relation.rtuples)
    assert input in relation.rtuples


def test_given_relation_when_repr_then_match_expected():
    # given
    name = "f"
    header = ("a", "b", "c")
    rtuples = SortedSet([("'1'", "'2'", "'3'"), ("'1'", "'3'", "'5'")])
    relation = Relation(name, header, rtuples)

    expected = """Relation(name='f', header=('a', 'b', 'c'), rtuples=SortedSet([("'1'", "'2'", "'3'"), ("'1'", "'3'", "'5'")]))"""

    # when
    answer = repr(relation)

    # then
    assert expected == answer


def test_given_relation_when_str_then_match_expected():
    # given
    name = "f"
    header = ("a", "b", "c")
    rtuples = SortedSet([("'1'", "'2'", "'3'"), ("'1'", "'3'", "'5'")])
    relation = Relation(name, header, rtuples)

    expected = """+-----+-----+-----+
|  a  |  b  |  c  |
+-----+-----+-----+
| '1' | '2' | '3' |
| '1' | '3' | '5' |
+-----+-----+-----+"""

    # when
    answer = str(relation)

    # then
    assert expected == answer


def test_given_relation_and_wrong_size_when_add_rtuple_then_exception():
    # given
    relation = Relation("f", ("a", "b", "c"), SortedSet())

    # when
    with pytest.raises(IncompatibleOperandError) as exception:
        relation.add_rtuple(("1", "2"))

    # then
    assert (
        "Error: ('1', '2') is not compatible with header ('a', 'b', 'c') in Relation.add_rtuple"
        == str(exception.value)
    )


def test_given_relation_when_add_rtuple_then_added():
    # given
    relation = Relation("f", ("a", "b", "c"), SortedSet())

    # when
    relation.add_rtuple(("1", "2", "3"))

    # then
    assert ("1", "2", "3") in relation.rtuples


def test_given_mismatched_header_and_tuble_when_construct_then_exception():
    # given
    header = ("a", "b", "c")
    rtuples = SortedSet([("1", "2")])

    # when
    with pytest.raises(IncompatibleOperandError) as exception:
        _ = Relation("f", header, rtuples)

    # then
    assert (
        "Error: ('1', '2') is not compatible with header ('a', 'b', 'c') in Relation.add_rtuple"
        == str(exception.value)
    )


def test_given_mismatched_relations_when_difference_then_exception():
    # given
    left = Relation("f", ("a", "b", "c"), SortedSet())
    right = Relation("f", ("a", "b"), SortedSet())

    # when
    with pytest.raises(IncompatibleOperandError) as exception:
        left.difference(right)

    # then
    assert (
        "Error: headers ('a', 'b', 'c') and ('a', 'b') are not compatible in Relation.difference"
        == str(exception.value)
    )


def test_given_matched_relations_when_difference_then_difference():
    # given
    left = Relation("f", ("a", "b", "c"), SortedSet([("1", "2", "3"), ("2", "4", "6")]))
    right = Relation("f", ("a", "b", "c"), SortedSet([("2", "4", "6")]))
    expected = Relation("f", ("a", "b", "c"), SortedSet([("1", "2", "3")]))

    # when
    answer = left.difference(right)

    # then
    assert expected == answer
