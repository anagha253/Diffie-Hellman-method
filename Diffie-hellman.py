p,g=input("Enter public keys: ").split()
p=int(p)
g=int(g)

a=int(input("Enter the private key of alice: "))
b=int(input("Enter the private key of bob: "))

def alice1(a,p,g):
    return (g**a)%p
def bob1(b,p,g):
    return (g**b)%p

m=key_alice=bob1(b,p,g) 
n=key_bob=alice1(a,p,g)

#secret key generation

def alice_secret(m,a,p):
    return (m**a)%p
def bob_secret(n,b,p):
    return (n**b)%p

ka=alice_secret(m,a,p)
kb=bob_secret(n,b,p)

if ka==kb:
    print("Success! Generated symmetric key is "+str(ka))
else:
    print("error...")
