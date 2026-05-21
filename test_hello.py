import subprocess
import sys


def test_hello_world():
    result = subprocess.run(
        [sys.executable, "hello.py"],
        capture_output=True,
        text=True
    )
    assert result.returncode == 0
    assert result.stdout.strip() == "Hello, World!"


if __name__ == "__main__":
    test_hello_world()
    print("All tests passed.")
