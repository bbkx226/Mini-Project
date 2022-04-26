import random

ans = input("Type a number: ")

if ans.isdigit():
    ans = int(ans)

    if ans <= 0:
        print('Please type a number larger than 0. ')
        quit()

else:
    print("Please type a number. ")
    quit()

random_number = random.randint(0, 11)
guesses = 0
while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number next time. ")
        continue
    
    if user_guess == random_number:
        print("You got it! ")
        break
    elif user_guess > random_number:
        print("You were above the number! ")
    else:
        print("You were below the number! ")

print("You got it in ", guesses, "guesses")
