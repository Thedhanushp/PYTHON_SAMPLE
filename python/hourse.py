name = input("whats your name : ")
# match
match name:
    case "Harry" | "Ron" | "Kevin":# | means or
        print("Gryffinder")
    case "Hermione":
        print("Gryffinder")
    case _:
        print("Who?")
    ####******
if name == "Harry" or name == "Hermione" or name == "Ron":
    print("Gryffinder")
elif name == "Hermino":
    print("Gryffinder")
elif name == "Ron":
    print("Gryffinder")
elif name == "Draco":
    print("Slytherin")
else:
    print("Who?")