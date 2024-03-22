car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  'prijs': 100
}

prijs_van_auto = car.get('prijs',15000)

print(prijs_van_auto)