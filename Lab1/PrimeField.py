p = int(input("Enter p value: "))

f = [0]+[i for i in range(p)]

mat = [f]
for i in range(p):
	tmp = [f[i+1]]
	for j in f[1:]:
		tmp.append((i+j)%p)
	mat.append(tmp)
print("\nAddition:\n")
for i in mat:
	print(i)
print("---x----x----x----x----x----x----x----x----")
mat = [f]
for i in range(p):
	tmp = [f[i+1]]
	for j in f[1:]:
		tmp.append((i-j)%p)
	mat.append(tmp)
print("\nSubtraction:\n")
for i in mat:
	print(i)
print("---x----x----x----x----x----x----x----x----")
mat = [f]
for i in range(p):
	tmp = [f[i+1]]
	for j in f[1:]:
		tmp.append((i*j)%p)
	mat.append(tmp)
print("\nMultiplication:\n")
for i in mat:
	print(i)
print("---x----x----x----x----x----x----x----x----")
mat = [f]
for i in range(p):
	tmp = [f[i+1]]
	for j in f[1:]:
		if j == 0:
			tmp.append('-')
		else:
			tmp.append((i/j)%p)
	mat.append(tmp)
print("\nDivision:\n")
for i in mat:
	print(i)
print("---x----x----x----x----x----x----x----x----")