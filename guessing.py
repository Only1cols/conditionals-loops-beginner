import random

secret_number = random.randint(2, 9)

print("welcome to the guessing game!")
print("I'm thinking of a number between 1 and 10. ")

attempts = 0
while True:
    guess = int(input("guess a number between 1 and 10: "))

    if guess == secret_number:
        print("congratulations, you guessed it")
        break

    elif guess < secret_number:
        print("incorrect guess,to low")

    elif guess > secret_number:
        print("incorrect guess, too high")

    attempts += 1
    if attempts >= 2:
        print(
            f"sorry, you've used all your attempts. The number was {secret_number}.")
        break
