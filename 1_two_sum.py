class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in nums and nums.index(complement) != i:
                return [i, nums.index(complement)]


if __name__ == '__main__':
    solution = Solution()
    nums = [3, 3]
    print(solution.twoSum(nums, 6))