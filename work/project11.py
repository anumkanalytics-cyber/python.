#Simple Quiz game
question_1 = "Which symbol is used to create comment in python?"
answer_1 = "#"
question_2 = "Which data type is used to store text?"
answer_2 = "string"
question_3 = "What does remove() do in python?"
answer_3 = "remove value"
question_4 = "What is the symbol used in an operator to know if the value is greater or equal to the other value?"
answer_4 = ">="
question_5 = "What does append() do in python?"
answer_5 = "add value"
questions = [question_1, question_2, question_3, question_4, question_5]
answers = [answer_1, answer_2, answer_3, answer_4, answer_5]
score = 0
for i in range(len(questions)):
    user_answer = input(questions[i] + " ")
    if user_answer.lower() == answers[i].lower():
        score += 1
        print("Correct!")
    else:
        print("Wrong!")
print("Your score:", score, "/", len(questions))