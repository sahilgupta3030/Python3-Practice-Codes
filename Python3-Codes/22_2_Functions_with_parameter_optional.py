# Two Parameters
def greet(name, dish):
	print("How you doing?",name)
	print("Your favourite food: ",dish)

greet("Shubham","Samosa")
greet("Bhuvam","Maggie")
print("------------------")



# Optional Parameter
def greet(name, dish="Dosa"):
	print("How you doing?",name)
	print("Your favourite food: ",dish)

greet("Shubham","Samosa")
greet("Shubham")


