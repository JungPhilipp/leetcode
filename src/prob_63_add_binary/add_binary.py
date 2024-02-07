from itertools import zip_longest


#   * Runtime: O(1):
#   * Space: O(1):
class SolutionConvert:
    def addBinary(self, a: str, b: str) -> str:
        return format(int(a, 2) + int(b, 2), "b")


class SolutionString:
    def addBinary(self, a: str, b: str) -> str:
        result = ""
        carry = 0
        for x, y in zip_longest(reversed(a), reversed(b), fillvalue="0"):
            if x == "1" and y == "1":
                carry += 2
            elif x == "1" or y == "1":
                carry += 1
            else:
                carry += 0

            if carry == 3:
                result += "1"
                carry = 1
            elif carry == 2:
                result += "0"
                carry = 1
            elif carry == 1:
                result += "1"
                carry = 0
            else:
                result += "0"
                carry = 0

        if carry == 1:
            result += "1"

        return result[::-1]


Solution = SolutionString
