#Input: list1 = [2, 7, 5, 64, 14]
#Output: Even = 3, odd = 2
list1 = [10, 21, 4, 45, 66, 93, 1]

even_count, odd_count = 0,0
for num in list1:
    if num % 2 == 0:
        even_count +=1

    else:
            odd_count +=1
print("Even numbers in the list:", even_count)
print("Odd numbers in the list:",odd_count)