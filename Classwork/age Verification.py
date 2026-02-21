name=input("What is your name : ")
birth_date=int(input("what year were you born : "))
age=2026 -birth_date
if age >=18:
	print(f"welcome {name} you are {age} so are allowed to access our site .")
else :
	print(f"sorry you are {age} years old which is not of legal age to access our site . ")
	