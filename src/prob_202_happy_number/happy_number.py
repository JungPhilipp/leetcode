class Solution:
    def isHappy(self, n: int) -> bool:
        cache = set()
        while True:
            if n == 1:
                return True
            if n in cache:
                return False
            cache.add(n)
            n = sum([int(i) ** 2 for i in str(n)])


