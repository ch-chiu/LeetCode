class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        negative = 1
        str_x = str(x)
        str_x = str_x[::-1]
        if x < 0:
            str_x = str_x.replace("-", "")
            negative = -1
        x = int(str_x) * negative
        if x >= -2147483648 and x <= 2147483647:
            ans = x
        else:
            ans = 0
        return ans


if __name__ == '__main__':
    x = -123
    solution = Solution()
    ans = solution.reverse(x)
    print(ans)
