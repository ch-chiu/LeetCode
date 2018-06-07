import re

class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        regex = re.compile(p)
        if regex.findall(s):
            return True if regex.findall(s)[0] == s else False
        return False


if __name__ == '__main__':
    s = "ab"
    p = ".*c"
    solution = Solution()
    ans = solution.isMatch(s, p )
    print(ans)