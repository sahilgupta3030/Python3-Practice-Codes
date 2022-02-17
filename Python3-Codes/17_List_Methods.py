a = [22, 47, 75, 84, 68, 84, 12]

a.append(33)
print("After append: ",a)

a.insert(1, 155)
print("After insert: ",a)

a.sort()
print("After sort: ",a)

a.pop(0)
print("After pop: ",a)

a.reverse()
print("After reverse: ",a)


print("Get the index: ",a.index(84))
print("Get the count: ",a.count(84))

a.clear()
print("After clear: ",a)
