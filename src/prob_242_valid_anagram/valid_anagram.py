# Complexity simple:
#   * Runtime: O(n)
#   * Space: O(m) m = different letters
# Complexity best conceivable:
#   * Runtime: O(n)
#   * Space: O(1)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter = [0] * 256
        for letter in s:
             counter[ord(letter)] +=1

        for letter in t:
            counter[ord(letter)] -=1

        return all(count == 0 for count in counter)
