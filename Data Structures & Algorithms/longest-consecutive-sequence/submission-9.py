class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) <= 0:
            return 0
        nums = sorted(set(nums))
        temp = nums[0]
        count = 0
        ans = 0
        print(nums)
        for i in range(len(nums)):
            print(f" ")
            print(f"Loop: {i} and temp starts: {temp}")
            if (nums[i] == temp ):
                print(f" ")
                print(f"-if 1 ")
                count += 1
                print(f"({nums[i]} == {temp}), Count + 1: {count}")
            else:

                print(f"ans {ans}")
                print(f" ")
                print(f"-if 2, {count} ")
                count = 1
                print(f"- ({nums[i]} != {temp}), Count = 1: {count}")
                temp = nums[i] + 1
                continue
            if ans <= count:
                ans = count
            temp = nums[i] + 1
            print(f"incrementing temp + 1 == {temp}")


        return ans