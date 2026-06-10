class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        if (len(self.stack) == 0):
            return "Stack empty"
        return self.stack.pop(-1)

    def top(self) -> int:
        if (len(self.stack) == 0):
            return 0
        return self.stack[-1]

    def getMin(self) -> int:
        temp = self.stack.copy()

        topTemp = temp.pop(-1)

        while len(temp) > 0:
            if topTemp < temp[-1]:
                temp.pop()
            else: topTemp = temp.pop(-1)
        
        return topTemp