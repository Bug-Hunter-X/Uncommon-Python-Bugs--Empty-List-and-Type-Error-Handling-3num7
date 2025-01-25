def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list
    total = sum(numbers)
    return total / len(numbers)

# Example usage with an empty list
average = calculate_average([])
print(f"Average: {average}")
#Example usage with a list containing non-numbers
average = calculate_average([1,2,'a'])
print(f"Average: {average}")