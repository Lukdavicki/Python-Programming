from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

data = question_data
question_bank = []
for q_data in data:
    q_text = q_data["text"]
    q_answer = q_data["answer"]
    new_question = Question(q_text, q_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
quiz.next_question()