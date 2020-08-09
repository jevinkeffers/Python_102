# Given a string, print the Caesar Cipher (or ROT13) of that string. What is Caesar Cipher? http://practicalcryptography.com/ciphers/caesar-cipher/

# Use your solution to decipher the following text: "lbh zhfg hayrnea jung lbh unir yrnearq"

ciphertext = "lbh zhfg hayrnea jung lbh unir yrnearq"
def rot13(ciphertext):
    result = ""
    for v in ciphertext:
        c = ord(v)
        if c >= ord('a') and c <= ord('z'):
            if c > ord('m'):
               c-= 13
            else:
                c += 13
        elif c >= ord('A') and c <= ord('Z'):
            if c >= ord('M'):
                c -= 13
            else:
                c += 13
        result += chr(c)
    return result

print(rot13(ciphertext))

#Solved with the magic of Google