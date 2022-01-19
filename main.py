# python simple quiz start

#score
score = 0

#question 1
answer1 = input("who is youre teacher?")
if answer1 == "Mr.V" or answer1 == "Mr. Veldkamp":
    print("correct")
    score = score + 1
else:
    print ("incorrect")

#question 2
answer2 = input("whats 9 + 10?")
if answer2 == "21":
    print("correct")
    score = score + 1
else:
    print ("incorrect, idiot")

#output resul of quiz
print("youre score is " + str(score) + " / 2.")

if score == 2:
    print("youre did it :)")
elif score == 1:
    print("you kinda blow lol")
else:
    print("you stoopid")