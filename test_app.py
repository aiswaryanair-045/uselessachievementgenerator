import subprocess
import sys
import unittest


class FlaskAppWebTest(unittest.TestCase):
    def test_app_imports_and_exposes_flask_app(self):
        result = subprocess.run(
            [
                sys.executable,
                "-c",
                "from app import app; print(type(app).__name__)",
            ],
            capture_output=True,
            text=True,
            timeout=10,
        )

        self.assertEqual(result.returncode, 0, msg=result.stderr)
        self.assertIn("Flask", result.stdout)


if __name__ == "__main__":
    unittest.main()
