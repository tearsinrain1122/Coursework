import requests  # To send http requests to the API
import random  # To randomise the question selection for each user
from time import sleep  # Function imported from additional module to make the console output more readable

print("""
                    ***Hello, and welcome to Ellen's Film Trivia Quiz!***
                    """)

# Sending http request and storing the data from API in a variable named data
endpoint = "https://opentdb.com/api.php?amount=10&category=11&difficulty=easy&type=multiple"
response = requests.get(endpoint)
data = response.json()

sleep(1)

print("Get ready, here's the first question...\n")

sleep(1)


# Function to print a random trivia question from the API and corresponding multiple choice
# answers to the console, ask user for input to select their answer, then tell them if
# they are correct or not.
def generate_question(random_question_number):
    question = data["results"][random_question_number]["question"]
    corrected_question = check_for_special_characters(question)
    print(corrected_question)
    q_wrong_answers = data["results"][random_question_number]["incorrect_answers"]
    q_correct_answer = data["results"][random_question_number]["correct_answer"]
    multi_choice_answers = generate_multi_choice(q_wrong_answers, q_correct_answer)
    player_answer = input("Type the number for the correct answer here: ")
    if player_answer.isnumeric() and int(player_answer) < 5:
        if multi_choice_answers[int(player_answer)-1] == q_correct_answer:
            print("\nCongratulations, that's correct!")
            write_to_file(f"""
Question: {corrected_question}
Correct Answer: {q_correct_answer}
Congratulations, you got this right!""")
            return True
        else:
            print("\nSorry, that's not quite right.")
            write_to_file(f"""
Question: {corrected_question}
Correct Answer: {q_correct_answer}
Apologies, you got this wrong.""")
            return False
    else:
        print("\nSorry, that's not quite right.")
        write_to_file(f"""
Question: {corrected_question}
Correct Answer: {q_correct_answer}
Apologies, you got this wrong.""")
        return False


# Function to randomly insert the correct answer into a pre-existing list of three incorrect answers.
# Ensures the right answer is not in the same position each time.
def generate_multi_choice(wrong_answers, correct_answer):
    multi_choice_answers = wrong_answers
    multi_choice_answers.insert(random.randint(0, 3), correct_answer)
    for i in multi_choice_answers:
        print(f"{multi_choice_answers.index(i)+1}: {check_for_special_characters(i)}\n")
    return multi_choice_answers


# I noticed that some questions/answers on the API had special characters that made them less readable,
# so I made a function to replace these instances with readable alternatives.
def check_for_special_characters(question_or_answer):
    bad_characters = ["&quot;", "&#039;", "&rsquo;"]
    question_or_answer = question_or_answer.replace("&ntilde;", "n")
    question_or_answer = question_or_answer.replace("&aacute;", "a")
    question_or_answer = question_or_answer.replace("&amp;", "&")
    for i in bad_characters:
        question_or_answer = question_or_answer.replace(i, "`")
    return question_or_answer


# I wanted to make a Certificate of Participation that recorded the score and correct answers, so rather
# than write everything to a file at the end, I decided to make a function that would write any input to
# a file, so that I could do this more easily as the program ran. The correct file pathway should be input between
# the ""
def write_to_file(to_file):
    file = open("", "a+")
    to_file = check_for_special_characters(to_file)
    file.write(to_file + "\n")
    file.close()


# Initialising player score at 0, and overwriting any existing certificate file with a new version. The correct file pathway should 
# be input between the ""
player_score_counter = 0
file_start = open("", "w")
file_start.write("Ellen's Film Trivia Quiz - Certificate of Participation\n")
file_start.close()

# Three random numbers from a range of 10 to select three random questions from the API of 10 (0-9 indexes),
# without replacement to avoid repetition.
question_numbers = random.sample(range(10), 3)

# The generate_question function is run for each question from the three randomly selected, with the value
# of the function stored as a variable. The player's score is increased by 1 if the value of the function is True
# (i.e., if their answer is correct).
question_one = generate_question(question_numbers[0])
if question_one:
    player_score_counter += 1

sleep(1)

print("\nLet's move on to Question 2!")

sleep(1)

question_two = generate_question(question_numbers[1])
if question_two:
    player_score_counter += 1

sleep(1)

print("\nOkay, final question. Concentrate now...")

sleep(1)

question_three = generate_question(question_numbers[2])
if question_three:
    player_score_counter += 1

sleep(1)

# Closing statement/results, also added to Certificate file.
final_message = (f"""\nThanks for playing! You got {player_score_counter} out of 3 questions correct.
Congrats, you're a pro!""")
if player_score_counter >= 2:
    print(final_message)
    write_to_file(final_message)
else:
    print(final_message[:58])
    write_to_file(final_message[:58])
