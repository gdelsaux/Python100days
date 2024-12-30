import random
import my_module

# creates a random num between 1 and 10(inclusive)
random_int = random.randint(1, 10)
print(random_int)

# creates a random float between 0 and 1(not inclusive)
random_num_0_to_1 = random.random()
print(random_num_0_to_1)

# creates a random float betwwen 1 an 10(inclusive)
random_float = random.uniform(1, 10)
print(random_float)
