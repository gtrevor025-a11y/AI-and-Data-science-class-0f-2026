#this is a  simple password checker based on if statements  ,bools,input ,print and variables

#asks user for their password and name
name=input("What is your name :  ")
password=input("please place your preferred password : ")
#this next section says asks if your password is correct
pw=input("what is ypur password :")
if pw==password:
	print(f"welcome {name} ")
else:
	print("incorrect password to retrieve your password")
