def check_string_properties(s):
    print(any(c.isalnum() for c in s))  # Check for alphanumeric characters
    print(any(c.isalpha() for c in s))  # Check for alphabetical characters
    print(any(c.isdigit() for c in s))  # Check for digits
    print(any(c.islower() for c in s))  # Check for lowercase characters
    print(any(c.isupper() for c in s))  # Check for uppercase characters

if __name__ == '__main__':
    s = input()
    check_string_properties(s)
