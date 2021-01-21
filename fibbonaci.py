def fib(n):
    a, b = 0, 1
    if (n == 1) & (n > 0):
        print(a)
    elif n > 0:
        print(a)
        print(b)
    else:
        print("Enter a valid input")
    for i in range(2, n):
        c = a + b
        a = b
        b = c
        print(c)


n = int(input("Enter the numbers of elements of fibbonaci series you want to get : "))
fib(n)
