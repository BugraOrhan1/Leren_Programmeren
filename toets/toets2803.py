# zorg ervoor dat test_lib.py in dezelfde directory zit als de toets
from test_lib import test, report

def is_even(getal: int) -> bool:
    return getal % 2 == 0 #klaar

def get_even_list(lijst: list) -> list:
    even_getallen = []
    for getal in lijst:
        if getal % 2 == 0:
            even_getallen.append(getal)
    return even_getallen #klaar


def omgedraaid_even(lijst: list) -> list:
    even_getallen = get_even_list(lijst)
    even_getallen.reverse()
    return even_getallen#klaar

def aantal_even_getallen(lijst: list) -> int:
    count = 0
    for getal in lijst:
        if is_even(getal):
            count += 1
    return count#klaar

def is_palindroom(woord: str) -> bool:
    omgekeerd_woord = ''
    for letter in woord:
        omgekeerd_woord = letter + omgekeerd_woord
    return woord == omgekeerd_woord#klaar

def omgedraaid(lijst: list) -> list:
    omgekeerde_lijst = []
    for item in reversed(lijst):
        omgekeerde_lijst.append(item)
    return omgekeerde_lijst#klaar

def lijsten_samenvoegen(lijst1: list, lijst2: list) -> list:
    return lijst1 + lijst2

def aantal_palindromen(lijst: list) -> int:
    count = 0
    for woord in lijst:
        if is_palindroom(woord):
            count += 1
    return count#klaar

def aantal_even_getallen_op_even_index(lijst: list) -> int:
    count = 0
    for i in range(len(lijst)):
        if i % 2 == 0 and is_even(lijst[i]):
            count += 1
    return count#klaar

# opdracht 1a
# bepaal of een getal even is.
# schrijf minimaal 2 extra testen. De eerste 2 testcases zijn weggegeven.
expected = True
result = is_even(2)
test('Opdracht 1a (test 1) is correct', expected, result)

expected = False
result = is_even(3)
test('Opdracht 1a (test 2) is correct', expected, result)

expected = True
result = is_even(0)
test('Opdracht 1a (test 3) is correct', expected, result)

expected = False
result = is_even(101)
test('Opdracht 1a (test 4) is correct', expected, result)



# vraag 1b

expected = [2,4]
result = get_even_list([1,2,3,4,5])
test('Opdracht 1b (test 1) is correct', expected, result)

expected = [24, 16, 12, 2]
result = get_even_list([27, 15, 24, 16, 7, 12, 1, 2])
test('Opdracht 1b (test 2) is correct', expected, result)

expected = [36, 26, 32, 36]
result = get_even_list([36, 26, 32, 36, 21, 11, 19])
test('Opdracht 1b (test 3) is correct', expected, result)

expected = [26, 16, 6]
result = get_even_list([26, 11, 16, 6])
test('Opdracht 1b (test 4) is correct', expected, result)

# vraag 2

expected = 2
result = aantal_even_getallen([1,2,3,4,5])
test('Opdracht 2 (test 1) is correct', expected, result)

expected = 4
result = aantal_even_getallen([1,2,3,4,5,6,7,8,9])
test('Opdracht 2 (test 2) is correct', expected, result)

expected = 2
result = aantal_even_getallen([1,2,8,9])
test('Opdracht 2 (test 3) is correct', expected, result)

# vraag 3

expected = [5, 4, 3, 2, 1]
result = omgedraaid([1, 2, 3, 4, 5])
test('Opdracht 3 (test 2) is correct', expected, result)

expected = ['c', 'b', 'a']
result = omgedraaid(['a', 'b', 'c'])
test('Opdracht 3 (test 4) is correct', expected, result)

expected = ['z', 'q', 'r']
result = omgedraaid(['r', 'q', 'z'])
test('Opdracht 3 (test 4) is correct', expected, result)

# vraag 4

expected = [4, 2]
result = omgedraaid_even([1, 2, 3, 4, 5])
test('Opdracht 4 (test 1) is correct', expected, result)

expected = [6, 4, 2]
result = omgedraaid_even([1, 2, 3, 4, 5, 6])
test('Opdracht 4 (test 2) is correct', expected, result)

expected = [8, 6, 4, 2]
result = omgedraaid_even([1, 2, 3, 4, 6, 8])
test('Opdracht 4 (test 3) is correct', expected, result)

# vraag 5

expected = [1, 2, 3, 4, 5, 6]
result = lijsten_samenvoegen([1, 2, 3],  [4, 5, 6])
test('Opdracht 5 (test 1) is correct', expected, result)

expected = [1, 2, 3, 4, 5, 6, 7, 8]
result = lijsten_samenvoegen([1, 2, 3],  [4, 5, 6, 7, 8])
test('Opdracht 5 (test 2) is correct', expected, result)

expected = ['a', 'b', 'c', 'd', 'e']
result = lijsten_samenvoegen(['a', 'b'], ['c', 'd', 'e'])
test('Opdracht 5 (test 3) is correct', expected, result)

# vraag 6
expected = True
result = is_palindroom('anna')
test('Opdracht 6 (test 1) is correct', expected, result)

expected = False
result = is_palindroom('hello')
test('Opdracht 6 (test 2) is correct', expected, result)

expected = True
result = is_palindroom('racecar')
test('Opdracht 6 (test 3) is correct', expected, result)

# vraag 7
expected = 3
result = aantal_palindromen(['anna', 'lepel', 'developer', 'parterretrap', 'test'])
test('Opdracht 7 (test 1) is correct', expected, result)

expected = 3
result = aantal_palindromen(['level', 'stats', 'python', 'deified'])
test('Opdracht 7 (test 2) is correct', expected, result)

expected = 1
result = aantal_palindromen(['hello', 'world', 'madam'])
test('Opdracht 7 (test 3) is correct', expected, result)

# vraag 8

expected = 3
result = aantal_even_getallen_op_even_index([2, 3, 4, 5, 6])
test('Opdracht 8 (test 1) is correct', expected, result)

expected = 0
result = aantal_even_getallen_op_even_index([1, 2, 3, 4, 5, 6])
test('Opdracht 8 (test 2) is correct', expected, result)

expected = 2
result = aantal_even_getallen_op_even_index([6, 8, 10,])
test('Opdracht 8 (test 3) is correct', expected, result)

report()









