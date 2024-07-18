print("welcome to Amir's frist simple encryption program!")
print("it's Caesar Cipher")

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
def encrypt(text, shift):

    txl = ""
    for c in text:
        if c==" " or c=="!" or c== "?" :
            txl+=c
        else :
            oindex = alphabet.index(c)
            if oindex + shift > 25:

                oindex = (oindex + shift) % 26
            else:
                oindex += shift
            txl += alphabet[oindex]
    print(txl)


def decrypt(text, shift):
    txl = ""
    for c in text :
        if c==" " or c=="!" or c== "?" :
            txl+=c
        else :
            oindex=alphabet.index(c)
            if oindex-shift < 0 :
                shift=shift%26
                oindex=oindex-shift
            else :
                oindex-=shift
            txl+=alphabet[oindex]
    print(txl)

while True :

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

    if direction=='encode' :
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        encrypt(text,shift)
    elif direction=='decode' :
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        decrypt(text,shift)
    else :
        print(" invalid input ! ")
