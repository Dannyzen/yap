# Contributing to Fast Voice-to-Text

First off, thank you for considering contributing to Fast Voice-to-Text! It's people like you that make Fast Voice-to-Text such a great tool.

## Code of Conduct

This project advocates for a welcoming and inclusive environment. Please treat everyone with respect and follow the standard code of conduct.

## How Can I Contribute?

### Reporting Bugs

- **Ensure the bug was not already reported** by searching on GitHub under [Issues](https://github.com/fast-voice/issues).
- If you're unable to find an open issue addressing the problem, [open a new one](https://github.com/fast-voice/issues/new). Be sure to include a **title and clear description**, as much relevant information as possible, and a **code sample** or an **executable test case** demonstrating the expected behavior that is not occurring.

### Suggesting Enhancements

- Open a new issue with a clear title and detailed description of the suggested enhancement.
- Explain why this enhancement would be useful to most Fast Voice-to-Text users.

### Pull Requests

1. Fork the repo and create your branch from `main`.
2. If you've added code that should be tested, add tests.
3. If you've changed APIs, update the documentation.
4. Ensure the test suite passes.
5. Make sure your code lints.
6. Issue that pull request!

## Style Guide

We follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) for Python code.

- Use 4 spaces for indentation.
- Limit line length to 88 characters (Black style).
- Use distinct, descriptive variable names.
- Type hints are encouraged for all public interfaces.

## Development Setup

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/fast-voice.git
    cd fast-voice
    ```

2.  **Install dependencies**:
    We use `uv` for dependency management.
    ```bash
    uv pip install -e .
    ```

3.  **Run Tests**:
    ```bash
    uv run python -m unittest discover tests
    ```

## Commit Messages

- Use the present tense ("Add feature" not "Added feature").
- Use the imperative mood ("Move cursor to..." not "Moves cursor to...").
- Limit the first line to 72 characters or less.
- Reference issues and pull requests liberally after the first line.

## License

By contributing, you agree that your contributions will be licensed under its MIT License.
