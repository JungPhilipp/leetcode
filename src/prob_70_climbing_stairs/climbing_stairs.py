from functools import lru_cache

# Almost the same as fib() just differs in starting conditions (0, 1, 2) vs (0, 1, 1)


#   * Runtime: O(2**n): fibonacci
#   * Space: O(n): stack space for recursion
class SolutionRecursive:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)


#   * Runtime: O(n): Use cache to compute fib(n) for each n only once
#   * Space: O(n): cache
class SolutionDynamic:
    @lru_cache(maxsize=None)
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)

#   * Runtime: O(n): Use cache to compute fib(n) for each n only once
#   * Space: O(1): cache
class SolutionDynamicSpace:
    def climbStairs(self, n: int) -> int:
        current = 0
        previous = 1
        pre_previous = 0
        for _ in range(n):
            current = previous + pre_previous
            pre_previous = previous
            previous = current

        return current

#   * Runtime: O(1):
#   * Space: O(1):
class SolutionClosedForm:
    phi = 1.618033988749895
    sqrt_5 = 2.23606797749979
    def climbStairs(self, n: int) -> int:
        return round(pow(self.phi, n + 1)/ self.sqrt_5)

Solution = SolutionClosedForm
