data1=500
data2=("m,n,o,p,q")
data3="gtr"
print(data1,data2,data3)
print(type(data1) , type(data2) , type(data3))
print("loading " ,end='!!!!')

print (data1,data2,data3,sep="&")
# for loops to show differenc when using indents
for i in range (1,10):
	print(i ,end="#$@")
	print("1")
print("the end")
print(i +1)
#various functions of slashes \
print("one chicken \ntwo dogs")#goes to new line
print("Next level\tgames\tgraphics")#creates a tab space
print("spaceship\\spacecraft\\rockets")#creates a slash
print("12345\b66")#removes previos character like thos one becomes 55566
print("my cows\' are \"home\"")# use to create quptes inside strings since if used like that woul ruin program
var1="trevor"
var2=45
var3=3.146
print(f"{var3:.1f}")
print(f"{var1.upper()}")
print(f"{var1.lower()}")
print(f"{var2:>6}")#creates spaces as specified by the number following it like 20 or 54 spaces
print(f"{var2:<7}")#creates spaces after the variable
k=99
k += 1
print(k)
k*=2
print(k)
k -=1
print(k)
k/=3
print(k)
k%=3
print(k)