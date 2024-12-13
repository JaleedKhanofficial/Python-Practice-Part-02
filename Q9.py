# Write a program to input a string and count the number of vowels (a, e, i, o, u) using a loop.

print("** Count Vowels in a String **")
string = str(input("Enter String : "))
count = 0

words=string.lower()
for word in words:
    if word == 'a' or word == 'e' or word == 'i' or word == 'o' or word == 'u':
        count += 1
print(count)