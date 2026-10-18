
def find_dulpicate(numbers):
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i != j and numbers[i] == numbers[j]:
                return True

    return False


numbers = [10, 22, 35, 20, 48]

result = find_dulpicate(numbers)

if result:
    print("Duplicate found!")
else:
    print("No Duplicate.")
