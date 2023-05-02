
from pathlib import Path

my_text = """\
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
"""

filepath = "./testing_files/new_sample.txt"
with Path(filepath).open(mode="w") as f:
    f.write(my_text)
