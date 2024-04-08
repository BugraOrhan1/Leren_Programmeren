groen = 0
rijp = 1
rot = 2

appels = [groen, rijp, rijp, rot, groen, rot, rijp, rijp, rijp, rot, rijp, groen]

groene_appels = []
for appel in appels:
    if appel == groen:
        groene_appels.append(appel)


for appel in appels:

percentage_rijpe_appels = (len(appels) / len(groene_appels)) * 100

print("Groene appels:", groene_appels)
print("Rijpe appels zonder rot:", appels)
print("Percentage rijpe appels:", percentage_rijpe_appels)
