from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for q_set in question_data:
    q_text = q_set["text"]
    q_answer = q_set["answer"]
    # Question 객체 생성
    new_question = Question(q_text, q_answer)
    # Question 객체들로 구성된 리스트 생성
    question_bank.append(new_question)
    # 아래의 형식을 띄는, Question 객체들로 구성된 question_bank
    # question_bank = [
    #     Question(q_text1, q_answer1)
    #     Question(q_text2, q_answer2)
    #     Question(q_text3, q_answer3)
    # ]

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()
print("You've completed the quiz.")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")

