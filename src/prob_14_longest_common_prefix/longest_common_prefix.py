from operator import pos
from typing import List


class Solution:
    def longestCommonPrefix(self, strings: List[str]) -> str:
        if len(strings) == 0:
            return ""
        pos_in_str = 0
        while True:
            for str in strings:
                if pos_in_str >= len(str) or str[pos_in_str] != strings[0][pos_in_str]:
                    return strings[0][:pos_in_str]
            pos_in_str += 1
