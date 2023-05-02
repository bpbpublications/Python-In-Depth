
from pathlib import Path

with Path("./testing_files/sample1.txt").open(mode="r") as f:
    print("Sample 1")
    print(f.read())