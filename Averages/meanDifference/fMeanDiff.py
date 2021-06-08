from typing import List

def diff(nums: List[int]) -> List[int]:
    return [abs(nums[i] - nums[i + 1]) for i in range(len(nums) - 1)]

def mean(lst: List[int]) -> float:
    return sum(lst) / len(lst)

def mean_diff(nums: List[int], diff) -> None:
    return round(mean(diff(nums)), 1)


nums = [3, 1, 2, 5, 1, 5, -7, 9, -8, -3, 3]

print(f'M: {mean_diff(nums, diff)}')
