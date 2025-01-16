class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        word_one_dict = {}
        word_two_dict = {}

        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            if word_one_dict.get(s[i]) is not None:
                word_one_dict[s[i]] +=1
            else:
                word_one_dict[s[i]] = 1
        
        for i in range(len(t)):
            if word_two_dict.get(t[i]) is not None:
                word_two_dict[t[i]] +=1
            else:
                word_two_dict[t[i]] = 1

        if word_one_dict.items() != word_two_dict.items():
                return False
        
        return True
