class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums + nums 
        # n = len(nums)
        # ans = [nums] * 2
        # for i in range(n):
        #     ans = nums + nums
        # return ans

