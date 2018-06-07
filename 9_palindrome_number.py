class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        rem = 0
        while x > rem:
            rem = rem * 10 + x % 10
            x //= 10
        return True if (rem == x or x == rem / 10) else False


if __name__ == '__main__':
    x = 11
    solution = Solution()
    ans = solution.isPalindrome(x)
    print(ans)