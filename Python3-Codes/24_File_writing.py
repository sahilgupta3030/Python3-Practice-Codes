persons = ["Anuj\n", "Shubham\n", "Rohit\n"]

with open("written.txt", "w") as f:
	f.write("Sahil\n")
	f.writelines(persons)
	print("Sucess...")

# use APPEND mode as WRITE mode is dangerous
# as it deletes previous data