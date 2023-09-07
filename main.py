"""
Develop a quiz game that asks users multiple-choice or fill-in-the-blank questions on a specific topic. The game
should keep track of scores, provide feedback on correct/incorrect answers, and offer a variety of questions to make
it challenging and engaging.
Load Quiz Questions.
Calculate the Final Score.
Display Final Results:
Display Welcome Message and Rules.
Present Quiz Questions:
Display each question and answer choice.
Prompt the user to select an answer.
Evaluate the User's Answer:
Compare the user's answer with the correct answer.
Keep track of the user's score.
Provide Feedback:
Display if the answer was correct or incorrect.
Show the correct answer for incorrect responses.
Play Again:
Ask the user if they want to play again
"""
import random

class QuizQuestion:
    def __init__(self, question, choices, correct_answer):
        self.question = question
        self.choices = choices
        self.correct_answer = correct_answer

    def is_correct(self, user_answer):
        return user_answer.lower() == self.correct_answer.lower()


class QuizGame:
    def __init__(self):
        self.questions = []
        self.score = 0

    def load_questions(self):
        # Add your questions here
        question1 = QuizQuestion("What is the capital of France?", ["London", "Berlin", "Paris"], "Paris")
        question2 = QuizQuestion("Which planet is known as the Red Planet?", ["Earth", "Mars", "Jupiter"], "Mars")
        questions = [
            QuizQuestion("What is the capital of France?", ["London", "Berlin", "Paris"], "Paris"),
            QuizQuestion("What is the largest mammal in the world?", ["Elephant", "Giraffe", "Blue Whale"],
                         "Blue Whale"),
            QuizQuestion("Which gas do plants absorb from the atmosphere?", ["Oxygen", "Carbon Dioxide", "Nitrogen"],
                         "Carbon Dioxide"),
            QuizQuestion("Who wrote the play 'Romeo and Juliet'?",
                         ["Charles Dickens", "William Shakespeare", "Jane Austen"], "William Shakespeare"),
            QuizQuestion("What is the chemical symbol for gold?", ["Au", "Ag", "Fe"], "Au"),
            QuizQuestion("What is the tallest mountain in the world?",
                         ["Mount Kilimanjaro", "Mount Everest", "Mount Fuji"], "Mount Everest"),
            QuizQuestion("What is the largest organ in the human body?", ["Heart", "Brain", "Skin"], "Skin"),
            QuizQuestion("What is the primary function of the kidneys?", ["Digestion", "Respiration", "Filtration"],
                         "Filtration"),
            QuizQuestion("Which gas makes up the majority of Earth's atmosphere?",
                         ["Oxygen", "Carbon Dioxide", "Nitrogen"], "Nitrogen"),
            QuizQuestion("What is the chemical symbol for water?", ["H2O", "CO2", "O2"], "H2O"),
            QuizQuestion("Who painted the Mona Lisa?", ["Pablo Picasso", "Vincent van Gogh", "Leonardo da Vinci"],
                         "Leonardo da Vinci"),
            QuizQuestion("What is the smallest prime number?", ["0", "1", "2"], "2"),
            QuizQuestion("Which planet is known as the 'Morning Star'?", ["Venus", "Mars", "Mercury"], "Venus"),
            QuizQuestion("What is the powerhouse of the cell?", ["Mitochondria", "Nucleus", "Ribosome"],
                         "Mitochondria"),
            QuizQuestion("Who is the author of 'To Kill a Mockingbird'?",
                         ["J.K. Rowling", "Harper Lee", "George Orwell"], "Harper Lee"),
            QuizQuestion("What is the freezing point of water in Fahrenheit?", ["0°F", "32°F", "100°F"], "32°F"),
            QuizQuestion("Which gas do plants release during photosynthesis?", ["Carbon Dioxide", "Oxygen", "Nitrogen"],
                         "Oxygen"),
            QuizQuestion("What is the largest planet in our solar system?", ["Mars", "Venus", "Jupiter"], "Jupiter"),
            QuizQuestion("Who is credited with the discovery of electricity?",
                         ["Isaac Newton", "Thomas Edison", "Benjamin Franklin"], "Benjamin Franklin")
        ]

        # Add more questions here

        self.questions.extend([question1, question2])

    def display_welcome_message(self):
        print("Welcome to the Quiz Game!")
        print("Rules:")
        print("1. Answer the questions to the best of your ability.")
        print("2. You will receive feedback after each question.")
        print("3. Your final score will be displayed at the end.")

    def present_question(self, question):
        print(question.question)
        for choice in question.choices:
            print(choice)
        user_answer = input("Your answer: ")
        return user_answer

    def play(self):
        self.load_questions()
        self.display_welcome_message()

        play_again = "yes"
        while play_again.lower() == "yes":
            random.shuffle(self.questions)
            self.score = 0

            for question in self.questions:
                user_answer = self.present_question(question)
                if question.is_correct(user_answer):
                    print("Correct!\n")
                    self.score += 1
                else:
                    print(f"Incorrect. The correct answer is: {question.correct_answer}\n")

            final_score = (self.score / len(self.questions)) * 100
            print(f"Quiz completed! Your final score is: {final_score:.2f}%")
            play_again = input("Do you want to play again? (yes/no): ")


if __name__ == "__main__":
    quiz_game = QuizGame()
    quiz_game.play()
