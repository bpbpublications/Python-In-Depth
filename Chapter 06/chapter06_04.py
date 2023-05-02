
MAX = 10

class DoublesIterator:
    """ An iterator of integers multiples of 2 """

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index <= MAX:
            result = 2 * self.index
            self.index = self.index + 1
            return result
        else:
            raise StopIteration

if __name__ == "__main__":

    it = DoublesIterator()

    for item in it:
        print(item)
