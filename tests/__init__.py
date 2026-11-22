"""Test package. Ensures the repo root is importable (so `from tools import ...` works)
regardless of how unittest is invoked."""
import os
import sys

_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if _ROOT not in sys.path:
    sys.path.insert(0, _ROOT)
