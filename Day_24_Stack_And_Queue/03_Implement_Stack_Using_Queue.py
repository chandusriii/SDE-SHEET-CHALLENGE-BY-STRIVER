from collections import deque

class QueueStack:

    def __init__(self):
        self.q = deque()

    def push(self, x):
        self.q.append(x)

        # Rotate queue so the new element comes to the front
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self):
        if self.isEmpty():
            return -1
        return self.q.popleft()

    def top(self):
        if self.isEmpty():
            return -1
        return self.q[0]

    def isEmpty(self):
        return len(self.q) == 0


# Example Usage
if __name__ == "__main__":
    stack = QueueStack()

    stack.push(4)
    stack.push(8)

    print("Top:", stack.top())          # 8
    print("Pop:", stack.pop())          # 8
    print("Is Empty:", stack.isEmpty()) # False
