

def phi(p, q):
    return (p-1)*(q-1)

def get_candidate(e, phi_n):
    # since we're dealing with small numbers we're going to only generate 100 iterations
    candidates = [(phi_n+1)+i*phi_n for i in range(100)]
    
    for i, num in enumerate(candidates):
        if num % e == 0:
            return num
    return -1

# given phi of n and the modular inverse
def find_mod_inverse(e, phi_n):
    
    cand = get_candidate(e, phi_n)
    if cand==-1: 
        raise ValueError("No candidate was found for the modular inverse")
    
    return cand/e

    
# this function is just to verify t
def RSA_decrypt_special_case(y, e, p, q):
    n = p*q
    phi_n = phi(p,q)
    try: 
        d = find_mod_inverse(e, phi_n)
        ## privatekey is d and n 
        # return sthe decrypted value and then d (the modular inverse) 
        return y**d % n , d
    except:
        print("Could not find a modular inverse to decrypt this value")

    


    


if __name__=='__main__':

    p=31
    q=37
    e=17
    ciphertext = 2
    
    
    print(f"The plaintext is {RSA_decrypt_special_case(ciphertext, e, p, q)}")