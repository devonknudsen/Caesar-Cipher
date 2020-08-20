#######################################################
# Name: Devon Knudsen
# Date: 23 March 2020
# Assignment: Et tu, Brute?
# Written in Python 3
#######################################################

from sys import stdin

# the alphabets
ALPHABET = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789`~!@#$%^&*()-_=+[{]}\|;:'\",<.>/? "
# ALPHABET = " -,;:!?/.'\"()[]$&#%012345789aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxyYzZ"

# the dictionary
DICTIONARY_FILE = "dictionary.txt"

# threshold for the acceptable percentage of words
# currently = 30%
THRESHOLD = 0.5
        
# shifts a copy of the alphabet based on a given shift number
# returns a version of deciphered text based on the shifted alphabet
def rot(cTxt, shift):
    sAlphabet = []
    for char in ALPHABET:
        sAlphabet.append(char)
    
    # shifts the copied alphabet
    for i in range(shift):
        temp = ALPHABET[len(ALPHABET) - i - 1]
        sAlphabet.remove(ALPHABET[len(ALPHABET) - i - 1])
        sAlphabet.insert(0, temp)
    sAlphabet = "".join(sAlphabet)
    
    dTxt = ""
    # deciphers the cipher text
    for j in range(len(cTxt)):
        if(cTxt[j] in sAlphabet):
            cIndx = sAlphabet.index(cTxt[j])
            dTxt += ALPHABET[cIndx]
        else:
            dTxt += cTxt[j]
            
    return dTxt
    
# MAIN
file = open(DICTIONARY_FILE, "r")
dictionary = file.read().rstrip("\n").lower().split("\n")
file.close()

cipherTxt = stdin.read().rstrip("\n")

for i in range(len(ALPHABET)):
    pTxt = rot(cipherTxt, i)
    words = pTxt.split(" ")
        
    count = 0
    for word in words:
        if word in dictionary:
            count += 1
        
    if((count/len(words)) >= THRESHOLD):
        print("SHIFT: {}".format(len(ALPHABET) - i))
        print(pTxt)