from typing import List

#   * Runtime: O(n): n = number of digits
#   * Space: O(n): output

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        result = []
        for i in reversed(digits):
            sum = i + carry
            if sum >= 10:
                carry = sum // 10
                sum %= 10
            else:
                carry = 0
            result.append(sum)

        if carry > 0:
            result.append(carry)
        return result[::-1]
