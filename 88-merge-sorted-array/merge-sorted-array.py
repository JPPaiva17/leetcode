class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        write = m + n - 1
        readNums2 = n - 1
        readNums1 = m - 1
        
        while readNums2 >= 0:
            if readNums1 >= 0 and nums1[readNums1] > nums2[readNums2]:
                nums1[write] = nums1[readNums1]
                readNums1 -= 1
            else:
                nums1[write] = nums2[readNums2]
                readNums2 -= 1
            write -= 1