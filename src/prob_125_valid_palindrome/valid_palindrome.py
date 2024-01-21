# Complexity simple:
#   * Runtime: O(n)
#   * Space: O(1)
# Complexity best conceivable:
#   * Runtime: O(n)
#   * Space: O(1)


class Solution:
    def isPalindrome(self, s: str) -> bool:
        front = 0
        back = len(s) - 1
        while front < back:
            if not s[front].isalnum():
                front += 1
                continue
            elif not s[back].isalnum():
                back -= 1
                continue
            if s[front].lower() != s[back].lower():
                return False
            front += 1
            back -= 1

        return True
