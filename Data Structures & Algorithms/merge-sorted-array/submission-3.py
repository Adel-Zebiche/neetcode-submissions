class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for j in range(n) :
            val = nums2[j]
            nums1[m+j] = val
            i = m-1+j
            while i >=0  and nums1[i] > nums2[j] :
                nums1[i], nums1[i+1] = nums1[i+1], nums1[i]
                i-=1
        