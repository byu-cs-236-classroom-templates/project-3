# type: ignore
import pytest
import os
from project3.project3 import project3 as compute

_TEST_ROOT_DIR = "./tests/resources/project3-passoff/"


def _get_inputs(input_file: str, answer_file: str) -> tuple[str, str]:
    input = ""
    with open(input_file, "r") as f:
        input = f.read()
    answer = ""
    with open(answer_file, "r") as f:
        answer = f.read()
    return input, answer


@pytest.mark.bucket_80
@pytest.mark.parametrize(
    argnames="input_file, expected_file",
    argvalues=[
        ("input0.txt", "answer0.txt"),
        ("input1.txt", "answer1.txt"),
        ("input2.txt", "answer2.txt"),
        ("input3.txt", "answer3.txt"),
        ("input4.txt", "answer4.txt"),
        ("input7.txt", "answer7.txt"),
        ("input8.txt", "answer8.txt"),
    ],
    ids=[
        "input0",
        "input1",
        "input2",
        "input3",
        "input4",
        "input7",
        "input8",
    ],
)
def test_bucket_80(input_file, expected_file):
    # given
    test_dir = _TEST_ROOT_DIR + "80"
    input, expected = _get_inputs(
        os.path.join(test_dir, input_file), os.path.join(test_dir, expected_file)
    )

    # when
    answer = compute(input)

    # then
    assert expected.rstrip() == answer.rstrip()


@pytest.mark.bucket_100
@pytest.mark.parametrize(
    argnames="input_file, expected_file",
    argvalues=[
        ("input5.txt", "answer5.txt"),
        ("input6.txt", "answer6.txt"),
        ("input9.txt", "answer9.txt"),
    ],
    ids=["input5", "input6", "input9"],
)
def test_bucket_100(input_file, expected_file):
    # given
    test_dir = _TEST_ROOT_DIR + "80"
    input, expected = _get_inputs(
        os.path.join(test_dir, input_file), os.path.join(test_dir, expected_file)
    )

    # when
    answer = compute(input)

    # then
    assert expected.rstrip() == answer.rstrip()
