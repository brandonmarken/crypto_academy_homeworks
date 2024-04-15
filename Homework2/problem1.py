import sys
# the number map which takes an index and returns a letter 
# where 0 -> A, 1 -> B, 2 -> C, ..., 25 -> Z
number_map = [chr(i) for i in range(97, 123)]

def letter_to_number(letter):
    return number_map.index(letter)

def number_to_letter(num):
    return number_map[num]

def encrypt_decrypt_function(text, key):
    num = letter_to_number(text)
    key = letter_to_number(key)
    return number_to_letter((num-key) % 26)


if __name__=="__main__":


    cipher_text = "bsaspp kkuosp"
    theKey = "rsidpy dkawoa"
    result = ""
    for i in range(len(cipher_text)):

        # skip if we encounter a space 
        if cipher_text[i] == " ":
            result += " "
            continue 
        
        result += encrypt_decrypt_function(cipher_text[i], theKey[i])
    
    print(result) 