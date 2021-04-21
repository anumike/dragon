alphabet ="ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
stringToEncrypt = input("plase, write message:")
stringToEncrypt = stringToEncrypt.upper()
shiftAmont = int(input("plase write numeric(1,32)"))
encryptedString = ""

for currentCharacter in stringToEncrypt:
    position = alphabet.find(currentCharacter)
    newPosition = position + shiftAmont
    encryptedString = encryptedString + alphabet[newPosition]
print("your encryption message:", encryptedString)
