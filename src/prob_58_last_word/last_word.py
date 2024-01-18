from curses.ascii import isspace

# Complexity simple:
#   * Runtime: O(n)
#   * Space: O(1)
# Complexity best conceivable:
#   * Runtime: O(n)
#   * Space: O(1)


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        index = len(s) - 1
        word_length = 0
        while index >= 0:
            if s[index] == ' ':
                if word_length > 0:
                    return word_length
                else:
                    index -=1
                    continue
            word_length += 1
            index -= 1

        return word_length
