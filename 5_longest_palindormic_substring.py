class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        loc_dict = {}
        max_len_str = ""
        for i in range(len(s)):
            if s[i] not in loc_dict:
                loc_dict[s[i]] = []
            loc_dict[s[i]].append(i)
            for loc in loc_dict[s[i]]:
                substr = s[loc:i + 1]
                if i - loc >= len(max_len_str) and substr == substr[::-1]:
                    max_len_str = substr
        return max_len_str


if __name__ == '__main__':
    s = "babadada"
    solution = Solution()
    ans = solution.longestPalindrome(s)
    print(ans)