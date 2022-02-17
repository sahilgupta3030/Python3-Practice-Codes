# Dictionary Example 1
marks = {"Kuchu":70, "Puchu":60, "Sahil":98, 11:80, 12:85}

print(marks)
print(marks["Sahil"])
print(marks[11])


# Dictionary Example 2
numbers = {1:1, 2:4, 3:9, 4:16, 5:25, 6:36}

for x in numbers:
	print(x ,numbers[x])


# Adding or Updating dictionary
marks = {"Kuchu":70, "Puchu":60, "Sahil":98, 11:80, 12:85}

marks["Rohit"] = 99
print(marks)

