import random
def encode(text):
    mixed=[]
    for i in range(33,127):
      mixed.append(str(chr(i)))
    
    a=[]
    b=[]
    for i in range((len(text))):
      a.append([])
          
    for i in range((len(text))):
      a[i].append(text[i])
    
    for i in range((len(text))):
      for j in range((len(text))):
         a[i].append(random.choice(mixed))
    
    for i in range((len(text))):
      for j in range((len(text))):
            b.append(a[i][j])
            
    return b
     
def decode(text):
    y=int((len(text))**0.5)
    return (text[0::y])

def encrypt(text,key):


    dec = 0
    for i in key:
        dec+=ord(i)


    a=[]
    b=[]
    dec=dec//26
    decrypt=[]
    for i in range(32,127):
        a.append(str(chr(i)))
        
    
    for i in range(len(text)):
        for j in range(len(a)):
            if (text[i]==a[j]):
                b.append(j-dec)

    for i in b:
        decrypt.append(a[i])
    
    return  decrypt        

def decrypt(text,key):
    
    
    dec = 0
    for i in key:
        dec+=ord(i)
   


    a=[]
    b=[]

    crypt=[]

    dec=dec//26

    for i in range(32,127):
        a.append(str(chr(i)))
    

    for i in range(len(text)):
        for j in range(len(a)):
            if (text[i]==a[j]):
       
                b.append(j)
    

    for i in b:
    
    
        if i+dec < len(a):
    	    crypt.append(a[i+dec])
    	
        else:
    	    crypt.append(a[(i+dec)-95])
    	    
    return crypt
