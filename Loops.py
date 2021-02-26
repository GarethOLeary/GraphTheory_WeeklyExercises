#Gareth O'Leary
#Python Basics

def factorial(n):
    """Number to calculate factorial of."""
    #Deal with negative inputs
    if n < 1:
        m = -n
    else:
        m = n
    #The running total - eventually the factorial
    total = 1
    # Loop to do the multiplications
    while m > 0:
        total = total * m
        m = m -1
    #return the answer
    if n < 1:
        return -total
    else:
        return total

#Test the function
n = -20
# Calculate factorial of n
print(f"The factorial of {n} is {factorial(n)}.")