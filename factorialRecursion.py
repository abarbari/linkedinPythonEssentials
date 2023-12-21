import sys

# Returns the value of the factorial of num if it is defined, otherwise, returns None
def factorial(num):
    if type(num) is not int:
        return None
    if num < 0:
        return None
    if num == 0:
        return 1
    
    return num * factorial(num - 1)

# This Code below can be run via command line with single argument
if len(sys.argv) > 2:
    print("You have given more arguments to this function than it can handle. Here is the result of the first argument.")
print(factorial(int(sys.argv[1])))

# This Code below can be used to ignore argument limit and run it for each number given in command line
for item in sys.argv[1::]:
    print(f'Factorial of {item} is {factorial(int(item))}')

