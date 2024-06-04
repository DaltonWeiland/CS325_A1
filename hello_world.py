print("Welcome to my World")
print("Input q to quit")
myint = input("Enter your favorite Show: ")
while myint != 'q':
	if len(myint) % 2 == 0:
		print(myint, "is a good show.")
	else:
		print(myint, "is a bad show.")
	myint = input("Enter your favorite Show: ")
print("Exiting program...")
