class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        map = {}
        counter = 0

        for num in nums: 
            counter += 1
            if (num in map): 
                return True
            else:
                map[num] = counter
            
        return False