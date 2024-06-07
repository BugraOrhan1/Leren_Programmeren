def genereer_reeks():
    reeks = "1"
    while "33" not in reeks:
        nieuwe_reeks = ""
        aantal = 1
        for i in range(1, len(reeks)):
            if reeks[i] == reeks[i-1]:
                aantal += 1
            else:
                nieuwe_reeks += str(aantal) + reeks[i-1]
                aantal = 1
        nieuwe_reeks += str(aantal) + reeks[-1]
        reeks = nieuwe_reeks
        print(reeks)

genereer_reeks()
