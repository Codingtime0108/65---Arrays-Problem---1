#take an array then find out the missing number in the array, the array needs to be in a pattern

def find_missing_number(arr):
    n = len(arr) + 1   # since one number is missing
    total_sum = n * (n + 1) // 2
    actual_sum = sum(arr)
    return total_sum - actual_sum

# Example
arr = [1, 4, 3, 2, 6]
print(find_missing_number(arr))  # Output: 5