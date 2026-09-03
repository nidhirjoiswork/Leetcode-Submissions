class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        seen = {}

        for i, val in enumerate(nums):
            res = target - val
            
            if res in seen:
                return[seen[res], i]

            seen[val] = i