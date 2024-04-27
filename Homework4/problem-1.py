# this script is here to generate the multiplication and addition tables for GF(7)
import numpy as np



# this function generates the multiplication table for 
# a given galois field GF(num) where num is the modulus of the field
def get_mult_table(num):
    rv = np.zeros((num,num),dtype=np.uint8)
    for i in range(num):
        for j in range(num):
            rv[i][j] = (i*j) % num
    return rv

def get_addition_table(num):
    rv = np.zeros((num,num),dtype=np.uint8)
    for i in range(num):
        for j in range(num):
            rv[i][j] = (i+j) % num
    return rv

def make_markdown_table(table):
    rv = """| 0 | 1 | 2 | 3 | 4 | 5 | 6 |\n|---|---|---|---|---|---|---|\n"""
    for row in table:
        rv += "|"
        for entry in row:
            rv += f" {entry} |"
        rv += "\n"
    return rv

if __name__=="__main__":
    print(make_markdown_table(get_mult_table(7)))
    print("\n\n\n")
    print(make_markdown_table(get_addition_table(7)))