import re

def  add(numbers):
      if numbers == '': return 0

    numbers = map(int, re.findall(r"-?\d", numbers))
    numbers = filter(lambda x: x < 1000, numbers)
    negative_number = filter(lambda x: x < 0, numbers)

    if negative_number:raise Exception('negatives not allowed' + str(negative_number))
    return sum(numbers)
    
