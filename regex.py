from thefuzz import fuzz
from thefuzz import process

choices = ["Atlanta Falcons", "New York Jets", "New York Giants", "Dallas Cowboys"]

userInput = input('Enter the item you are looking for: ')
regexLimit = int(input('Enter the fuzzy ratio: '))
print(process.extract(userInput, choices, limit=regexLimit))

# process.extractOne("cowboys", choices)
