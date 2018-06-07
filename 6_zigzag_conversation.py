class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        i = 0
        out_str = []
        loc = 0
        down = True
        if numRows == 1:
            out_str = s
        else:
            for n in range(numRows):
                out_str.append("")
            while i < len(s):
                if loc < numRows and down:
                    out_str[loc] += s[i]
                    loc += 1
                elif loc == numRows:
                    down = False
                    loc = numRows - 2
                    out_str[loc] += s[i]
                    if loc == 0:
                        down = True
                        loc += 1
                    else:
                        loc -= 1
                else:
                    if loc == 0:
                        down = True
                        out_str[loc] += s[i]
                        loc += 1
                    else:
                        out_str[loc] += s[i]
                        loc -= 1
                i += 1
        return ''.join(out_str)


if __name__ == '__main__':
    s = "ABCDEF"
    numRows = 2
    solution = Solution()
    ans = solution.convert(s, numRows)
    print(ans)