class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for num in nums:
            x = nums.count(num)
            print(x)
            if x > 1:
                return True
        return False
            