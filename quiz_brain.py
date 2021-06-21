
class QuizBrain:
    def __init__(self,ques_list):
        self.ques_num = 0
        self.score = 0
        self.ques_list = ques_list
        
    def still_has_ques(self):
        return self.ques_num < len(self.ques_list)
        
    def next_ques(self):
        curr_ques = self.ques_list[self.ques_num]
        self.ques_num += 1
        user_answer = input("Q.{} {} (True/False):\n".format(self.ques_num,curr_ques.text))
        self.check_answer(user_answer,curr_ques.answer)
               
    def check_answer(self,user_answer,correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!!")
        elif user_answer.lower() != correct_answer.lower():
            print("You got it wrong.")
        print("Your current score is {}/{}.".format(self.score,self.ques_num))
        print("\n")
