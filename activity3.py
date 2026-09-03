def factorial(x):
    '''this is a recursive function to find the factorial of an integer'''

    if x == 0:
        return 1
    else:
        #calling function inside a function
        return x * factorial(x - 1)

# display result
print(factorial._doc__)
print("The facotorial of 0 is:", factorial(0))
print("The facotorial of 1 is:", factorial(1))
print("The facotorial of 2 is:", factorial(2))
print("The facotorial of 5 is:", factorial(5))
print("The facotorial of 10 is:", factorial(10))