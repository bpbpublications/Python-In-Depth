
import tracemalloc
tracemalloc.start()

FILENAME = "./testing_files/Anne-Frank-The-Diary-Of-A-Young-Girl.txt"
with open(FILENAME) as f:
    for line in f:
        split_line = line.split()
        for i in split_line:
            if 13 <= len(i) <= 18:
                print(i)

print("---")

snapshot = tracemalloc.take_snapshot()
for stat in snapshot.statistics('lineno')[:4]:
    print(stat)
