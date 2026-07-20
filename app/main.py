"""Very small Python application for the GH-600 educational repository.

Why this file exists:
- It provides the smallest possible executable application artifact in the repo.
- It gives workflows, prompts, reviewers, and tests a concrete code sample.

GH-600 concept demonstrated:
- Agents need a simple codebase target so surrounding artifacts have context.

Real-project usage:
- A real application would hold business logic here instead of a hello-world message.
"""


def get_message() -> str:
    """Return the educational greeting used throughout the repository."""
    return "Hello GH-600"


def main() -> None:
    """Print the repository greeting for local runs and workflow demonstrations."""
    print(get_message())


if __name__ == "__main__":
    main()
