# Quiz App

def display_question(question, options, correct_option):
    print("\n" + question)
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    
    try:
        answer = int(input("Enter your choice (1-4): "))
        if answer == correct_option:
            print("Correct!")
            return True
        else:
            print("Wrong! The correct answer was:", options[correct_option - 1])
            return False
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 4.")
        return False

def main():
    # List of questions, options, and the correct answer (1-indexed)
    quiz_data = [
        {
            "question": "What is the capital of India?",
            "options": ["Mumbai", "Delhi", "Kolkata", "Chennai"],
            "correct_option": 2
        },
        {
            "question": "Which programming language is known as the 'language of the web'?",
            "options": ["Java", "C++", "Python", "JavaScript"],
            "correct_option": 4
        },
        {
            "question": "Who wrote the famous novel '1984'?",
            "options": ["George Orwell", "J.K. Rowling", "Mark Twain", "Ernest Hemingway"],
            "correct_option": 1
        },
        {
            "question": "What is the largest planet in our solar system?",
            "options": ["Earth", "Mars", "Jupiter", "Saturn"],
            "correct_option": 3
        }
    ]

    print("Welcome to the Quiz App!")
    score = 0

    for q in quiz_data:
        if display_question(q["question"], q["options"], q["correct_option"]):
            score += 1

    print("\nQuiz Complete!")
    print(f"Your total score is: {score}/{len(quiz_data)}")

if __name__ == "__main__":
    main()
