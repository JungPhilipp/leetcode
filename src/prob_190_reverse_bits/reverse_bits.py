#   * Runtime: O(1):
#   * Space: O(1):
class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for i in reversed(range(32)):
            result |= (n & 1) << (i)
            n >>= 1
        return result
