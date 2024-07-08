import random
import math

lower = int(input("Enter the lower boundary: "))
upper = int(input("Enter the upper boundary: "))

x = random.randint(lower, upper)
total_chances = math.ceil(math.log(upper - lower + 1, 2))
print("\n\tYou only have ", total_chances, " chances to guess the integer!\n")

count = 0
flag = False
while count < total_chances:
    count += 1
    guess = int(input("guess a number : "))
    if x == guess:
        print("you got it!")
        flag = True
        break 
    elif x > guess:
        print("too small i'm afraid")
    elif x < guess:
        print("you guessed too high!")

if not flag:
    print("\nThe number is %d " % x)
    print("\tBetter luck next time!")