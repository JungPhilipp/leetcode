class Solution:
    def isPalindromeSimple(self, num: int) -> bool:
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

    def isPalindrome(self, num: int) -> bool:
        if num < 0 or (num > 0 and num % 10 == 0):
            return False

        reversed_num = 0
        while num > reversed_num:
            reversed_num = reversed_num * 10 + num % 10
            num //= 10
        return bool(num == reversed_num or num == reversed_num // 10)


# Simple Solution:
# O(n) for int to string conversion + O(n) to check all digits -> Overall O(n)
# Cannot improve asymptotic time complexity because all digits need to be checked to be sure
# O(n) memory, because of copied string (n being the number of digits)

# Improved Solution:
# Use mod to access digits instead of string conversion.
