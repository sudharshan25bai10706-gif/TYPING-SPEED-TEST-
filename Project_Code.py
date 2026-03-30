
import time
import random

print("Typing Speed Test")
print("------------------")

# some sentences
lines = [
    "python is easy to learn",
    "practice makes a person perfect",
    "coding is fun when you understand it",
    "i am learning python",
    "speed comes with practice"
]

# pick one line randomly
line = random.choice(lines)

print("\nType this line:")
print(line)

input("\nPress Enter when you are ready...")

# start time
start = time.time()

# user types
user_text = input("\nStart typing:\n")

# end time
end = time.time()

# total time
time_taken = end - start

# word count
words = len(user_text.split())

# speed calculation
wpm = (words / time_taken) * 60

# accuracy check
correct = 0
for i in range(len(line)):
    if i < len(user_text) and line[i] == user_text[i]:
        correct += 1

accuracy = (correct / len(line)) * 100

# result
print("\nResult")
print("Time taken:", round(time_taken, 2), "seconds")
print("Speed:", round(wpm, 2), "words per minute")
print("Accuracy:", round(accuracy, 2), "%")


 
