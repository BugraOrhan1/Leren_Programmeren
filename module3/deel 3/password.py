import random
import string

def genereer_wachtwoord():
    wachtwoord = ""

    aantal_hoofdletters = random.randint(2, 6)
    hoofdletters = random.sample(string.ascii_uppercase, aantal_hoofdletters)

    kleine_letters = random.sample(string.ascii_lowercase, 8)

    speciale_tekens = random.sample("@#$%&_?", 3)

    aantal_cijfers = random.randint(4, 7)
    cijfers = random.sample(string.digits, aantal_cijfers)

    wachtwoord_delen = hoofdletters + kleine_letters + speciale_tekens + cijfers

    while len(wachtwoord_delen) < 24:
        wachtwoord_delen.append(random.choice(string.ascii_lowercase))

    random.shuffle(wachtwoord_delen)

    wachtwoord = "".join(wachtwoord_delen)

    if (
        wachtwoord[1] in string.ascii_uppercase
        or wachtwoord[-1] in string.ascii_lowercase
        or wachtwoord[0] in "@#$%&_?"
        or wachtwoord[-1] in "@#$%&_?"
        or wachtwoord[:3].isdigit()
    ):
        return genereer_wachtwoord()

    return wachtwoord

wachtwoord = genereer_wachtwoord()
print(wachtwoord)

