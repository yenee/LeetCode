class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = 0
        for i in range(0, len(nums)):
            if nums[i - k] == 0:
                    nums.pop(i - k)
                    nums.append(0)
                    k += 1