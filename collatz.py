# Making the simplest impossible math problem (with error handling)

def collatz(number):
    if number % 2 == 0:
        return number // 2
    return 3 * number + 1


while 1:
    try:
        user_number = int(input('Please input a positive integer: \n'))
        if user_number < 1:
            continue
        break
    except ValueError:
        continue

while 1:
    if collatz(user_number) == 1:
        print(1)
        break
    print(collatz(user_number))
    user_number = collatz(user_number)
