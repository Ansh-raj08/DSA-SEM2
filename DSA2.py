# arr = [12,11,8,7,4]
# max_num = arr[0]
# for num in arr[1:]:
#     if num > max_num:
#         max_num = num
# print(max_num)
# arr.pop(0)
# max2_num = arr[0]
# for num2 in arr[1:]:
#     if num > max2_num:
#         max2_num = num2
# print(max2_num)

# arr = [12,55,76,34,65]
# max1_num = max2_num = float('-inf')
# for num in arr:
#     if num > max1_num:
#         max2_num = max1_num
#         max1_num = num
#     elif num > max2_num and num != max1_num:
#         max2_num = num
# print(f"first largest number: {max1_num} second largest number: {max2_num}")

# Two Sum problem-

# arr = [0,2,3,6,3,7]
# target = 9

# for i in range(0,len(arr)):
#     first_num = arr[i]

#     for j in range(i,len(arr)):
#         second_num = arr[j]
#         if first_num + second_num == target:
#             print(i,j)

arr = [2,3,4,5,6,1]
last_value = arr[-1]

for i in range(len(arr)-1,0,-1):
    arr[i] = arr[i-1]
arr[0] = last_value

print(arr)

