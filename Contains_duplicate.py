class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        sorted_nums = sorted(nums)
        for i in range(len(sorted_nums)-1):
            if sorted_nums[i] == sorted_nums[i+1]:
                return True
        return False
        
        '''
        This was my first solution, but it was not the best one. As it is O(n^2), it is not efficient and actually failed in the last test case.
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] == nums[j]:
                    return True

        return False
        '''