def average(numbers):
    if not numbers:
        raise ValueError("The list is empty")
    total = 0
    count = 0
    for number in numbers:
        total += number
        count += 1
    return total / count

def factorial(n):
    if n < 0:
        raise ValueError("Negative values are not allowed")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result