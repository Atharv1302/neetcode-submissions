class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:

        c1 = m - 1
        c1Sub = len(nums1) - 1
        c2 = n - 1

        while (c1 >= 0 and c2 >= 0):
            if nums1[c1] >= nums2[c2]:
                nums1[c1Sub] = nums1[c1]
                c1 = c1 - 1

            else:
                nums1[c1Sub] = nums2[c2]
                c2 = c2-1

            c1Sub = c1Sub - 1
        
        while c2 >= 0:
            nums1[c1Sub] = nums2[c2]
            c2 -= 1
            c1Sub -= 1