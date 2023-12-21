import sys

def allPrimesUpTo(num):
    # Assuming input greater than 2, 2 will always be prime existing in List
    primes = [2]
    
    # First iterate through numbers from 3 to Input
    for number in range(3, num):
        # For each number calculate the Sqrt 
        sqroot = number ** 0.5
        # For each item in primes check to see if it is divisable by the prime numbers
        for factor in primes:
            if number % factor == 0:
                # Not Prime skip to the next number
                break
            if factor > sqroot:
                # Prime Number was found append it to the list and iterate to next number
                primes.append(number)
                break

    return primes

# This Code below can be run via command line with single argument
if len(sys.argv) > 2:
    print("You have given more arguments to this function than it can handle. Here is the result of the first argument.")
try:
    temp = int(sys.argv[1])
except Exception:
    print(f'Argument {sys.argv[1]} contains non-numerical values and is not an acceptable as an input.')
else:
    print(f'Here is a list of primes for {temp}:')
    print(allPrimesUpTo(temp))
    

# This Code below can be used to ignore argument limit and run it for each number given in command line
for item in sys.argv[1::]:
    try:
        temp = int(item)
    except Exception:
        print(f'Argument {item} contains non-numerical values and is not an acceptable as an input.')
    else:
        print(f'Here is a list of primes for {temp}:')
        print(allPrimesUpTo(temp))
        