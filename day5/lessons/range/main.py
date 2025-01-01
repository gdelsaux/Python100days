# The range function does't do any thing on it's own it need to be use with another funct ex: forLoop

range(1, 5) # The range ins't inclusive of the last number so the expected range is : 1, 2, 3, 4

# Exercise: Complete the Gauss Chalenge
# calculate the sum of each iteration from 1 to 100: 1 + 2 + 3 + 4 + ... + 100
# the result should be: 5050
gauss = 0
for number in range(1, 101):
    gauss += number
print(gauss)

# NOTE:
# a 3rd param can be passed for incrementation, every n number
for number in range(1, 11, 3): # every 3rd number
    print(number) # expect 1, 4, 7, 10