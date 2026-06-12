class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for char in tokens:
            if char == "+":
                pop = stack.pop(-1)
                stack[-1] = str(int(stack[-1]) + int(pop))
                continue
            if char == "-":
                pop = stack.pop(-1)
                stack[-1] = str(int(stack[-1]) - int(pop))
                continue
            if char == "*":
                pop = stack.pop(-1)
                stack[-1] = str(int(stack[-1]) * int(pop))
                continue
            if char == "/":
                pop = stack.pop(-1)
                stack[-1] = str(int(int(stack[-1]) / int(pop)))
                continue
            stack.append(char)

        return int(stack[-1])