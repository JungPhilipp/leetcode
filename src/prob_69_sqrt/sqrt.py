# Complexity simple:
#   * Runtime: O(log n):
#   * Space: O(1):


class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
             return x
        def f(s):
            return s * s - x

        xn = x // 2
        f_last = x

        while True:
            f_xn = f(xn)
            if f_last >= 0 and f_xn <= 0:
                return xn

            f_xn1 = f(xn + 1)
            f_deriv = f_xn1 - f_xn

            xn -= max(f_xn // f_deriv, 1)
            f_last = f_xn
