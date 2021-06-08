nums = [3, 1, 2, 5, 1, 5, -7, 9, -8, -3, 3]

diff_list = []

for i in range(len(nums) - 1):
    diff = abs(nums[i] - nums[i+1])
    diff_list.append(diff)

mean = sum(diff_list) / len(diff_list)

print(f'M: {round(mean, 1)}')
