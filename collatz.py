# Making the simplest impossible math problem

def collatz(number):
    if number % 2 == 0:
        return number // 2
    return 3 * number + 1

user_number = int(input('Please input a positive integer: \n'))

while 1:
    if collatz(user_number) == 1:
        print(1)
        break
    print(collatz(user_number))
    user_number = collatz(user_number)
