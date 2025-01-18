class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic_list = []
        for word in strs:
            word_dict = {}
            for i in range(len(word)):
                if word_dict.get(word[i]) is not None:
                    word_dict[word[i]] +=1
                else:
                    word_dict[word[i]] = 1
            dic_list.append(word_dict)

        full_list = []
        for i in range(len(dic_list)):
            inner_list = [i]
            for j in range(i+1,len(dic_list)):
                if dic_list[i].items() == dic_list[j].items():
                    inner_list.append(j)
            full_list.append(inner_list)
    
        mapped_words= []
        for lst in full_list:
            sec_inner_list = []
            sec_inner_list = [strs[pos] for pos in lst]
            mapped_words.append(sec_inner_list)
        print(mapped_words)

        for i in range(len(mapped_words) - 1, -1, -1):  # Iterate backwards
            for j in range(len(mapped_words)):
                if set(mapped_words[i]).issubset(set(mapped_words[j])) and (len(mapped_words[i]) < len(mapped_words[j])):
                    mapped_words.pop(i)
                    break 
        
        return mapped_words

        

        