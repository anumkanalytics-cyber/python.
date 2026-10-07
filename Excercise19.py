#Even number filter
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
odd_num = []
even_num = []
for i in num:
    if i % 2 != 0:
        odd_num.append(i)
    else:
        even_num.append(i)
print("Original list:", num)
print("Even numbers:", even_num)
print("Odd numbers:", odd_num)