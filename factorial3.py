# using recursive function
# function calling the function in the body of the func is called recursive func

def fact(n) :
    if n == 0 :
        return 1
    else :
        return n * fact(n-1)
        
factFor = int(input('Enter Number You Want To Find Factorial : '))
result = fact(factFor)
print('Factorial of', factFor, 'is', result)
