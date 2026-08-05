num = int(input("Enter a number: "))
count = 0 # count always starts at 0 because we haven't counted any digits yet
while num !=0:
    num = num // 10  # remove one digit from the end
    count += 1       # add 1 to the count each time