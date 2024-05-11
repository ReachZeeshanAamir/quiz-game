import json

filepath = './question.json'

def save_questions(questions):
    data = {"questions": questions}  # Store questions in a dictionary
    with open(filepath, 'w') as file:
        json.dump(data, file, indent=4)

def load_questions(filepath):
    try:
        with open(filepath, 'r') as file:
            data = json.load(file)
            return data.get("questions", [])  # Retrieve questions from the loaded data
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def run_quiz(questions):
    score = 0
    for question in questions:
        print(question["prompt"])
        for option in question["options"]:
            print(option)
        answer = input(" Enter your answer:\n (A, B, C or D)").upper()
        if answer == question["answer"]:
            print("Correct\n")
            score +=1
        else:
            correct_answer = question["answer"]
            print(f"Wrong! The answer is \"{correct_answer}\" ")
    print(f"You got {score} out of {len(questions)} questions correct")        
    choice = input("Do you want to add questions? (Y for yes, N for no)").upper()
    if choice == 'Y':
        add_question(questions)
    else: 
        save_questions(questions)
        exit()

def add_question(questions):
    prompt = input("Write Question here: ")
    opt_a = input("Enter option A: ")
    opt_b = input("Enter option B: ")
    opt_c = input("Enter option C: ")
    opt_d = input("Enter option D: ")
    Lanswer = input("Enter Correct option: ")
    questions.append(
        {"prompt": prompt,
         "options": [opt_a, opt_b, opt_c, opt_d],
         "answer": Lanswer.upper() })
    save_questions(questions)
    want = input("Do you still want to run the quiz. (Y/N)").lower()
    if want == "y":
        run_quiz(questions)
    else:
        exit()

# Load existing questions or create an empty list if the file doesn't exist
questions = load_questions(filepath)
# Start the quiz with loaded questions
run_quiz(questions)
