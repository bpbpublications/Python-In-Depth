
import tracemalloc
tracemalloc.start()


# note: Python manages memory using reference counting semantics. Once an object is not referenced anymore, its memory is deallocated. But as long as there is a reference, the object will not be deallocated. Things like cyclical references can bite you pretty hard.

# https://docs.python.org/dev/library/sys.html#sys.getsizeof
# https://code.tutsplus.com/tutorials/understand-how-much-memory-your-python-objects-use--cms-25609

def get_unique_big_words(filename):

    with open(filename) as f:
        for line in f:
            line_res = set(line.lower().split())
            for i in line_res:
                if len(i) <= 12:
                    continue
                yield i


if __name__ == "__main__":

    FILENAME = "./testing_files/Anne-Frank-The-Diary-Of-A-Young-Girl.txt"

    res = get_unique_big_words(FILENAME)
    for i in res:
        print(i)

    print("-----")

    snapshot = tracemalloc.take_snapshot()
    for stat in snapshot.statistics('lineno')[:10]:
        print(stat)