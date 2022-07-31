import json
import time

jsonData = '{"game":{"id":406,"dayOffset":406,"boardState":["","","","","",""],"currentRowIndex":0,"status":"IN_PROGRESS","timestamps":{"lastPlayed":null,"lastCompleted":null}},"settings":{"hardMode":false,"darkMode":true,"colorblindMode":false},"stats":{"currentStreak":0,"maxStreak":0,"guesses":{"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"fail":0},"winPercentage":0,"gamesPlayed":0,"gamesWon":0,"averageGuesses":0},"timestamp":0}'

data = json.loads(jsonData)
stats = data["stats"]

stats["gamesPlayed"] = int(input("Number of games played: "))
stats["currentStreak"] = int(input("Current winning streak: "))
stats["maxStreak"] = int(input("Highest winning streak: "))

rowGuesses = [0, 0, 0, 0, 0, 0]

for i in range(6):
    maxGuesses = stats['gamesPlayed'] - sum(rowGuesses)

    if maxGuesses <= 0:
        break

    rowGuesses[i] = int(input(
        f"({maxGuesses} max) Correct guesses in row {i+1}: "))

    if rowGuesses[i] <= maxGuesses:
        stats["guesses"][str(i+1)] = rowGuesses[i]
    else:
        rowGuesses[i] = maxGuesses
        stats["guesses"][str(i+1)] = maxGuesses

stats["gamesWon"] = sum(rowGuesses)
stats["guesses"]["fail"] = stats["gamesPlayed"] - stats["gamesWon"]

stats["winPercentage"] = round(stats["gamesWon"] / stats["gamesPlayed"] * 100)
stats["averageGuesses"] = round(
    sum((i+1)*rowGuesses[i] for i in range(6)) / stats["gamesWon"])

data["timestamp"] = round(time.time())

print()
for item in stats:
    print(f"{item}: {stats[item]}")
print("\n\nCopy this JSON data:\n")

jsonData = json.dumps(data)
print(jsonData, "\n")
