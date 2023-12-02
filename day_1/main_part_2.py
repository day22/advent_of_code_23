import string

# Map of spelled number to digit
string_to_int = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
}

# List of digits as strings
str_digits = [str(digit) for digit in string.digits]

# Read lines from input 
with open('input.txt', 'r') as input_file:
    calibration_values = input_file.readlines()

result = 0

# Find code for each line 
for calibration_value in calibration_values:

    # List to store all the values we find
    found_vals = []

    # Add first and last instance of each digit in the line as tuple to result (index, value)
    for digit in str_digits:
        # find leftmost 
        index = calibration_value.find(digit)
        if index >= 0: 
            found_vals.append((index, digit))

            # find right most if we line contains at least one instance 
            index = calibration_value.rfind(digit)
            if index >= 0: 
                found_vals.append((index, digit))

    # Add first and last instance of each spelled num in the line as tuple to result (index, value)
    for spelled_num in string_to_int:
        # find leftmost 
        index = calibration_value.find(spelled_num)
        if index >= 0: 
            found_vals.append((index, string_to_int[spelled_num]))

            # find rightmost  
            index = calibration_value.rfind(spelled_num)
            if index >= 0: 
                found_vals.append((index, string_to_int[spelled_num]))

    # Sort the found value using the index as key
    found_vals.sort(key=lambda a: a[0])

    # Join digits to make code and add to result
    first_num = found_vals[0][1]
    last_num = found_vals[-1][1]
    value = int(first_num + last_num)
    result += value

print(result)