"""reate a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.

It will take your current age as the input and output a message with our time left in this format:

You have x days, y weeks, and z months left.

Where x, y and z are replaced with the actual calculated numbers."""

# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
b=int(age)
age_left= 90-b
num_days = age_left*365
num_weeks = age_left *52
num_months = age_left* 12
print("You have " + str(num_days) + " days, " + str(num_weeks) +" weeks, and "+ str(num_months) + " months left.")

