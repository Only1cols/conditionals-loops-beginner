# guess game using while loop
secret_number = 10
guess = int(input("guess a number between 1 and 10: "))
while guess != secret_number:
    print("incorrect, try again")
    guess = int(input("guess a number between 1 and 10: "))

    if guess == secret_number:
        print("correct!!!")
        break
