import json

def load_questions(filename):
    with open(filename, "r") as file:
        return json.load(file)

def run_quiz(questions):
    score = 0
    for i, q in enumerate(questions, 1):
        print(f"\nQ{i}: {q['question']}")
        for idx, opt in enumerate(q['options']):
            print(f"{idx + 1}. {opt}")
        try:
            answer = int(input("Your answer (1-4): ")) - 1
            if answer == q['answer']:
                print("✅ Correct!")
                score += 1
            else:
                correct = q['options'][q['answer']]
                print(f"❌ Wrong! Correct answer: {correct}")
        except:
            print("⚠️ Invalid input. Skipping question.")
    print(f"\n🏆 Final Score: {score}/{len(questions)}")

if __name__ == "__main__":
    questions = load_questions("indian_cricket_questions.json")
    run_quiz(questions)