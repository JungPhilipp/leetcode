# Complexity simple:
#   * Runtime: O(n^2) For each start position check if needle is next word (could be n log)
#   * Space: O(1)
# Complexity best conceivable:
#   * Runtime: O(n) look at every element only once
#   * Space: O(n) only constant number of variables


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        stack = []
        for index, c in enumerate(haystack):
            stack2 = []
            for start in stack:
                sub_index = index - start
                if sub_index == len(needle):
                    return start
                if c == needle[sub_index]:
                    stack2.append(start)
            if c == needle[0]:
                stack2.append((index))
            stack[:] = stack2

        if len(stack) == 0:
            return -1
        for start in stack:
            if len(haystack) - start == len(needle):
                return start
        return -1
