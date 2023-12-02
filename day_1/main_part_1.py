import string

# Open file 
with open('input.txt', 'r') as input_file:
    calibration_values = input_file.readlines()

result = 0
str_digits = [str(digit) for digit in string.digits]
for calibration_value in calibration_values:
    nums = [c for c in calibration_value if c in str_digits]
    first_digit = nums[0]
    last_digit = nums[-1]
    value = int(first_digit + last_digit)
    result += value

print(result)