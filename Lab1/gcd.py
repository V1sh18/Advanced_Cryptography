def gcd(a, b):
	if(b == 0):
		return a
	else:
		return gcd(b, a % b)

i = 0
while i!=5:
	a = int(input("Enter Value 1: "))
	b = int(input("Enter Value 2: "))
	print(f"The gcd of {a} and {b} is : ", end="")
	print(gcd(a, b))
	i+=1
