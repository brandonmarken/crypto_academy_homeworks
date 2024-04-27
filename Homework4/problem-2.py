
import numpy as np
import itertools 
import icecream as ic 


# this function generates a list of all permutations of lists length n consisting only of 0 and 1
# these will represent the coefficients of polynomials of GF(2^n+1)
def generate_permutations(n):
    return [list(seq) for seq in  itertools.product([0, 1], repeat=n)]


def generate_polynomials(n):
    coeffs = generate_permutations(n)
    # ic(coeffs)
    # ic(len(coeffs))
    return [np.polynomial.Polynomial(x) for x in coeffs]

# our polynomial multiplication may generate 2s occasionally but all of our
# it needs to be modulus m  (though in our case it's likely to always be a 2 )
def apply_mod(poly, n=2):
    
    coef = np.array(list(map(lambda x: x % n, poly.coef)))
    poly.coef = coef
    return poly
    
# this is our pretty print function which will return a string representing the polynomial in markdown
# it takes a list of coefficients for the result 
# 
def pretty_print_poly(poly):
    rv = ''
    for i in range(len(poly.coef)):
        if poly.coef[i] != 0:
            if i == 0:
                rv += f"{poly.coef[i]} + "
                
            elif i == 1:
                rv += f"{poly.coef[i]}x + "
            else:
                rv += f"{poly.coef[i]}x^{i} + "
    return rv[:-3] # remove the last plus sign

# this function generates the multiplication table of all the polynomials in the GF(2^n) 
# which will be A*B mod P(x) where P(x) is the irreducible polynomial
# and all coefficients are mod 2
# the return value is a table of polynomials 
def generate_table(polys, irr_poly):
    max_length = len(polys)
    rv = np.zeros((max_length, max_length), dtype=np.polynomial.Polynomial)
    #we can simplify this with itertools later but for now we won't be doing that
    for i in range(max_length):
        for j in range(max_length): 
            rv[i][j] = apply_mod(polys[i]*polys[j])%irr_poly
    return rv

# This function takes a numpy polynomial (i.e. numpy.polynomial.Polynomial)
# and returns a string for the LaTeX representation 
def poly_to_latex(poly):
    latex_rv = ""
    coeffs = poly.coef[::-1]        # reversing hte coefficients since they're flipped in numpy
    
    for i, coeff in enumerate(coeffs):
        if coeff != 0: 
            if i == 0:
                # Constant term
                latex_rv += str(int(coeff))
            elif i == 1:
                # Linear term 
                if coeff == 1:
                    latex_rv += "x"
                elif coeff == -1:
                    latex_rv += "-x"
                else:
                    latex_rv += f"{int(coeff)}x"
            else: 
                # higher order terms can be handled together
                if coeff == 1:
                    latex_rv += f"x^{{{i}}}"
                elif coeff == -1:
                    latex_rv += f"-x^{{{i}}}"
                else:
                    latex_rv += f"{int(coeff)}x^{{{i}}}"
                  # Add '+' sign except for the first non-zero term
       # if latex_rv and coeff > 0 and i != 0:
        if latex_rv and coeff > 0:
            latex_rv += " + "
            
    # we remove the final plus at the end of the string
    latex_rv = latex_rv[:-3]

    return f"${latex_rv}$"


# this is hardcoded because I need to make this table for my homework
# do not use in production 
# TODO make it flexible rather than hardcoded 
def make_markdown_table(table):
       
    rv = """| x | 0 | 1 | x | x + 1 | x^2 | x^2 + 1 | x^2 +x | x^2 + x + 1 |\n|---|---|---|---|---|---|---|---|---|\n"""

    for i, row in enumerate(table):
        # adding the beginning of the row
        if i < 2: 
            rv += f"| {i} |"
        else:
            rv += f"| x^{i-2} |"
        
        # convert each of the polynomials we have into laTeX and add them 
        # to rv 
        for j, poly in enumerate(row):
             rv += f" {poly_to_latex(poly)} |"

        rv +=f"\n"
        
    return rv


if __name__ == '__main__':
    
    degree = 3 
    polys = generate_polynomials(degree)
    # our irreducible polynomial x^3 + x + 1
    irreduc_poly = np.polynomial.Polynomial([1, 1, 0, 1])
    
    mult_table = generate_table(polys, irreduc_poly)
    #print(make_markdown_table(mult_table))
    # print(mult_table.shape)
    # print(mult_table)
    
    
    