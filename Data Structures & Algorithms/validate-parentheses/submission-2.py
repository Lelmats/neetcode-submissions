class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        map = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }

        for string in s:
            if string in map:
                if stack and map[string] == stack[-1]:
                    stack.pop()     
                else:
                    return False     
            else:
                stack.append(string)
            print(stack)
        
        return True if len(stack) == 0 else False