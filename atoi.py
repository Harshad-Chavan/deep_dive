def atoi(s):
    s = s.strip()  # Remove leading and trailing whitespace
    if not s:
        return 0  # Return 0 for empty string

    result = 0
    sign = 1  # Initialize the sign as positive

    # Check for a sign character ('+' or '-') at the beginning
    if s[0] in ('+', '-'):
        if s[0] == '-':
            sign = -1  # If negative sign is present, set the sign to -1
        s = s[1:]  # Remove the sign character

    for char in s:
        if char.isdigit():
            digit = ord(char) - ord('0')
            result = result * 10 + digit
        else:
            break  # Stop parsing if a non-digit character is encountered

    # Apply the sign to the result
    result *= sign

    # Ensure the result is within the 32-bit signed integer range
    INT_MAX = 2**31 - 1
    INT_MIN = -2**31
    if result > INT_MAX:
        return INT_MAX
    elif result < INT_MIN:
        return INT_MIN
    else:
        return result

# Example usage:
input_str = "   -42"
result = atoi(input_str)
print(result)
