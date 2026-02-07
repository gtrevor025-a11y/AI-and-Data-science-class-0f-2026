num=input("enter first number : ")
print(type(num))
num=int(num)
print(type(num))

num2=int(input("enter second number : "))
print(type(num2))

print(f"This is the first number you gave me {num}\nThis is the second number you gave me {num2}")

print(f"1.add")
print(f"2.subtraction")
print(f"3.multiplication")
print(f"4.division ")
operation=int(input("choose an operation : "))
if operation==1 :
	print(num + num2)
elif operation ==2 :
	print(num -num2)
elif operation ==3 :
	print(num *num2)
elif operation==4 :
	print(num/num2)
else :
	print ("invalid operation for this program")
	