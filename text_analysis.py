# List of questions
questions = [
    "If you see someone falling, would you help?",
    "Do you forgive people easily?",
    "Do you feel other people emotions?",
    "Do you accept being wrong?",
    "Do you apologize?"
]

# Initialize a variable to store the total score
total_score = 0

for question in questions:
    # user's response
    response = input(question + " (yes/no): ")
    
    # Check and calculate the score
    if response.lower() == "yes":
        score = 1
    elif response.lower() == "no":
        score = 0
    else:
        print("Invalid response. Please enter 'yes' or 'no'.")
        continue
    
    # Add the score to the total
    total_score += score

# Calculate the average score
average_score = total_score / len(questions)

# Analyze the average score to determine the user's level of empathy and interpersonal skills
if average_score > 0.8:
    print("You have high levels of empathy and interpersonal skills.")
elif average_score > 0.5:
    print("You have moderate levels of empathy and interpersonal skills.")
else:
    print("You have low levels of empathy and interpersonal skills.")