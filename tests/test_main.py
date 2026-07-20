"""Unit tests for the GH-600 hello-world application.

Why this file exists:
- It demonstrates the minimum viable automated test artifact.
- It gives GitHub Actions and agent reviewers a concrete validation target.

GH-600 concept demonstrated:
- Even educational repositories should show how tests validate agent-generated code.

Real-project usage:
- Production tests would expand to cover edge cases, failures, and integrations.
"""

from contextlib import redirect_stdout
from io import StringIO
import unittest

from app.main import get_message, main


class MainTests(unittest.TestCase):
    """Validate the tiny sample application behavior."""

    def test_get_message_returns_expected_greeting(self) -> None:
        self.assertEqual(get_message(), "Hello GH-600")

    def test_main_prints_expected_greeting(self) -> None:
        buffer = StringIO()
        with redirect_stdout(buffer):
            main()
        self.assertEqual(buffer.getvalue().strip(), "Hello GH-600")


if __name__ == "__main__":
    unittest.main()
