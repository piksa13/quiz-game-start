from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    question_bank.append(Question(text = question["question"], answer = question["correct_answer"]))

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
print("You ran out of questions")
print(f"Your final score is {quiz.current_score}/{len(quiz.question_list)}")