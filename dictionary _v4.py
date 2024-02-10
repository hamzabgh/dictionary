import random

questions_answers_1 = {
    'What is the capital of France?': 'Paris',
    'In which year did World War II end?': '1945',
    'Who wrote "Romeo and Juliet"?': 'William Shakespeare',
}

questions_answers_2 = {
    'What is the largest planet in our solar system?': 'Jupiter',
    'Who painted the Mona Lisa?': 'Leonardo da Vinci',
    'What is the square root of 144?': '12',
}

questions_answers_3 = {
    'Which programming language is known for its readability and ease of use?': 'Python',
    'What is the chemical symbol for gold?': 'Au',
    'Who is the CEO of Tesla?': 'Elon Musk',
}

all_questions_answers = [questions_answers_1, questions_answers_2, questions_answers_3]

user_score = 0
count = 0

while count < len(all_questions_answers):
    random_dict = random.choice(all_questions_answers)
    random_question = random.choice(list(random_dict.keys()))
    correct_answer = random_dict[random_question]

    user_input = input(f"{random_question}: ")

    if str(user_input) == str(correct_answer):
        print("Correct!")
        user_score += 1
    else:
        print("Incorrect!")
        user_score -= 1
    count += 1

if user_score >= 0:
    print(f"You scored {user_score} points!")
else:
    print(f"You scored {user_score} points. Keep trying, you can improve!") 
