L = [4,5,1,2,9,7,8,10,8]
print("Original List:", L)

count = 0

for i in L:
    count += 1

avg = sum(L) / count

print("Sum =", count)
print("Average =", avg)

L.sort()

print("Smallest element is:", L[0])

print("Largest element is:", L[-1])