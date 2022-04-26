print("Welcome to my quiz!")

play = input("Do you want to play?(yes or no) \n")
if play.lower() != "yes":
    quit()
print("Okay! Let's play.")
score = 0

answer = input("What does CPU stand for? \n")
if answer.lower() == "central processing unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does GPU stand for? \n")
if answer.lower() == "graphic processing unit":
    print('Correct!')
    score += 1
    
else:
    print("Incorrect!")

answer = input("What does RAM stand for? \n")
if answer.lower() == "random access memory":
    print('Correct!')
    score += 1

else:
    print("Incorrect!")

answer = input("What does PSU stand for? \n")
if answer.lower() == "power supply":
    print('Correct!')
    score += 1

else:
    print("Incorrect!")

print("You got " + str(score) + " question correct")
print("You got " + str((score/4) * 100) + " %")
