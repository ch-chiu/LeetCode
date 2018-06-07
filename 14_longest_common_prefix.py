class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        min_length = len(strs[0])
        flag = 1
        for n in range(1, len(strs)):
            if len(strs[n]) < min_length:
                min_length = len(strs[n])
        common_str = ""
        for i in range(min_length):
            tmp = strs[0][i]
            for j in range(len(strs)):
                if strs[j][i] != tmp:
                    flag = 0
                    break
            common_str += tmp * flag
        return common_str


if __name__ == "__main__":
    strs = ["cat", "catlog", "category"]
    solution = Solution()
    ans = solution.longestCommonPrefix(strs)
    print(ans)
