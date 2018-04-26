class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i = 0
        j = len(height) - 1
        left_max = right_max = 0
        volume = 0
        while i < j:
            if height[i] > height[j]:
                if height[j] >= right_max:
                    right_max = height[j]
                else:
                    volume += right_max - height[j]
                j -= 1
            else:
                if height[i] >= left_max:
                    left_max = height[i]
                else:
                    volume += left_max - height[i]
                i += 1
        return volume


if __name__ == '__main__':
    height_list = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    solution = Solution()
    result = solution.trap(height_list)
    print(result)