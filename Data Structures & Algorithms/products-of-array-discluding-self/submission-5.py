class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [0] * len(nums)
        p = [1] * len(nums)
        s = [1] * len(nums)

        p[0] = nums[0]
        s[-1] = nums[-1]

        # print(p,s)
        
        product = 1 
        for i in range(len(nums)):
            p[i] = product
            product *= nums[i]

        product = 1 
        for i in reversed(range( len(nums))):
            s[i] = product
            product *= nums[i]
        
        for i in range(len(nums)):
            output[i] = p[i] * s[i]
        print(p,s)

        return output