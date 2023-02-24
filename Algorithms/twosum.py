from typing import List


class Solution:
    @staticmethod
    def two_sum(nums: List[int], target: int) -> List[int]:
        values = {}
        for index, element in enumerate(nums):
            diff = target - element
            if diff in values:
                return [index, values[diff]]
            values[element] = index
        return []
