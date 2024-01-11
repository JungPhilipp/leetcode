import sys
from typing import List, Optional


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        out = nums1
        out_index = m + n - 1
        in_index1 = m - 1
        in_index2 = n - 1
        while out_index >= 0:
            in1 = nums1[in_index1] if in_index1 >= 0 else -1 * sys.maxsize
            in2 = nums2[in_index2] if in_index2 >= 0 else -1 * sys.maxsize

            if in1 > in2:
                out[out_index] = in1
                in_index1 -= 1
            else:
                out[out_index] = in2
                in_index2 -= 1
            out_index -= 1
