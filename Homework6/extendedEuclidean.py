'''
    Here we'll be implementing the extended Euclidean algorithm to find the GCD of two numbers
    and also the modular inverse of a number
'''



"""_summary_
    This function takes two integers dividend and devisor representing the 
    dividend and divisor respectively. 
    It returns the "euclidean quotient", i.e. the quotient of integer division between 
    the two and the remainder. 
"""
def e_divide(dividend: int, devisor: int): 
    
    if devisor == 0:
        raise ValueError("Devisor cannot be zero")
    
    quotient: int = dividend // devisor
    remainder: int = dividend % devisor
    
    return quotient, remainder


# shamelessly stole from wikipedia 
# it takes 2 numbers and finds the greatest common divisor of the two 
# returns it along with the bezout coefficients
def extended_euclidean(num1: int, num2: int):
    
    s: int = 0
    r: int = num2 
    old_s: int = 1
    old_r: int = num1
    
    while r != 0:
        quot_r , rem_r = e_divide(old_r, r)
        old_r, r = r, rem_r
        old_s, s = s, old_s - quot_r * s
        
    # here we compute the bezout coefficients
    # and then the gcd of the two numbers
    if num2 != 0: 
        bezout_t = (old_r - old_s*num1) // num2
    else:
        bezout_t = 0
    
    # so the bezout coefficients are old_s and bezout_t
    # and the gcd is old_r
    return old_r , old_s, bezout_t 


# def mod_inverse_with_crt(n, mods):
#     m, *more_mods = mods
#     inverses = []
#     for _, m in enumerate(more_mods):
#         inverse = extended_euclidean(n, m)  # we drop the bezout coefficients here 
#         if inverse is None:
#             return None    
#         inverses.append(inverse)
        

if __name__=="__main__":
    print(extended_euclidean(31, 640))
    print(extended_euclidean(49, 640))