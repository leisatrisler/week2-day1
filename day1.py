# Exercise #1
# Cube Number Test... Print out all cubed numbers up to the total value 1000. Meaning that if the cubed number is over 1000 break the loop.

list_num = []
for x in range(1, 1001):
    print(x*x*x)


# Exercise #2
# Get first prime numbers up to 100

# HINT::
# An else after an if runs if the if didn’t
# An else after a for runs if the for didn’t break

x1 = 1
y = 100
for x in range(x1, y):
    is_prime = True
    for i in range(2, x):
        if (x % i == 0):
            is_prime = False
    if is_prime == True:
        print(x)

# Exercise 3
# Take in a users input for their age, if they are younger than 18 print kids, if they're 18 to 65 print adults, else print seniors. Gracefully log the error if the user doesn't enter a number
# age = int(input(18: )) if age >= 18
# print(kids)
# else:
#     print(adults)
# ``
