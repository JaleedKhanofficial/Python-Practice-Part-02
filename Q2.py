# Write a program to calculate the sum of the first n natural numbers using a while loop. (n should be taken as input.)

print("**Sum of Natural Number**")
n = input("Enter Number: ")

try:
    num = int(n)
    sum = 0
    update = 0
    while num >= update :
        sum = sum + update     # here is some of all natural numbers to num(takes from user)
        print(f"At index {update} the value is {sum}")
        update +=1
    print("The Total Sum is:", sum)
except:
    print("Invalid Input")  # if user enters a non-numeric value, it will print

