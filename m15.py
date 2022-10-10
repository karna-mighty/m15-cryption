import main1 as m15
ch=(input("enter \n0 for encryption \n1 for decryption \n(0,1) "))

def fun():
	global ch	

	if ch=='0':
		text=input("enter the message to encrypt\n")
		key=input("enter the key \n")
		a=(m15.encode(m15.encrypt(text,key)))
		for i in a:
			print(i,end="")
	elif ch=='1':
		text=input("enter the message to decrypt \n")
		key=input("enter the key \n")
		a=m15.decrypt(m15.decode(text),key)
		for i in a:
			print(i,end="")
	else:
		print("enter either  0 or 1 not ",ch)
		ch=input()
		fun()
fun()
