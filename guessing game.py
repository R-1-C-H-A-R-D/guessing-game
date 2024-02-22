secret_number = 10
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input("Try and guess a number from 0 to 10: "))
    guess_count += 1
    if guess == secret_number:
        print ("You won")
        break
else:
    print ("Sorry, you failed!")