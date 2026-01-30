# decimal = 0
# binary = 1011
# powr = 0 

# while binary > 0:

# arr = [1,2,3,4]
# revarry = []

# @ 27 JAN 

import array as ar

# arrName = ar.array('i',[12,6,8,9,5])
# print(arrName)
# operations

# 1.Add
# a. append

# arrName.append(10) #append function only takes one number at a time
# print(arrName)

# arrName.insert(0,-9)
# print(arrName)

# arrName.pop(2)
# print(arrName)

# arrName.reverse() #reverse func takes no arguments in it's bracket()
# print(arrName)

# @ 28 JAN 11:05 AM

arrayName = ar.array('i',[22,33,44,55])
# print(arrayName)

# 1. Add
# a) append (value) --> add the values in last, T/C - O(1), O(N)
# b) insert (index, value) --> inserts the value at index, T/C - O(1), O(n)

# 2. Delete
# 3. Remove()
# 4. pop()

arrayName.remove(22)
arrayName.pop()
# print(arrayName)

arrayName[0]=40 # to update the array elements.
arrayName[1]=50
# print(arrayName)

# for i in range(0, len(arrayName)):
#     print(arrayName[i], end=" ")

# write a program to get sum and product.

# sum = 0
# product = 1
# for val in arrayName:
#     sum += val
#     product *= val

# print(sum)
# print(product)

# count = 0
# target = int(input("Enter target value: "))

# for val in arrayName:
#     if val == target:
#         count += 1

# print(count)

inc = True
dec = True
for i in range (0, len(arrayName)-1):
    if(arrayName[i]>arrayName[i+1]):
        inc = False
    if(arrayName[i]<arrayName[i+1]):
        dec = False

if(inc == True):
    print("It's in increasing order.")

elif(dec == True):
    print("It's in descending order.")

else:
    print("Not Sorted.")


