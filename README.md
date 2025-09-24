# Project 3

This project uses the `lexer` and `parser` functions from Project 1 and Project 2 to get an instance of a `DatalogProgram` that must then be interpreted to answer its queries. Project 3 must
  1. Create a relation for each named scheme in the Datalog program.
  1. Add each fact in the Datalog program to the appropriate relation.
  1. Evaluate each query in the Datalog program and return the answers to each one.
[QUERIES_INTERP.md](docs/QUERIES_INTERP.md) explains each of these steps in detail.

**There is no rule evaluation for project 3.** Anything related to evaluating rules, including the natural join of two relations, is **not a part of project 3.**

The interpreter **must be implemented with relational algebra.** No exceptions. Specifically, project, rename, and select along with union, intersection, and difference as appropriate.

**Summary of Documentation**

- [README.md](README.md): describes project logistics
- [QUERIES_INTERP.md](docs/QUERIES_INTERP.md): describes how to interpret queries in Datalog program
- [CODE.md](docs/CODE.md): describes the starter code
- [Relational Algebra Operations Examples](ddocs/Relational_algebra_operations_example.ipynb) (Jupyter Notebook)
- Lecture notes in [learningsuite.byu.edu](https://learningsuite.byu.edu) and specifically the slides in the lecture _Relational Operators and Project 3_.

**You are strongly encouraged to review the above documentation _before_ proceeding further**.

## Table of Contents
- [Developer Setup](#developer-setup)
- [Project Requirements](#project-requirements)
- [AI Policy for Project 3](#ai-policy-for-project-3)
- [Unit Tests](#unit-tests)
- [Integration Tests (pass-off)](#integration-tests-pass-off)
- [Code Quality](#code-quality)
- [Submission And Grading](#submission-and-grading)
- [Best Practices](#best-practices)

## Developer Setup

The `vscode` extensions for developing Project 3 are already installed as part of Project 0. You should not need to install any new extensions. You do need to set up the project locally on your machine. The below steps outline the process that is similar to what you did in Project 2 ony with additional files to copy over.

1. Clone the repository to your machine. Accepting the Project 3 assignment on GitHub classroom creates a repository for your submission. You need to clone that repository to your machine. Copy the URL generated after accepting the assignment and in a terminal on your machine in a sensible location. From an integrated terminal, type `git clone \<URL\>` where `\<URL\>` is the one you copied. Or open a new vscode window, select _Clone Git Repository_, and paste the URL you copied. If you followed the URL to GitHub, then you can recopy the URL using the "<> Code ▼" button.
1. Create and activate a virtual environment in the project directory.  Revisit Project 0 for a reminder on how to create the virtual environment. There is also a _cheat sheet_ at [learningsuite.byu.edu](https://learningsuite.byu.edu) _Content_ &rarr; _Projects_ &rarr; _Projects Cheat Sheet_.
1. Install the project package. **Be sure your virtual environment is active before installing the package!** In a terminal in the virtual environment in the project directory do: `pip install --editable ".[dev]"`. Use `pip3` instead of `pip` if your system requires it.
1. Verify the package installation. From the terminal in which you activated the virtual environment and installed the project package, type `project1` and hit enter. You should see the below output.
    ```
    $ project3
    usage: project3 <input file>
    ```
1. Install `pre-commit` for the project. **Be sure your virtual environment is active before installing pre-commit!**. In a terminal in the virtual environment in the project directory do: `pre-commit install`
1. Verify the `pre-commit` installation. From the terminal in which you installed `pre-commit`, type `pre-commit run --all-files` and hit enter. You should see something like the below at the end of the setup output:
    ```
    $ pre-commit run --all-files
    trim trailing whitespace.................................................Passed
    fix end of files.........................................................Passed
    check yaml...............................................................Passed
    check for added large files..............................................Passed
    CRLF end-lines remover...................................................Passed
    Tabs remover.............................................................Passed
    ruff.....................................................................Passed
    ruff-format..............................................................Passed
    mypy.....................................................................Passed
    ```
1. Verify that tests are ready to run. Open the _Testing Pane_ in VS Code by clicking on the test tube icon. If you see
    ```
    pytest Discovery Error [project-3]
    ```
    then you must open the _Command Palette_ from the _View_ menu, choose `Python: Select Interpreter`, and choose the interpreter for the virtual environment (probably `Python 3.12.5 (.venv)`).
1. **IMPORTANT**: Copy the below files from your solution to Project 2 into the `src/project3/` folder:
    * `datalogprogram.py`
    * `fsm.py`
    * `lexer.py`
    * `parser.py`
The `token.py` file is unchanged here and should not be copied over. None of test files from Project 2 should be copied over either.

## Project Requirements

1. The project must be completed individually -- there is no group work.
1. Project pass-off is on GitHub. You will commit your final solution to the `master` branch of your local repository and then push that commit to GitHub. Multiple commits, and pushes, are allowed. A push triggers a GitHub action that is the auto-grader for pass-off. The TAs look at both the result of the auto-grader on GitHub and your code to determine your final score. Projects that use iteration instead of tail recursion will not be accepted.
1. You must pass all integration tests up to, and including, `tests/test_passoff_80.py` to move on to the next project. Bucket 80 is the minimum functionality to complete the course.
1. You must **_"do the math"_** to write positive and negative tests in `tests/test_relation.py` for the following functions in the `Relation` class in `src/project3/relation.py`. AI may be used to generate the code for the tests once you **_"do the math"_** for the for the inputs and outputs and write a few examples for the AI to follow using your inputs and outputs. See [AI Policy for Project 3](#ai-policy-for-project-3) for details.
    - `intersection` (easy),
    - `project` (hard),
    - `rename` (super easy),
    - `reorder` (hard)
    - `select_eq_col` (moderate),
    - `select_eq_lit` (moderate), and
    - `union` (easy).
1. You must implement the following functions in the `Relation` class in `src/project3/relation.py`:
    - `intersection` (easy),
    - `project` (hard),
    - `rename` (super easy),
    - `reorder` (hard)
    - `select_eq_col` (moderate),
    - `select_eq_lit` (moderate), and
    - `union` (easy).
1. You must add to the `Interpreter` class in `src/project3/interpreter.py` attributes to represent, or implement, a relational database. A relational database is just a named collection of relations (see [QUERIES_INTERP.md](docs/QUERIES_INTERP.md))
1. You must interpret a Datalog program with relational algebra by implementing the following in the `Interpreter` class in `src/project3/interpreter.py`. The other functions will be implemented is later projects. See [QUERIES_INTERP.md](docs/QUERIES_INTERP.md) for details on each of the required to implement function as well as the docstrings defined for those functions. You are encouraged to **_"do the math"_** and write positive for the required to implement functions.
    - `eval_schemes`
    - `eval_facts`
    - `eval_queries`
1. Your code must not report any issues with the following code quality tool run in the integrated `vscode` terminal from the root of the project directory: `pre-commit run --all-files`. This tool includes _type checking_ so your solution requires type annotations.

Consider using a branch as you work on your submission so that you can `commit` your work from time to time. Once everything is working, and the auto-grader tests are passing, then you can `merge` your work into your master branch and push it to your GitHub repository. Ask your favorite AI for help learning how to use Git branches for feature development.

## AI Policy for Project 3

Project 3 code is very algorithmic and specific to interpreting Datalog. It does not include repeated code with similar structure that AI can learn, adapt, and repeat. As such, you are expected to write all the implementation code in the `Relation` class and `Interpreter` class without AI assist.

AI may be used to help generate code for the positive and negative tests for the functions in the `Relation` class with the exception that you must **_"Do the math"_** to figure out the input and expected output for each of the tests and only use AI to generate the code to implement the tests. We recommend that after you **_"Do the math"_**, you write the code for the negative and positive test for one of the operators. Then use that code, with your already computed input and output values for the other tests, to prompt the AI to generate the code for the remaining tests.

All the tests should appear in `tests/test_relation.py`.

## Unit Tests

Similar to Project 2, you are required to "_do the math_" to write positive and negative unit tests for all of the relational algebra operators. The `tests/test_relation.py` file already includes some tests related to the starter code as starting point for positive

See the [AI Policy for Project 3](#ai-policy-for-project-3) for instructions on when to use and not use AI in generating tests.

## Integration Tests (pass-off)

**The pass-off test structure has changed.** All the primary tests are in a single file: `tests/test-passoff.py`. Running individual tests is the same using either `pytest` directly or the testing pane in vscode (**recommended**). As before, the `xx` on each bucket denotes the available points for passing the tests in that bucket. The value of each test in each bucket is uniform: _points-for-bucket/number-of-tests-in-bucket_. Bucket 80 is the minimum requirement to pass the course.

## Code Quality

Pre-commit must run on all the files and report no errors.

## Submission and Grading

The minimum standard for this project is **bucket 80**. That means that if all the tests pass in all buckets up to and including bucket 80, then the next project can be started safely. You can run each bucket from the testing pane or with `pytest` on the command line. Passing everything up to and including `test_passoff_80.py` is the minimum requirement to move on to the next project.

Submit Project 2 for grading by doing the following:

  * Commit your solution on the master branch
  * Push the commit to GitHub -- that should trigger the auto-grader
  * Goto [learningsuite.byu.edu](https://learningsuite.byu.edu) at _Assignments_ &rarr; _Projects_ &rarr; _Project 2_ to submit the following:
    1. Your GitHub ID and Project 2 URL for grading.
    1. A short paragraph outlining (a) how you prompted the AI to generate any code (if you used it) and (b) how you determined the quality and correctness of that code.
    1. A screen shot showing no issues with `pre-commit run --all-files`.
  * Confirm on the GitHub Actions pane that the pass-off tests passed, or alternatively, goto the Project 1 URL, find the green checkmark or red x, and click it to confirm the auto-grader score matches the pass-off results from your system.

### Paragraph on AI

Guidelines for answering

_"A short paragraph outlining (a) how you prompted the AI to generate any code (if you used it) and (b) how you determined the quality and correctness of that code."_

These guidelines give examples from Project 1.

* Brief means no more than 500 words.
* Be specific about what code was generated. _"AI generated FSM code for the following non-terminals: `facts`, etc."_
* Be general about the final form of the prompts used to generate the code and any prompt iteration that was required. _"I gave the AI example code and asked it to create code that matched the pattern, and style, in that example code. I had to revise the prompt to specifically ask it to not generalize an FSM to detect a supplied string."_
* Be specific about how you determined the quality and correctness of generated code. _"A manual visual inspection was sufficient to determine quality and correctness because the generated code was trivial. I also ran the code quality tools on the generated code as a second level check."_
* Be specific about where else AI was leveraged. _"I used AI to breakdown and explain the pseudo-code for the `lexer` algorithm as well as the `FiniteStateMachine` class. AI also provided test inputs for my `STRING` FSM to help debug the apostrophe escape sequence."_
* Be specific about how you used AI to write tests, and how you generated the parse trees necessary for writing tests based on the math.

## Best Practices

Here is the suggested order for Project 3:

1. Read the code and order in your mind what has been provided, how it works, and what you need to implement -- **don't skip this step**.
1. For each required function in `Relation`:

    1. Write a negative test that fails.
    1. Write code to pass the negative test.
    1. Write a positive test that fails.
    1. Write code to pass the positive test.

1. For each required function in `Interpreter`:

    1. Write a positive test that fails.
    1. Write code to pass the positive test.

1. Run the pass-off tests -- debug as needed.


### Branches

Consider using a branch as you work on your submission so that you can `commit` your work from time to time. Once everything is working, and the auto-grader tests are passing, then you can `merge` your work into your master branch and push it to your GitHub repository. Ask your favorite search engine or LLM for help learning how to use Git feature branches.
