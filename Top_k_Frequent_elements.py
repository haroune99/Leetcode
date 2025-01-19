class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        val_counts = {}
        for num in nums:
            if num in val_counts.keys():
                val_counts[num] +=1
            else:
                val_counts[num] = 1

        sorted_counts = sorted(val_counts.items(), key = lambda x: x[1])
        sorted_counts = sorted_counts[:k]

        final_list = []
        for element in sorted_counts:
            final_list.append(element[1])

        return final_list


