class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums2 = []
        for num in nums:
            if num not in nums2:
                nums2.append(num)
            else:
                return True
        return False
            