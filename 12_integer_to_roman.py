class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        syms = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        syms_dict = {"M": 1000, "CM": 900, "D": 500, "CD": 400, "C": 100, "XC": 90,
                     "L": 50, "XL": 40, "X": 10, "IX": 9, "V": 5, "IV": 4, "I": 1}
        coef = {}
        ans = ""
        rem = num
        for i in range(len(syms)):
            key = syms[i]
            if key in syms_dict:
                coef[key] = rem // syms_dict[key]
                rem -= coef[key] * syms_dict[key]
        for sym in syms:
            if sym in coef:
                ans += sym * coef[sym]
        return ans


if __name__ == '__main__':
    num = 58
    solution = Solution()
    ans = solution.intToRoman(num)
    print(ans)