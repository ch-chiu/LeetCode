class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        num = sorted(nums1 + nums2)
        if len(num) % 2 == 0:
            ans = (num[len(num) / 2 - 1] + num[len(num) / 2]) / 2
        else:
            ans = num[int((len(num) - 1)/2)]
        return ans

if __name__ == '__main__':
    nums1 = [1, 3]
    nums2 = [2]
    solution = Solution()
    ans = solution.findMedianSortedArrays(nums1, nums2)
    print(ans)