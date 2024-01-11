from typing import List, Optional, Tuple


class Solution:
    count_valid = 0

    def next_front_index(
        self,
        front_index: int,
        nums: List[int],
        val: int,
        back_index: int,
    ) -> Tuple[int, Optional[int]]:
        while front_index <= back_index:
            if nums[front_index] == val:
                return front_index
            front_index += 1
            self.count_valid += 1
        return None

    def next_back_index(
        self, back_index: int, nums: List[int], val: int, front_index: int
    ) -> Optional[int]:
        while back_index >= front_index:
            if nums[back_index] != val:
                return back_index
            back_index -= 1
        return None

    def removeElement(self, nums: List[int], val: int) -> int:
        self.count_valid = 0
        front_index = 0
        count = len(nums)
        back_index = count - 1

        while front_index <= back_index:
            front_index = self.next_front_index(front_index, nums, val, back_index)
            if front_index == None:
                break
            back_index = self.next_back_index(back_index, nums, val, front_index)
            if back_index == None:
                break

            nums[front_index], nums[back_index] = nums[back_index], nums[front_index]
            front_index += 1
            back_index -= 1
            self.count_valid += 1

        return self.count_valid
