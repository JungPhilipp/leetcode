class Solution:
    def expected(self, c: str):
        if c == ")":
            return "("
        elif c == "]":
            return "["
        elif c == "}":
            return "{"

    def isValid(self, str: str) -> bool:
        stack = []
        for c in str:
            if c == "(" or c == "[" or c == "{":
                stack.append(c)
            elif len(stack) == 0:
                return False
            else:
                if not stack.pop() == self.expected(c):
                    return False
        return len(stack) == 0
