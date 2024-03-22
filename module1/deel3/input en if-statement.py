
a = int(input("Voer het getal a in? "))
b = int(input("Voer het getal b in? "))
Min = a
Max = a

if a > b:
    Max = a
    Min = b
    print("a is het grootste getal:", Max)
elif a < b:
    Max = b
    Min = a
    print("a is het kleinste getal:", Min)
else:
    print("a en b zijn even groot")


print("Het minimum is:", Min)
print("Het maximum is:", Max)