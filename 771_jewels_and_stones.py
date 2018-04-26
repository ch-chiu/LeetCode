class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        numJewels = 0
        for stone in S:
            if stone in J:
                numJewels += 1
        return numJewels


if __name__ == '__main__':
    J = "aA"
    S = "aAAbbbb"
    solution = Solution()
    result = solution.numJewelsInStones(J, S)
    print(result)