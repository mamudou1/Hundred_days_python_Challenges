#Write a program that calculates the Body Mass
# Index (BMI) from a user's weight and height.
# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
a=float(height)
b=float(weight)
body_mass_index= b/(a**2)
result= int(body_mass_index)
print(result)