def monkey_count(n):
    lijst = []
    teller = 1
    for _ in range(n):
        lijst.append(teller)
        teller += 1
    return lijst

resultaat = monkey_count(10)
print(resultaat)
