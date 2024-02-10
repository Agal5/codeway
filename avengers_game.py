print("WELCOME TO AVENGERS QUIZ GAME")
print("NOTE: If the spelling is incorrect, the answer will be wrong")

questions = [
    "Who uses a hammer?", 
    "Who is the first Avenger?", 
    "What is Iron Man's name in Avengers?",
    "Who is Thor's brother?",
    "Who uses webs to catch?",
    "Who is the green beast?",
    "Who kills Vision?",
    "Who is Black Widow?",
    "Who changes size?"
]

answers = ["thor", "captain america", "tony stark", "loki", "spiderman", "hulk", "thanos", "natasha", "antman"]

points = 0

for i, question in enumerate(questions, 1):
    user_answer = input(f"{i}. {question} ").lower()
    if user_answer == answers[i-1]:
        print("Correct answer 👏🏻\nYou got 1 point")
        points += 1
    else:
        print("Incorrect answer ")
        print(f"Correct answer is '{answers[i-1].title()}'")

print(f"\nNumber of questions: {len(questions)}")
print(f"Your points: {points}")

feedback = input("Give your feedback about this quiz: ")
print(feedback)

play_again = input("Do you want to play this quiz again? ").lower()
if play_again == "yes":
    print("Restarting quiz...\n")
    exec(open(__file__).read())
else:
    print("Goodbye!")


