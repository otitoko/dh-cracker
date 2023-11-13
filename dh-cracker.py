g = 5
prime = 97
private_key_a = 32
private_key_b = 41

def diffe_hellman(g, prime, x, y):
    b = g**y % prime
    key = b**x % prime
    a = g**x % prime

    return key


def hellman_diffie(g, p, public_key_a, public_key_b):
    print("public key A is ", public_key_a)
    print("public key B is ", public_key_b)

    possible_private_key_a = []
    for i in range(p+1):
        if g**i % p == public_key_a:
            possible_private_key_a.append(i)

    possible_private_key_b = []
    for i in range(p+1):
        if g**i % p == public_key_b:
            possible_private_key_b.append(i)
    private_keys = []
    for i in possible_private_key_a:
        for j in possible_private_key_b:
            if public_key_a**j % p == public_key_b**i % p:
                private_keys.append(i)
                private_keys.append(j)

    return private_keys

print("they diffied key is: ",diffe_hellman(g, prime, private_key_a, private_key_b))
print("the private keys are: ", hellman_diffie(g, prime, 35, 80))


