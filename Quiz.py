questions = ("How many elements are in the periodic table?:",
             "What is the most dangerous animal?:",
             "How many bones are in the human body:",
             "What was hulks original color?:")






options = (("A. 116", "B. 117", "C. 118", "D. 119"),
           ("A. Elephant", "B. Mosquito", "C. Hippo", "D. Buffalo Bison"),
           ("A. 240", "B. 218", "C. 400", "D. 206"),
           ("A. Green", "B. Red", "C. Grey", "D. Purple"))

answers = ("C", "B", "D", "C")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("-------------------------")
    print(question)
    for option in options [question_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("Correct!")
    else:
        print("Incorrect!")
        print(f"{answers[question_num]} is the correct answer.")
    question_num += 1


print("-------------------------")
print("      RESULTS     ")
print("-------------------------")

print("answers:", end="")
for answer in answers:
    print(answer, end="")
print()

score = int(score / len(questions) * 100)
print(f"Your score is {score}%")