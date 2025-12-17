# Example1 : indenation & whitespace
def calculate_average(numbers):
    sum = 0
    for num in numbers:
        sum += num
    average = sum / len(numbers)
    return average
print(calculate_average([10, 20, 30, 40, 50]))