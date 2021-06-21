from data import question_data
from ques_model import Question
from quiz_brain import QuizBrain

question_bank = []

for ques in question_data:
    ques_txt = ques['text']
    ques_ans = ques['answer']
    new_q = Question(ques_txt, ques_ans)
    question_bank.append(new_q)

quiz = QuizBrain(question_bank)

while quiz.still_has_ques():
    quiz.next_ques()
