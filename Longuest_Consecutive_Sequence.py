class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums.count(0) > 1:
            first_index = nums.index(0)
            nums = [value for i, value in enumerate(nums) if value != 0 or i == first_index]

        for i in range(1, len(nums)):
            if nums[i] != nums[0]:
                break
            else:
                return 1 


        if len(nums) ==0:
            return 0
        elif len(nums) ==1:
            return 1
        else:
            sorted_nums = sorted(nums)
            runs = []
            for i in range(1,(len(sorted_nums))):
                runs.append(sorted_nums[i]-sorted_nums[i-1])


            print(runs)
            if runs.count(0) > 1:
                first_index = runs.index(0)
                runs = [value for i, value in enumerate(runs) if value != 0 or i == first_index]

            cs = []
            for j in range(len(runs)):
                c = 0
                while (j < len(runs)) and (runs[j] ==1):
                    c+=1
                    j+=1
                cs.append(c+1)
            
            return max(cs)

        