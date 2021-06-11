nums = [3, 1, 2, 5, 1, 5, -7, 9, -8, -3, 3]

diff_list = [abs(nums[i] - nums[i + 1]) for i in range(len(nums) - 1)]

mean = sum(diff_list) / len(diff_list)

print(round(mean, 1))
