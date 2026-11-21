class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for index, j in enumerate(nums):
        
                if nums[i] + j == target and i != index:
                    return [i, index]