friends = {"Rishit": "9 March",
    "Ayushman": "15 July",
    "Ananya": "22 November",
    "Priya": "5 January",
    "Harry": "30 September",
}
    

name = input("Enter friend's name: ")

birthday = friends.get(name)
if birthday:
    print(f"{name}'s birthday is {birthday}.")
else:
    print("Friend not found.")
