# List of questions. Each question contains:
# [question text, option 1, option 2, option 3, option 4, correct option number (1-4)]
questions = [
    ["What is the capital of France?", "Berlin", "Madrid", "Paris", "London", 3],
    ["Which number is even?", "3", "7", "10", "9", 3],
    ["Which animal barks?", "Cat", "Dog", "Cow", "Horse", 2],
    ["What color is the sky on a clear day?", "Green", "Blue", "Red", "Yellow", 2],
    ["Which fruit is yellow?", "Apple", "Banana", "Cherry", "Grapes", 2],
    ["Which planet is known as the Red Planet?", "Earth", "Mars", "Venus", "Jupiter", 2],
    ["How many legs does a spider have?", "6", "8", "4", "2", 2],
    ["What is 2 + 2?", "3", "4", "5", "6", 2],
    ["What do bees produce?", "Milk", "Honey", "Water", "Juice", 2],
    ["Which is a primary color?", "Green", "Purple", "Blue", "Pink", 3]
]

# List of prize money for each correct answer
prizes = [
    "1 Million",
    "2 Million",
    "3 Million",
    "4 Million",
    "5 Million",
    "6 Million",
    "7 Million",
    "8 Million",
    "9 Million",
    "10 Million"
]

reward = 0  # To keep track of how many correct answers the player gives

# Loop through each question
for i, question in enumerate(questions):
    print(f"\nQuestion {i + 1}: {question[0]}")  # Print the question
    print(f"1. {question[1]}")
    print(f"2. {question[2]}")
    print(f"3. {question[3]}")
    print(f"4. {question[4]}")
    print("Enter your answer (1-4):")

    try:
        option = int(input(">>"))  # Take input from user

        if (option < 1 or option > 4):
            print("Invalid option. Please choose between 1 and 4.")  # Input range validation
            break

        if question[5] == option:  # Check if the answer is correct
            print("Correct Answer!")
            print(f"You won {prizes[reward]}")  # Show the prize won so far
            reward += 1  # Move to next level/reward
        else:
            print("Better luck next time")  # If wrong answer

            # Calculate what the player has won so far
            if reward > 0:
                final_reward = prizes[reward - 1]
            else:
                final_reward = "Nothing"

            print(f"You won only: {final_reward}")
            break  # End the quiz if wrong answer is given

    except Exception as e:
        print("Invalid input! Please enter a number.")  # Handle non-integer input
        break

# If all questions are answered correctly
if reward == len(questions):
    print("\n🎉 Congratulations! You answered all questions and won the grand prize!")
