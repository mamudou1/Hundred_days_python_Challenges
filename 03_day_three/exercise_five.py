"""You are going to write a program that tests thecompatibility
between two people.To work out the love score between two people:
Take both people's names and check for the numberof times the
letters in the word TRUE occurs. Then check for the number of
times the letters in the word LOVE occurs. Then combine these 
numbers to make a 2 digit number."""

# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
x = name1 + name2
total= x.lower()
true_count= total.count("t") + total.count("r")+ total.count("u")+ total.count("e")
love_count =total.count("l") + total.count("o")+ total.count("v")+ total.count("e")

sum_total= int(str(true_count) + str(love_count))
 

if sum_total < 10 or sum_total > 90:
    print(f"Your score is {sum_total}, you go together like coke and mentos.")
elif sum_total >= 40 and sum_total <= 50:
    print(f"Your score is {sum_total}, you are alright together.")
else:
    print(f"Your score is {sum_total}.")