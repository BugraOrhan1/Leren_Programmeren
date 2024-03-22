def check_even(number):
    if number % 12 == 0:
          return True  
    return False

GETALLEN_REEKS = (2,7,15,25,24,28,17,420,8,3,20)

even_numbers_ = filter(check_even, GETALLEN_REEKS)
even_numbers = list(even_numbers_)
print(even_numbers)

