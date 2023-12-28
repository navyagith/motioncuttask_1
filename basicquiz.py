class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def display_question(self, question_num):
        question = self.questions[question_num]['question']
        options = self.questions[question_num]['options']
        
        print(f"\nQuestion {question_num + 1}: {question}")
        for i, option in enumerate(options, start=1):
            print(f"{i}. {option}")
    
    def check_answer(self, question_num, user_answer):
        correct_answer = self.questions[question_num]['answer']
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("Correct!")
        else:
            print(f"Sorry, that's incorrect. The correct answer is: {correct_answer}")

    def start_quiz(self):
        for i in range(len(self.questions)):
            self.display_question(i)
            user_choice = input("Enter your choice (1, 2, 3, etc.): ")
            self.check_answer(i, user_choice)
        
        print(f"\nQuiz completed! Your final score is: {self.score}/{len(self.questions)}")


# Sample quiz questions
quiz_questions = [
    {
        'question': 'What is the capital of France?',
        'options': ['Paris', 'Rome', 'Berlin'],
        'answer': 'Paris'
    },
    {
        'question': 'Which planet is known as the Red Planet?',
        'options': ['Mars', 'Jupiter', 'Venus'],
        'answer': 'Mars'
    },
    {
        'question': 'Who painted the Mona Lisa?',
        'options': ['Leonardo da Vinci', 'Pablo Picasso', 'Vincent van Gogh'],
        'answer': 'Leonardo da Vinci'
    }
]

# Create a quiz object and start the quiz
my_quiz = Quiz(quiz_questions)
my_quiz.start_quiz()
