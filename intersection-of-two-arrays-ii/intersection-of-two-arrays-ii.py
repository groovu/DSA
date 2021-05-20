class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        def search(big, small):
            result = []
            for i in small:
                if i in big:
                    big[big.index(i)] = -1
                    result.append(i)
            return result
        
        if len(nums1) > len(nums2):
            return search(nums1, nums2)
        else:
            return search(nums2, nums1)
        