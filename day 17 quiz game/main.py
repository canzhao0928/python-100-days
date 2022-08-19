from question_model import Question
from quiz_brain import QuizBrain
import requests



url="https://opentdb.com/api.php?amount=10&category=9&difficulty=easy&type=boolean"
question_data = requests.get(url).json()["results"]

question_bank = []
for data in question_data:
    question=Question(data["question"],data["correct_answer"])
    question_bank.append(question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    answer = quiz.next_question()

print(f"You've completed the quiz.\nYour final score was: {quiz.score}/{quiz.question_num}")
