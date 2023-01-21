from random import randrange
searched = randrange(0, 1000)

print("Guess the number! 0 - 1000")

while searched == searched:
    n = int(input("Guess! "))
    if (n > searched):
        print("Too much!")
        continue
    elif (n < searched):
        print("Try a higher  number!")
        continue
    elif (n == searched):
        print("Yes! That's the one!", searched)