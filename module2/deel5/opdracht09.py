from fruitmand2 import fruitmand

mylist= []
for fruit in fruitmand:
    if fruit['name'] == 'druif':
        fruitmand.remove(fruit)



for fruit in fruitmand:
    if not fruit['color'] in mylist:
        mylist.append(fruit['color'])

print(mylist)