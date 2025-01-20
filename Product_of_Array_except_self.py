class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        def recursion(nums):
            if len(nums) ==1:
                return nums[0]
            for i in range(len(nums)):
                return nums[0]*recursion(nums[1:])

        answer = []
        for i in range(len(nums)):
            temp = nums.copy()
            temp.pop(i)
            answer.append(recursion(temp))


        return answer

        
