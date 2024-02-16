# Complexity simple:
#   * Runtime: O(n):
#   * Space: O(n): return


class Solution:
    def mySqrt(self, x: int) -> int:
        s = x // 2
        while True:
            s2 = s * s
            sp1 = (s + 1) * (s + 1)
            if s2 <= x and sp1 > x:
                return s
            if s2 < x:
                s = (s + 1) * 2
            else:
                s = s // 2
