factFor = int(input('Enter Number You Want To Find Factorial : '))
result = 1
if factFor == 0 :
    print('Factorial of', factFor, 'is', result)
else :
    for i in range(1, factFor + 1) :
        result *= i
    print('Factorial of', factFor, 'is', result)
