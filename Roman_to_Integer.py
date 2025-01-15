'''
Given a roman numeral, convert it to an integer.
'''
class Solution:
    def romanToInt(self, s: str) -> int:
        patterns = {'IV': 4,
        'IX': 9,
        'XL': 40,
        'XC': 90,
        'CD': 400,
        'CM': 900}
        initials = {'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000}
        pairs = []
        value = 0
        length = len(s)
        for i in range(0,length):
            pair = s[i:i+2]
            pairs.append(pair)
        for item in pairs:
            if item in patterns:
                value += patterns[item]
                s = s.replace(item,"")
        for crc in s:
            if crc in initials:
                value += initials[crc]

        return value        

        

        

