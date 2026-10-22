n = [ 1, 2, 3, 4, 5, 5, 5, 5, 6, 7, 7, 8, 9 ,10]
m = [1, 22, 3 , 55 , 33, 2, 10]
for num in m:
    count = 0
    for x in num:
      if x == num:
        count += 1
        print(count)