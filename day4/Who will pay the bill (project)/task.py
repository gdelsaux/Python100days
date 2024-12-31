import random

people = ["John", "Bruce", "Mike", "Peter", "Barbara", "Mary"]
number_of_person = len(people) - 1
random_person_index = random.randint(0, number_of_person)

print(random_person_index)
print(f"Looks like {people[random_person_index]} will be paying the bill today")