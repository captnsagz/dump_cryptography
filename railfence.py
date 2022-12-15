str_enc = input("Enter the string you want to encrypt :")
temp1 = ""
temp2 = ""

for ch in str_enc:
	if str_enc.index(ch) % 2 == 0:
		temp1 = temp1 + ch
	else:
		temp2 = temp2 + ch

print(temp1, temp2)
str_enc = temp1 + temp2
print(str_enc)
