string = input("Enter a string: ")
character = input("Enter a character to count: ")
count = 0
# i=0
# while i<len(string):
#     if string[i]==character:
#         count+=1
#     i+=1
#print(count)

for i in string:
    if i.lower()==character.lower():
        count+=1
print(count)