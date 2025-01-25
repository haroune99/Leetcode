class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1

        # Find the middle index
        mid = len(nums) // 2

        # Check the middle element
        if target < nums[mid]:
            return self.search(nums[:mid], target)  # Search in the left half
        elif target > nums[mid]:
            result = self.search(nums[mid + 1:], target)  # Search in the right half
            return result + mid + 1 if result != -1 else -1  # Adjust index if found
        else:
            return mid 

