def check_even(number):
    if number % 2 == 0 and number > 12:
          return True  
    return False

GETALLEN_REEKS = (2,7,15,25,24,28,17,420,8,3,20)

even_numbers_ = filter(check_even, GETALLEN_REEKS)
even_numbers = tuple(even_numbers_)
print(even_numbers)



