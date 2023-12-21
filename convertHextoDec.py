import sys

hexNumbers = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
}

# Converts a string hexadecimal number into an integer decimal
# If hexNum is not a valid hexadecimal number, returns None
def hexToDec(hexNum):
    for char in hexNum:
        if char not in hexNumbers:
            return None
    
    exponent = 0
    result = 0
    for char in hexNum[::-1]:
        result = result + (int((16 ** exponent) * hexNumbers[char])) 
        exponent = exponent + 1
                
    return result

# This Code below can be run via command line with single argument
if len(sys.argv) > 2:
    print("You have given more arguments to this function than it can handle. Here is the result of the first argument.")
temp = hexToDec(sys.argv[1])
if temp:
    print(temp)
else:
    print(f'Argument {sys.argv[1]} contains values that do not exist in Hexidecimal.')

# This Code below can be used to ignore argument limit and run it for each number given in command line
for item in sys.argv[1::]:
    temp = hexToDec(item)
    if temp:
        print(f'Converted Hexidecimal value {item} into Decimal valude {temp}')
    else:
        print(f'Argument {item} contains values that do not exist in Hexidecimal.')