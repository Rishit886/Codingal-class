n = int(input())

#1 The Loop Condition
while n > 0:

    #2 Grab a piece(The Remainder)
    last_digit = n % 2
    print("Found Digit", last_digit)

    #3 Update the number(Shrink It!)
    n = n // 2
    print("That number has been shrunk to", n)
    print("---" )