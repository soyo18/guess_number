import random
secret_number = random.randint(1,100)
guess = input("please guess a number between 1 and 100: ")
guess_number = int(guess)
number_of_times = 1
if guess_number == secret_number:
    print("you guessed right!\nnumber_of_times is 1")
while guess_number != secret_number:
    if guess_number > secret_number:
        print("you guessed too big")
        guess = input("please guess a number between 1 and 100: ")
        guess_number = int(guess)
    else:
        print("you guessed too small")
        guess = input("please guess a number between 1 and 100: ")
        guess_number = int(guess)
    number_of_times += 1
print("you guessed right!\nnumber_of_times is ",number_of_times)
