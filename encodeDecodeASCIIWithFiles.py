import os

import json


def encodeString(stringVal):
    encodedList = []
    prevChar = None
    count = 0
    for char in stringVal:
        if prevChar != char and prevChar is not None:
            encodedList.append((prevChar, count))
            count = 0
        prevChar = char
        count = count + 1
    encodedList.append((prevChar, count))
    return encodedList

def decodeString(encodedList):
    decodedStr = ''
    for item in encodedList:
        try:
            decodedStr = decodedStr + item[0] * item[1]
        except:
            print(item)
    return decodedStr



def encodeFile(filename, newFilename):
    # Open file to read
    with open(filename) as f:
        data = encodeString(f.read())
    
    # Format characters and count based on data read in
    data = [f'{char}|{count}' for char, count in data]

    # Create new file and append newly formatted data for encoding
    with open(newFilename, 'w') as f:
        f.write('~'.join(data))

def decodeFile(filename):
    # Open encoded file
    with open(filename) as f:
        data = f.read()
    
    # Parse encoded data to reconstruct image
    pairs = data.split('~')
    pairs = [p.split('|') for p in pairs]
    pairs = [(p[0], int(p[1])) for p in pairs]
    return decodeString(pairs)



# Checking compression by comparing original file with encoded file
print(f'Original file size: {os.path.getsize("10_04_challenge_art.txt")}')

encodeFile('10_04_challenge_art.txt', '10_04_challenge_art_encoded.txt')

print(f'New file size: {os.path.getsize("10_04_challenge_art_encoded.txt")}')


# Decoding from encoded file
print(decodeFile('10_04_challenge_art_encoded.txt'))


