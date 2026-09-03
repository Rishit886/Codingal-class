# define function to calculate cube
def cube(num):
    return num**3

# define a function which will excecute cube function if the user entered number is divisible by 3
def by_three(num):
    if num%3==0:
        return cube(num)
    else:
        return False
# display result
print(by_three(9))
print(by_three(4))