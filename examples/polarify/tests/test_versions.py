import polars
import sys

def test_versions():
    print("") # empty line
    print(f"Polars version: {polars.__version__}")
    print(f"Python version: {sys.version}")
