class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        largest = 0
        largest_idx = [0,0]
        # while i <= j and i < len(height) and j < len(height):
        #     h = min(height[i], height[j])
        #     width = j - i
        #     area = h * width
        #     print(i, j ,area)
        #     if area > largest:
        #         largest = area
        #         largest_idx[0] = i
        #         largest_idx[1] = j
        #     if height[i] < height[j]:
        #         i += 1
        #     else:
        #         j += 1
        # print(largest_idx)
        # return largest
        while i < j:
            h = min(height[i], height[j])
            width = j - i
            area = h * width
            if area > largest:
                largest = area
                largest_idx = [i,j]
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return largest