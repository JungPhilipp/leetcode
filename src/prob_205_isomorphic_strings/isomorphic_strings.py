# Complexity simple:
#   * Runtime: O(n) try morph, look up O(1) with hashmap
#   * Space: O(n) two hashmaps
# Complexity best conceivable:
#   * Runtime: O(n) try morph, look up O(1) with hashmap
#   * Space: O(n) two hashmaps


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        map = dict()
        values = set()

        for src, dest in zip(s, t):
            if src not in map:
                map[src] = dest
                values.add(dest)
                continue
            if map[src] != dest:
                return False

        return len(map) == len(values)
