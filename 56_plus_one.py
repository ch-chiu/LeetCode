class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        holder = 0
        ans = []
        digits[len(digits) - 1] += 1
        for i in range(len(digits) - 1, -1, -1):
            digits[i] += holder
            if digits[i] >= 10:
                holder = 1
                digits[i] %= 10
                if i == 0:
                    ans = []
                    ans.append(1)
                    ans.extend(digits)
            else:
                holder = 0
                ans = digits
        return ans

    def simpleSolution(self, digits):
        return list(map(int, list(str(int("".join(map(str, digits))) + 1))))


if __name__ == '__main__':
    _input = [9]
    solution = Solution()
    ans = solution.plusOne(_input)
    print(ans)