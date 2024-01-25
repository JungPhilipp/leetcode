# Complexity simple:
#   * Runtime: O(n)
#   * Space: O(m) m = different letters
# Complexity best conceivable:
#   * Runtime: O(n)
#   * Space: O(1)


from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
