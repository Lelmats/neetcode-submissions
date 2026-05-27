class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        res = []
        for num in nums:
            if num in map:
                map[num] += 1
            else:
                map[num] = 1
                
        map = {k: v for k, v in sorted(map.items(), key=lambda item: item[1], reverse=True)}
                
        for i,key in enumerate(map):
            if i >= k: break
            res.append(key)
            
        return res
        
        