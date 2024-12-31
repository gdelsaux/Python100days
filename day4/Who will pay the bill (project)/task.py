import random

def printString(name):
  print(f"Option1: Looks like {name} will be paying the bill today")


# first option without native python list randomness
people = ["John", "Bruce", "Mike", "Peter", "Barbara", "Mary"]
number_of_person = len(people) - 1
random_person_index = random.randint(0, number_of_person)
printString(people[random_person_index])

# second option with native python method
printString(random.choice(people))