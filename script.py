try:
	with  open("/mnt/c/Users/akars/OneDrive/Desktop/test.txt") as my_file :
		print(my_file.readlines())
except FileNotFoundError as err:
	print("file not found")


