# Write a program that takes a string and two numbers (start and end) as input. Use slicing to extract and print the substring between these indices.

print("** Extract Substring **")
original_string = input("Enter a string: ")

# Take user input for start and end indices
try:
    start_index = int(input("Enter the start index: "))
    end_index = int(input("Enter the end index: "))

    # Extract and print the substring
    substring = original_string[start_index:end_index]
    print(f"The extracted substring is: {substring}")
except ValueError:
    print("Please enter valid integer indices.")

