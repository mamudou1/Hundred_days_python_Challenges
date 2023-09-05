#You are going to write a program that calculates 
# the average student height from a List of heights.
# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
sum_hi = 0
len_h = 0
for total in student_heights:
    sum_hi += total
    len_h += 1
x = sum_hi/len_h
y= round(x)
print(y)
