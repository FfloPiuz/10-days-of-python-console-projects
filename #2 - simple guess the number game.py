import random as r

answer = r.randint(1, 100)
attempts = 0

print("Guess the number from 1 to 100!")

while True:
    try:
        question = int(input("Enter the num: "))
        attempts += 1

        if question < 1 or question > 100:
            print("The number must be between 1 and 100!")
            continue

        if question == answer:
            print(f"Correct! You took {attempts} attempts!")
            break
        elif question < answer:
            print("⬆Too low! Try again.")
        else:
            print("⬇Too high! Try again.")

    except ValueError:
        print("❌ Please enter a valid number!")