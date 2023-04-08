n = int(input('Enter a number between 1 to 10'))

while True:
    try:
        if 1<n<10:
            print("Yes")
        else:
            print("Number not in between 1 and 10")
        break
    except ValueError:
        print("Enter a Number pls")
        continue

