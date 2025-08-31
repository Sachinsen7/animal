from Question import Question

question_prompts = [
    "What color are apples?\n(a) Red/Greenn\n(b) Purple \n(c) Orange\n\n",
    "What color are Bananas?\n(a) Red\n(b) Purple \n(c) Yellow\n\n",
    "What color are strawberries?\n(a) Magenta\n(b) Blue \n(c) Red\n\n"
              ]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "c")
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("you got " + str(score) + "/" + str(len(questions)) + "correct " )

run_test(questions)
