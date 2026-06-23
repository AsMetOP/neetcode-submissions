class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = 2 * [nums]
        for i in  range(0, len(nums)):
            ans = nums + nums
        return ans