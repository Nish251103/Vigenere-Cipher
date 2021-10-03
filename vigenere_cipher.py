def new_alphabet(ch):
    ch = ch.lower()
    alph = 'abcdefghijklmnopqrstuvwxyz'
    new_alphabet = alph[alph.index(ch):] + alph[:alph.index(ch)]
    return new_alphabet
    
   
def encrypt(text, big_key):
    res = ''
    alph = 'abcdefghijklmnopqrstuvwxyz'
    i = 1
    for char in big_key:
        new = new_alphabet(char)
        for t in text:
            if alph.count(t) == 1 :
                res += new[alph.index(t)]
                text = text[i:]
                break
            elif alph.count(t.lower()) == 1:
                res += new[alph.index(t.lower())].upper()
                text = text[i:]
                break
            else:
                res += t
                text = text[i:]
                break
            i += 1    
    return res

while True:
    print("1. Encrypt")
    print("2. Decrypt")

    a = int(input("> "))

    if a==1:
        text1 = input("Encrypt : ")
        key = input("Key : ")

        if len(key) <= len(text1):
            big_key = key * (len(text1) // len(key)) + key[:len(text1) % len(key)]
            text_encrypt = encrypt(text1, big_key)
            print("Encrypted : ", text_encrypt)
        else:
            print('Error: Key is longer than the word.')

    elif a==2:
        text2 = input("Decrypt : ")
        key1 = input("Key : ")

        if len(key1) <= len(text2):
            big_key1 = key1 * (len(text2) // len(key1)) + key1[:len(text2) % len(key1)]
            text_decrypt2 = decrypt(text2, big_key1)
            print("Decrypted : ", text_decrypt2)
        else:
            print('Error: Key is longer than the word.')

    else:
        print("Invalid.")