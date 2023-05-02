
my_text = """\
Extract of "The Zen of Python", by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
"""

with open("./testing_files/new_sample.txt", mode="w") as f:
    f.write(my_text)
