# a for loop can also be used to iterate a list, tuple, string or even a dictionary..

name = "Elvis"

for letter in name:
    if letter == "v":
        print("this is letter v")
    else:
        print(letter)

# below is a list of counties
counties = ["Nairobi", "Mombasa", "Kisumu", "Kajiado", "Machakos", "Meru", "Embu"]

print(counties)

for county in counties:
    print(county)

for county in counties:
    if "Nairobi" in counties:
        print("the county is part of the list")
        break
    else:
        print ("the county is not part of the list")

player = {
    "name": "mbape",
    "age" : 25,
    "teas" : ["psg", "Monaco", "france",],
    "nationality" : "france"
}

for key in player:
    print(key)

for value in player:
    print(player(value))

# loop through the teams the player has played for