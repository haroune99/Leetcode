'''
Write a function to find the longest common prefix string amongst an array of strings
'''
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        length = float(inf)
        index = None
        letters = []
        max_pref = None
        for i in range(len(strs)):
            if len(strs[i]) < length:
                length = len(strs[i])
                index = i

        shortest = strs[index]

        for letter in strs[index]:
            letters.append(letter)
        
        for i in range(length):
            for word in strs:
                if word[i] != letters[i]:
                    return shortest[:i]

        return shortest


        
        
         
    

