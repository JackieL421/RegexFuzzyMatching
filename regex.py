from thefuzz import fuzz
from thefuzz import process

choices = ["Atlanta Falcons", "New York Jets", "New York Giants", "Dallas Cowboys"]

print(fuzz.ratio("this is a test", "this is a test!"))

print(process.extract("new york jets", choices, limit=2))

# process.extractOne("cowboys", choices)
