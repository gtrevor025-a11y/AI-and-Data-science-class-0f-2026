print(f"PASSWORD AUTHENTICATOR")
password=input("please input your password : ")
attempts=1
while attempts <= 3 :
	pass_attempt=input("please enter your password : ")
	attempts +=1
	if pass_attempt !=password :
		print(f"incorrect password please try again")
	elif attempts == 3:
		if pass_attempt != password :
			print("you have been locked out ")
	else :
		print("correct")
		break
