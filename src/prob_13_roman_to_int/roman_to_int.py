class Solution:
    def romanToInt(self, roman: str) -> int:
        roman += "O"
        num = 0
        roman_values = {
            "O": 0,
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        for i in range(len(roman) - 1):
            first = roman_values[roman[i]]
            next = roman_values[roman[i + 1]]
            if first < next:
                num -= first
            else:
                num += first
        return num
