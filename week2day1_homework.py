# Exercise 1
# Cube Number Test... 
# Print out all cubed numbers up to the total value 1000, 
# so if the cubed number is over 1000 break the loop.

for i in range(0,2000):
    if i**3 >= 1000:
        break
    print(i**3)

# Exercise 2
# Get first prime numbers up to 100

for num in range(1, 100):
    if num > 1:
        for var in range(2, num):
            if (num % var) == 0:
                 break
        else:
            print(num)

# Exercise 3
# Take in a users input for their age, if they are younger than 18 print kids, 
# if they're 18 to 65 print adults, else print seniors

age = input("What is your age? ")
if int(age) < 18:
    print("kids")
else:
    print("seniors")