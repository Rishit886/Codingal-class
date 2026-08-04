# take input from user 
num = int(input("Please enter a number: "))

# intialize sum
sum = 0

# find the sum of each cube digit
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10

# display the result
if num == sum:
    print(num, "is an Armstrong number")
else: 
    print(num, "is not an Armstrong number")