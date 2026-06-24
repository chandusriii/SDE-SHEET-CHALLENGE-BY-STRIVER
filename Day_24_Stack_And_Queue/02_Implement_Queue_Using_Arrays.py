class ArrayQueue:

    def __init__(self):
        self.queue = []
        self.front = 0

    def push(self, x):
        self.queue.append(x)

    def pop(self):
        if self.isEmpty():
            return -1

        val = self.queue[self.front]
        self.front += 1
        return val

    def peek(self):
        if self.isEmpty():
            return -1

        return self.queue[self.front]

    def isEmpty(self):
        return self.front >= len(self.queue)


# Example Usage
if __name__ == "__main__":
    queue = ArrayQueue()

    queue.push(5)
    queue.push(10)

    print("Peek:", queue.peek())        # 5
    print("Pop:", queue.pop())          # 5
    print("Is Empty:", queue.isEmpty()) # False
