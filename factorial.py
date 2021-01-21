def factorialB(n):                                          ### bruteforce method      ###
    product = 1
    if(n == 0):
        return product
    elif(n>0):
        for i in range(1, n + 1):
            product = product * i
        return product
    else:
        return "Enter a valid input"


def factorialR(n):                                      ### recursion method            ###
    product = 1
    if n == 0:
        product = 1
        return product
    if n >= 0:
        return n * factorialR(n-1)
    elif(n < 0):
        return "Enter a valid input"
n = int(input("Enter the number : "))
print(factorialR(n))