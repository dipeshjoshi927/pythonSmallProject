#-----------------------
def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("-----------------------")
        print(key)
        for i in options[question_num-1]:
           print(i)
        guess = input("Enter your choice(A,B,C,D):")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key),guess)
        question_num +=1 
    display_score(correct_guesses,guesses)
#-----------------------
def check_answer(answer,guess):
    if answer == guess:
        print("Correct")
        return 1
    else:
        print("Wrong")
        return 0
#-----------------------
def display_score(correct_guesses,guesses):
    print("-----------------------")
    print("RESULTS!!")
    print("-----------------------")
    print("Answer:",end=" ")
    for key in questions:
        print(questions.get(key),end=" ")
    print()    
    print("Guesses:",end=" ")
    for i in guesses:
        print(i,end=" ")
    print()    

    score = (correct_guesses/len(questions))*100
    print("Your score is:",score,"%")
#-----------------------
def play_again():
    response = input("Do you want to play again?(yes or no):")
    response = response.upper()
    if response == "YES":
        return True
    else: 
        return False

#----------------------- 

questions ={
    "Who created Python?: ": "A",
    "What year was Python created?: ":"B",
    "Python is tributed to which comedy group?: ":"C",
    "Is the Earth round?: " :"A"
}

options =[["A. Guido van Rossum","B. Elon musk","C. Bill gates","D. Mark Zukurberg"],
         ["A. 1989","B. 1991","C. 2000","D. 2016"],
         ["A. Lovely Island","B. smoosh","C. monty Python","D. SNL"],
         [ "A.True","B. nah","C. Oh god no","D. Why are you gay"]
]

new_game()

while play_again():
    new_game()

print("Bye!!!")


