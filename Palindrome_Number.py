'''
Given an integer x, return true if x is a palindrome and false otherwise.
'''
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            string = str(x)
            len_str = len(string)
            if (len_str > 2) and (len_str % 2 == 0):
                for i in range((len_str//2)):
                    if string[i] != string[-i-1]:
                        return False
                return True
            elif (len_str > 2) and (len_str % 2 != 0):
                for i in range((len_str//2)):
                    if string[i] != string[-i-1]:
                        return False
                return True
            elif len_str == 2:
                return string[0] == string[1]
            else:
                return True
