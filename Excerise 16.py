#Student grade analyzer
marks = []
number = int(input("How many students? "))
i = 0
while i < number:
    mark = int(input("Enter marks: "))
    marks.append(mark)
    i += 1
print("Marks:", marks)
highest = marks[0]
lowest = marks[0]
i = 1
while i < len(marks):
    if marks[i] > highest:
        highest = marks[i]
    if marks[i] < lowest:
        lowest = marks[i]
    i += 1
total = 0
i = 0
while i < len(marks):
    total += marks[i]
    i += 1
average = total / len(marks)
passed = 0
failed = 0
i = 0
while i < len(marks):
    if marks[i] >= 40:
        passed += 1
    else:
        failed += 1
    i += 1
print("Highest:", highest)
print("Lowest:", lowest)
print("Average:", round(average, 2))
print("Passed:", passed)
print("Failed:", failed)