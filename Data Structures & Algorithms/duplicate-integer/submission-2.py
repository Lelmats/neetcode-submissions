class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        map = {}
        for num in nums:
            if num in map:
                map[num] += 1
                if map[num] > 1:
                    return True
            else: map[num] = 1
            
        print(map) 
        return False