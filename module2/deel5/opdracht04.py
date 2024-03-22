import random
from fruitmand2 import fruitmand

aantal = int(input("Voer het aantal in: "))

for _ in range(aantal):
    random_fruit = random.choice(fruitmand)
    print(random_fruit['name'])
