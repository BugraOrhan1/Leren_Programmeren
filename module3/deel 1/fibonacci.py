aantal_getallen = int(input("Voer het aantal Fibonacci-getallen in dat je wilt genereren: "))
fibonacci_reeks = [0, 1]

for i in range(2, aantal_getallen):
        volgende_getal = fibonacci_reeks[i-1] + fibonacci_reeks[i-2]
        fibonacci_reeks.append(volgende_getal)

laatste_twee_getallen = fibonacci_reeks[-2:]
gulden_snede = laatste_twee_getallen[-1] / laatste_twee_getallen[-2]

print("Fibonacci-reeks:", fibonacci_reeks)
print("De gulden snede is:", gulden_snede)


