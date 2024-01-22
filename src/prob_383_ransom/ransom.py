# Complexity simple:
#   * Runtime: O(n^2) check the entire magazine for each letter
#   * Space: O(1)
# Complexity best conceivable:
#   * Runtime: O(n + m) Insert into hashmap (letter -> count), check each letter
#   * Space: O(1)


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letters = dict()
        for letter in magazine:
            letters[letter] = letters.get(letter, 0) + 1

        for letter in ransomNote:
            if not letter in letters:
                return False
            if letters[letter] <= 0:
                return False
            letters[letter] -= 1

        return True
