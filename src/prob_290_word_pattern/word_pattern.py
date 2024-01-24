from math import log
import sys
from typing import List, Optional

# Complexity simple:
#   * Runtime: O(n)
#   * Space: O(m) m = different letters/words in pattern/s
# Complexity best conceivable:
#   * Runtime: O(n)
#   * Space: O(1)


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(words) != len(pattern):
            return False

        map = dict()
        inverse = dict()

        for letter, word in zip(pattern, words):
            if letter not in map:
                map[letter] = word
                inverse[word] = letter
                continue
            if map[letter] != word:
                return False

        return len(map) == len(inverse)

