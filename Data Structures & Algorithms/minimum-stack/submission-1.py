class MinStack:

    def __init__(self):
        self.stack = list()
        self.minStack = list()

    def push(self, val: int) -> None:
        self.stack.append(val)
        minVal = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(minVal)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]        

    def getMin(self) -> int:
        return self.minStack[-1]
