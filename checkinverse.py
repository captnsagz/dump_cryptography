Inverse = []
Position = []
NonInverse = []
mod = int(input("Enter modulo to check :"))
for i in range(mod):
	for n in range(mod):
		if( (i * n) % mod ) == 1:
			Inverse.append(i)
			Position.append(n)
			print("This number :", i ," has an inverse at position : " , n)

print("Inverse list : ",Inverse)
#print("NonInverse list :",NonInverse)