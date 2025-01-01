import random

random_num = random.randint(1 , 2)

head_or_tail = input("head or tail? ")

if head_or_tail == "tail" and random_num % 2 == 0:
  print("you win!")
elif head_or_tail == "head" and not random_num % 2 == 0:
  print("you win!")
else:
  print("I won!")