#Working on Part 6.
class PeekableIterator:
    def __init__(self, iterable):
        self.iterator = iter(iterable)
        self.peeked = None
        self.has_peeked = False

    def __iter__(self):
        return self

    def __next__(self):
        if self.has_peeked:
            result = self.peeked
            self.has_peeked = False
            self.peeked = None
            return result
        return next(self.iterator)

    def peek(self):
        if not self.has_peeked:
            try:
                self.peeked = next(self.iterator)
                self.has_peeked = True
            except StopIteration:
                return None
        return self.peeked

    def has_next(self):
        if self.has_peeked:
            return True
        try:
            self.peek()
            return True
        except StopIteration:
            return False

# Example usage and testing
if __name__ == "__main__":
    # Test with a list
    test_list = [1, 2, 3, 4, 5]
    peekable = PeekableIterator(test_list)

    print("Peek:", peekable.peek())  # Should print: Peek: 1
    print("Next:", next(peekable))   # Should print: Next: 1
    print("Next:", next(peekable))   # Should print: Next: 2
    print("Peek:", peekable.peek())  # Should print: Peek: 3
    print("Peek:", peekable.peek())  # Should print: Peek: 3 (demonstrating multiple peeks)
    print("Next:", next(peekable))   # Should print: Next: 3
    print("Has next:", peekable.has_next())  # Should print: Has next: True
    print("Next:", next(peekable))   # Should print: Next: 4
    print("Next:", next(peekable))   # Should print: Next: 5
    print("Has next:", peekable.has_next())  # Should print: Has next: False

    try:
        print("Next:", next(peekable))  # Should raise StopIteration
    except StopIteration:
        print("Iterator exhausted")