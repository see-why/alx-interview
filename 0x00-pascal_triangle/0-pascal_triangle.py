import math

def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)

def combination(n, r):
    return int(factorial(n) / (factorial(r) * factorial(n-r)))

def generate_row(n):
    array = [1]
    if n == 2:
        array.append(1)
    elif n > 2:
        array += compute_coefficients(n-1) + [1]
    return array

def compute_coefficients(n):
    array = []
    stop_index = math.ceil(n/2)+1
    for i in range(1,stop_index):
        array.append(combination(n, i))

    reversed = array[::-1]

    result = array + reversed[1:] if n %2 == 0 else array + reversed[2:]
    return result

def pascal_triangle(n):
    result = []

    if n >= 1:
      for i in range(1,n+1):
          result.append(generate_row(i))

    return result