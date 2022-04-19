class Solution:
    def isPalindrome(self, num: int) -> bool:
        if num < 0:
            return False
        num_string = str(num)
        front = 0
        back = len(num_string) - 1
        while front <= back:
            print(front, back)
            if num_string[front] != num_string[back]:
                return False
            front += 1
            back -= 1
        return True
