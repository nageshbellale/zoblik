# -------- Question Class --------
class Question:
    def __init__(self, question, options, correct_option):
        self.question = question
        self.options = options  # List of answer options
        self.correct_option = correct_option  # Index of correct answer (0-based)

    def check_answer(self, answer):
        return answer == self.correct_option

# -------- Quiz Class --------
class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def start(self):
        print("Welcome to the Online Quiz!\n")
        for idx, question in enumerate(self.questions, start=1):
            print(f"Q{idx}: {question.question}")
            for i, option in enumerate(question.options, start=1):
                print(f"{i}. {option}")

            # Get user input with validation
            while True:
                try:
                    answer = int(input("Enter your option (1-4): "))
                    if answer < 1 or answer > len(question.options):
                        raise ValueError
                    break
                except ValueError:
                    print("Invalid input! Please enter a number between 1 and 4.")

            # Check answer
            if question.check_answer(answer - 1):
                print("✅ Correct!\n")
                self.score += 1
            else:
                print(f"❌ Wrong! The correct answer was: {question.options[question.correct_option]}\n")

        # Display final score
        print(f"🎉 Quiz Completed! Your Score: {self.score}/{len(self.questions)}")

# -------- Quiz Data --------
questions_data = [
    {
        "question": "What is the capital of France?",
        "options": ["Berlin", "Paris", "Rome", "Madrid"],
        "answer": 1
    },
    {
        "question": "Which language is used for web apps?",
        "options": ["Python", "JavaScript", "C++", "Java"],
        "answer": 1
    },
    {
        "question": "Which data type is immutable?",
        "options": ["List", "Set", "Tuple", "Dictionary"],
        "answer": 2
    },
    {
        "question": "Which company developed Python?",
        "options": ["Microsoft", "Apple", "Google", "Python Software Foundation"],
        "answer": 3
    },
    {
        "question": "What does HTML stand for?",
        "options": ["Hyper Text Markup Language", "High Tech Machine Language", "Hyperlinks Text Markup Language", "Home Tool Markup Language"],
        "answer": 0
    }
]

# Convert dictionary data to Question objects
questions = [Question(q['question'], q['options'], q['answer']) for q in questions_data]

# -------- Start Quiz --------
if __name__ == "__main__":
    quiz = Quiz(questions)
    quiz.start()
