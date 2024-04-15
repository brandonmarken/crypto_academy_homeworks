
import sys
from icecream import ic  


# start state
start_state = [1, 1, 1, 1, 1, 1, 1, 1]

# primitive polynomial for the LFSR 
# 1 + x + x^3 + x^4 + x^8
primitive_polynomial = [1, 1, 0, 1, 1, 0, 0, 0, 1]

# this function generates the next bit of output for this LFSR
# given the current state as a list of bits, 1 if a bit is set and 0 if it's not
# and the primitive polynomial as a list of bits, 1 if a bit is set and 0 if it's not
def next_bit(current_state, primitive_polynomial):
    # the next bit is the xor of the bits in the current state
    # that are set and the bits in the primitive polynomial
    next_bit = 0
    for i in range(len(current_state)):
        if current_state[i] == 1 and primitive_polynomial[i] == 1:
            next_bit ^= 1
    # shift the current state to the right
    for i in range(len(current_state)-1, 0, -1):
        current_state[i] = current_state[i-1]
    # set the first bit of the current state to the next bit
    current_state[0] = next_bit
    return current_state

if __name__=='__main__':
    current_state = start_state
    for i in range(16):
        current_state = next_bit(current_state, primitive_polynomial)
        print(current_state)