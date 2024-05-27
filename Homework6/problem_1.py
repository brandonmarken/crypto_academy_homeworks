
import extendedEuclidean



"""
    This is the gen_keys function
    It takes 2 integers p and q each representing one of the primes
    for the RSA algorithm
    it returns the public key and private key as arbitrary length integers
"""
def gen_keys(p: int, q: int):
    
    n: int = p*q 
    phi: int = (p-1)*(q-1)
    
    
def phi(p, q):
    return (p-1)*(q-1)

def is_valid_exponent(e, phi_n):
    return extendedEuclidean.extended_euclidean(e, phi_n)[0] == 1

if __name__=='__main__':
    p = 41
    q = 17
    n = p*q
    phi_n = phi(p, q)
    print(f"n={n} and phi(n)={phi_n}")
    e1 = 32 
    e2 = 49 
    
    if is_valid_exponent(32, phi_n):
        print(f"{e1} is a valid exponent")
    else: 
        print(f"{e1} is not a valid exponent")
        
    
    if is_valid_exponent(49, phi_n):
        print(f"{e2} is a valid exponent")
    else:
        print(f"{e2} is not a valid exponent")
    
    
    _, bezout_1, _ = extendedEuclidean.extended_euclidean(49, phi_n)
    print(f"the modular inverse you're looking for is {bezout_1}")
    