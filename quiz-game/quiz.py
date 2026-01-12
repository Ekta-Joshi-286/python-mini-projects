# Quiz Game

# Step 1: Store questions, options, and answers
questions = [
    {
        "question": "What is the capital of India?",
        "options": ["A. Mumbai", "B. Delhi", "C. Kolkata", "D. Chennai"],
        "answer": "B"
    },
    {
        "question": "Which language is used to write Python programs?",
        "options": ["A. C", "B. Java", "C. Python", "D. HTML"],
        "answer": "C"
    },
    {
        "question": "What is 5 + 3?",
        "options": ["A. 6", "B. 7", "C. 8", "D. 9"],
        "answer": "C"
    }
]

score = 0  # Start with zero score

# Step 2: Function to ask questions
def play_quiz():
    global score
    for q in questions:
        print("\n" + q["question"])
        for option in q["options"]:
            print(option)
        answer = input("Enter your answer (A/B/C/D): ").upper()

        if answer == q["answer"]:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong! Correct answer is {q['answer']}")

# Step 3: Run the quiz
print("🎯 Welcome to the Quiz Game!")
play_quiz()

# Step 4: Show final score
print("\n------ QUIZ RESULT ------")
print(f"Your Score: {score}/{len(questions)}")

if score == len(questions):
    print("🏆 Excellent! You got all correct!")
elif score >= 2:
    print("👍 Good job! You did well.")
else:
    print("😅 Keep practicing! Better luck next time.")
