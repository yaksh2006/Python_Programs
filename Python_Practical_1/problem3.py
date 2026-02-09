import numpy as np
# nums = np.arange(10, 90, 4).reshape(4, 5)
# print(nums, "\n")
# third_column = nums[:,2]
# print(third_column, "\n")
# nums[3] = [1, 2, 3, 4, 5]
# print(nums)

names = np.array(["Roxana", "Statira", "Roxana", "Statira", "Roxana"])
score = np.array([126, 115, 130, 141, 132])
print(names)
print(score)

print(score[score < 130])

score[names == "Statira"]
score[names == "Roxana"] +10
print(score)