# f = open("data.txt","r")

# for line in f:
# 	print(line)

# # print(f.readline())
# # print(f.readline())
# # print(f.readline())

# f.close()



# Other way to do to avoid error of File Closing
# this Automatically closes because of -- with --
with open("data.txt","r") as f:
	# for line in f:
	# 	print(line)
	print(f.read())
	f.seek(0) # Use to Reposition the cursor
	print(f.read(10)) # 10 char printing

