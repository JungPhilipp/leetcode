

# Complexity simple:
#   * Runtime: O(n^2) For each start position check if needle is next word (could be n log)
#   * Space: O(1)
# Complexity best conceivable:
#   * Runtime: O(n) look at every element only once
#   * Space: O(1) only constant number of variables


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for index, _ in enumerate(haystack):
            if haystack[index:index+len(needle)] == needle:
                return index
        return -1
