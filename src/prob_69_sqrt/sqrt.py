# Complexity simple:
#   * Runtime: O(log n):
#   * Space: O(1):


class Solution:
    def mySqrt(self, x: int) -> int:
        def f(x):
            return x * x

        start = 0
        end = x // 2

        steps = 0
        while True:
            fx = f(start)
            fx1 = f(start + 1)
            if fx <= x and fx1 > x:
                return start

            mid = start + max((end - start) // 2, 1)
            f_mid = f(mid)
            if f_mid == x:
                return mid
            if f(mid) < x:
                start = mid
            else:
                end = mid

            steps += 1
