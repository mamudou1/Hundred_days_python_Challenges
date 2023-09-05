
#Write a program that adds the digits in 
# a 2 digit number. e.g. if the input 
# was 35, then the output should be 3 + 5 = 8
# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇
a= int(two_digit_number)
b=a//10
#or
x=two_digit_number[0]

c=a%10
#or
y=two_digit_number[1]
e=int(x)
d=int(y)

print(b+c)
print((e+d))