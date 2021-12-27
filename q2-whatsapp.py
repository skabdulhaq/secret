print("Enter 3 Numbers")

num1 = int(input("Enter First Number\n"))
num2 = int(input("Enter Second Number\n"))
num3 = int(input("Enter Third Number\n"))

if num1 > num2:
    if num1 > num3:
        print("First Number i.e "+str(num1)+" is largest")
    else:
        print("Third Number i.e "+str(num3)+" is largest")
else:
    if num2 > num3:
        print("Second Number i.e "+str(num2)+" is largest")
    else:
        print("Third Number i.e "+str(num3)+" is largest")
