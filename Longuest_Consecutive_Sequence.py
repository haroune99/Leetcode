class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) ==0:
            return 0
        elif len(nums) ==1:
            return 1
        else:
            sorted_nums = sorted(nums)
            runs = []
            for i in range(1,(len(sorted_nums))):
                runs.append(sorted_nums[i]-sorted_nums[i-1])

            cs = []
            c = 0
            for j in range(len(runs)):
                while (j < len(runs)) and (runs[j] == 1):
                    c+=1
                    j+=1
                cs.append(c+1)
                c=0
            
            return max(cs)

        
