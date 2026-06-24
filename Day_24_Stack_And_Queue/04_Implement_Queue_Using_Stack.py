class StackQueue:

    def __init__(self):
        self.s1 = []  # Input stack
        self.s2 = []  # Output stack

    def push(self, x):
        self.s1.append(x)

    def pop(self):
        if self.isEmpty():
            return -1

        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())

        return self.s2.pop()

    def peek(self):
        if self.isEmpty():
            return -1

        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())

        return self.s2[-1]

    def isEmpty(self):
        return len(self.s1) == 0 and len(self.s2) == 0


# Example Usage
if __name__ == "__main__":
    queue = StackQueue()

    queue.push(4)
    queue.push(8)

    print("Peek:", queue.peek())        # 4
    print("Pop:", queue.pop())          # 4
    print("Is Empty:", queue.isEmpty()) # False
