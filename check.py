f = 0
mod = int(input("Enter the modulo to use :"))
a = int(input("Enter the value of a:"))
b = int(input("Enter the calue of b:"))
lis = []
for i in range(mod) :
	f = a * i + b
	lis.append(f%mod)
print(lis)

for c in lis:
	if lis.count(c) != 1:
		print(c)


