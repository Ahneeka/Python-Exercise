import random

random.seed(4)
number = random.randint(1, 10)

i = 0
while i < 3:
    guess = int(input("Guess a number between 1 and 10"))

if guess == number:
    print("You guessed right")
elif guess < number:
    print("Too high")
else:
    print("Too low")

# if guess == number:
#     print ("You guessed right")
# else:
#     print("Better luck next time, you tried guessing ordinary", random)
