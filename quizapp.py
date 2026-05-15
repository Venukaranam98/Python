import json

questions = [

    {
        "question":
        "What is the capital of Andhra Pradesh?",

        "options":
        ["A. Amaravathi", "B. Chennai",
         "C. Hyderabad", "D. Mumbai"],

        "answer":
        "a"
    },

    {
        "question":
        "Which keyword is used to create a function in Python?",

        "options":
        ["A. func", "B. define",
         "C. def", "D. function"],

        "answer":
        "c"
    },

    {
        "question":
        "Which loop repeats until condition becomes false?",

        "options":
        ["A. for", "B. while",
         "C. switch", "D. do"],

        "answer":
        "b"
    }

]


score = 0


def start_quiz():

    global score

    for q in questions:

        print("\n" + q["question"])

        for option in q["options"]:

            print(option)

        user_answer = input(
            "Enter option (a/b/c/d): "
        ).lower()

        if user_answer == q["answer"]:

            print("Correct")

            score += 1

        else:

            print("Wrong")

            print(
                "Correct answer:",
                q["answer"].upper()
            )


def show_result():

    percentage = (
        score / len(questions)
    ) * 100

    print("\n--- QUIZ RESULT ---")

    print("Score:", score)

    print(
        "Total Questions:",
        len(questions)
    )

    print(
        "Percentage:",
        percentage
    )

    if percentage >= 90:

        print("Grade: Excellent")

    elif percentage >= 70:

        print("Grade: Good")

    else:

        print("Grade: Needs Improvement")


def save_score():

    result = {
        "score": score,
        "total": len(questions)
    }

    with open("quiz_result.json", "w") as file:

        json.dump(result, file)

    print("Result saved")


start_quiz()

show_result()

save_score()