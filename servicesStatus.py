import random
import time

servicesAreUp = True

def getData50():
    if servicesAreUp and random.random() < 0.5:
        return 'You got the data! That only happens 50% of the time!'

def getData25():
    if servicesAreUp and random.random() < 0.25:
        return 'You got the data! That only happens 25% of the time!'    

def getData10():
    if servicesAreUp and random.random() < 0.1:
        return 'You got the data! That only happens 10% of the time!'
    



# This tests the above commands retrying a max of 15 times to achieve the appropriate responses.
def getWithRetry(dataFunc):
    maxRetries = 15
    
    for _ in range(0, maxRetries):
        response = dataFunc()
        if response:
            return response
        

# Should return 'You got the data! That only happens 50% of the time!'
print(getWithRetry(getData50))

# Should return 'You got the data! That only happens 25% of the time!'
print(getWithRetry(getData25))

# Should return 'You got the data! That only happens 10% of the time!'
print(getWithRetry(getData10))



#This should cause all Services to be down and return None for the following commands
servicesAreUp = False

# Returns None
print(getWithRetry(getData50))

# Returns None
print(getWithRetry(getData25))

# Returns None
print(getWithRetry(getData10))



servicesAreUp = True

#Adding timing interference with getData Commands
def getData50():
    time.sleep(.1)
    if servicesAreUp and random.random() < 0.5:
        return 'You got the data! That only happens 50% of the time!'

def getData25():
    time.sleep(.1)
    if servicesAreUp and random.random() < 0.25:
        return 'You got the data! That only happens 25% of the time!'    

def getData10():
    time.sleep(.1)
    if servicesAreUp and random.random() < 0.1:
        return 'You got the data! That only happens 10% of the time!'
    
print(getWithRetry(getData50))

print(getWithRetry(getData25))

print(getWithRetry(getData10))
