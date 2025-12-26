def process_numbers(numbers):
        total = sum(numbers)
        average =  total / len(numbers)
        minimum = min(numbers)
        maximum = max(numbers)
        return f"Total: {total}, Average: {average}, Min:{minimum}, Max:{maximum}"

result = process_numbers([1, 2, 3, 4, 5])
print(result)

float_result = process_numbers([1.75, 2.9 ,9.87, 1.38, 5.12, 1.4])
print(float_result)