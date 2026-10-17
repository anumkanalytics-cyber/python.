def find_name(names, target):
    names = sorted(names, key=str.lower)
    target = target.lower()
    left = 0
    right = len(names) - 1
    while left <= right:
        middle = (left + right) // 2
        if names[middle].lower() == target:
            return middle
        elif names[middle].lower() < target:
            left = middle + 1
        else:
            right = middle - 1
    return -1
names = ["Ali", "Amna", "zara", "sara", "Marium", "Ahmad", "Isha"]
target_name = "Marium"
result = find_name(names, target_name)
if result != -1:
    print("Found at index", result)
else:
    print("Not found")