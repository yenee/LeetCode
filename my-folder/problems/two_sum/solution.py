class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        save = []
        for i in range(len(nums)):
            n = target - nums[i]
            if nums[i] in save:
                return [nums.index(n), i]
            save.append(n)