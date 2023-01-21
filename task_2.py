print("Write down even and positive numbers to add!")

result = 0
i = 0

while i < 3:
    n = int(input("Enter number = "))
    if ((not(n % 2 == 0)) and n > 0):
        print("It was supposed to be an even number!")
        continue
    elif (n < 0):
        print("It was supposed to be a positive number!")
        continue
    elif (n > 0 and n / 2):
        result += n
        i += 1
print("Addition result: ", result)