
class Solution:
    def insert(self, stack, x):
        if not stack or stack[-1] <= x:
            stack.append(x)
            return

        temp = stack.pop()
        self.insert(stack, x)
        stack.append(temp)

    def sortStack(self, stack):
        if len(stack) <= 1:
            return stack

        temp = stack.pop()
        self.sortStack(stack)
        self.insert(stack, temp)
        return stack
