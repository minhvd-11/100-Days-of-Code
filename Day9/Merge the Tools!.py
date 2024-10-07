def merge_the_tools(string, k):
    # your code goes here
    # Iterate over the string in steps of k
    for i in range(0, len(string), k):
        # Get the substring of length k
        substring = string[i:i+k]
        # Use a dictionary to remove duplicates while maintaining order
        unique_chars = ''.join(dict.fromkeys(substring))
        # Print the result
        print(unique_chars)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)