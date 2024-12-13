# Write a program that takes a list of numbers as input and uses a while loop to find and print the first even number.

print("** Find The First Even Number **")

while True:
    n = input("Enter Number : ")
    num = int(n)
    if num % 2 == 0:
        print("The first even number is: ", num)
        break
