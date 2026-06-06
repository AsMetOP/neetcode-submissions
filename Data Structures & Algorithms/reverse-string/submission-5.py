class Solution:
    def reverseString(self, s: List[str]) -> None:
        # i = 0
        # j = len(s) - 1
        # while i < j:
        #     s[i], s[j] = s[j], s[i]
        #     i += 1
        #     j -= 1
        # s.reverse()
        for i in range(len(s) // 2):
            j = len(s) - 1 - i
            s[i], s[j] = s[j], s[i]