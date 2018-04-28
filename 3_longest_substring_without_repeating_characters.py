class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_len = 0
        i = 0
        tmp = {}
        for j in range(len(s)):
            if s[j] in tmp and i <= tmp[s[j]]:
                i = tmp[s[j]] + 1
            else:
                max_len = max(max_len, j - i + 1)
            tmp[s[j]] = j
        return max_len


if __name__ == '__main__':
    solution = Solution()
    string = "pwwkew"
    result = solution.lengthOfLongestSubstring(string)
    print(result)