# Question 1 : Shape, Size and Datatype and finding sum of all elements in  array;

import numpy as np

nums = np.array([[10, 34, 56, 89, 78],
                 [89, 90, 34, 23, 24],
                 [99, 100, 56, 23, 77],
                 [12, 133, 90, 34, 55],
                 [11, 44, 77, 88, 99]])

print("Shape is: ", nums.shape,"\n")
print("Size is: ", nums.size,"\n")
print("Data type is: ", nums.dtype,"\n")

sum_of_elements = np.sum(nums)
print("The sum of all elements are: ", sum_of_elements,"\n")

# Question 2 : Even value Extraction and total number of even values;

even_values = nums[nums % 2 == 0]
print("Even values are : ", "\n")
print(even_values, "\n")

print("Total number of even values are: ", even_values.size, "\n")

# Question 3 : Indexing and slicing

third_column = nums[:2]
print("The Third column is: ", "\n")
print(third_column, "\n")

second_row = nums[1]
print("The second row is: ", "\n")
print(second_row, "\n")

sub_matrix = nums[1:3, 2:5]
print("The sub matrix is: ", "\n")
print(sub_matrix, "\n")

# Question 4 : Array Modification

modified_nums = nums.copy()
modified_nums[modified_nums < 35] = -1
print("Modified array is: ", "\n")
print(modified_nums, "\n")

modified_nums[3] = [31, 45, 89, 90, 43]
print("Changed nums is: ", "\n")
print(modified_nums, "\n")