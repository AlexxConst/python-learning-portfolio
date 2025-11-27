Simple CLI Calculator
Small command-line calculator demonstrating modular design, error handling and unit tests.

Features

Pure function calculate(a, op, b) implementing basic arithmetic (+, -, *, /).
CLI wrapper (cli()) for interactive usage.
Unit tests (pytest) covering normal and error cases.
Ready for CI.

Quick start
Run the CLI:
python3 python_doc/calculator.py

Run tests:
pytest -q

Example

Input:
Enter first number: 2
Enter operator (+, -, *, /): *
Enter second number: 3

Output:
Result: 6.0

Project structure
.
├─ python_doc/
│  ├─ calculator.py
│  └─ test_calculate.py
├─ README.md
└─ LICENSE

Notes for reviewers

calculate() is a pure function and is the main public API.
CI (GitHub Actions) runs pytest on push and PRs.
License
This project is available under the MIT License — see LICENSE.
