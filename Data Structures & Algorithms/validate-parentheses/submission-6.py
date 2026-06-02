class Solution:
    def isValid(self, s: str) -> bool:
        if (len(s) <= 1):
            return False

        stack = []

        for i in range(len(s)):
            if (s[i] == ")" or s[i] == "}" or s[i] == "]"):
                print(f"found {s[i]}")
                if (len(stack) < 1 ):
                    return False
                print(f"stack: {stack}")
                if (stack[-1] == "(" and s[i] == ")"):
                    print(f"found pair {stack[-1]} == {s[i]} ")
                    popped = stack.pop()
                    print(f"Poped {popped}")
                    continue
                if (stack[-1] == "{" and s[i] == "}"):
                    print(f"found pair {stack[-1]} == {s[i]} a")
                    popped = stack.pop()
                    print(f"Poped {popped}")
                    continue
                if (stack[-1] == "[" and s[i] == "]"):
                    print(f"found pair {stack[-1]} == {s[i]} ")
                    popped = stack.pop()
                    print(f"Poped {popped}")
                    continue
                else:
                    return False
            elif (s[i] == "(" or s[i] == "{" or s[i] == "["):
                stack.append(s[i])
                print(f"Appending open {s[i]} to stack: {stack}")
            else:
                return False 
        if (len(stack) > 0 ):
            return False
        return True