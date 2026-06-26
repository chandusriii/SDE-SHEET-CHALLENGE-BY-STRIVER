
class ArrayStack:

    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        if self.isEmpty():
            return -1
        return self.stack.pop()

    def top(self):
        if self.isEmpty():
            return -1
        return self.stack[-1]

    def isEmpty(self):
        return len(self.stack) == 0


# Example Usage
if __name__ == "__main__":
    stack = ArrayStack()

    stack.push(5)
    stack.push(10)

    print("Top:", stack.top())      # 10
    print("Pop:", stack.pop())      # 10
    print("Is Empty:", stack.isEmpty())  # False
