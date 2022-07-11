"""
Student Number: 101370671
Sample Coding Questions 01 Week 01
First Name: Binye
Last Name: Liu
"""
# Q2 Defining Variables
num_arr = [1, 4, 7, 9]
# Q3 Order of Operations
a = 1
b = 2
c = 3
d = 4
# Fully-Bracketed Version of: e = a - b ** c // d + a % c
#e = 1 - 2 ** 3 // 4 + 1%3
e = a - (b ** c // d) + (a % c)
print(e)
# Q4 Formatting
temperature = 32.6
print("The temperature today is: {:.3f} degrees Celsius.".format(32.600))
# Q5 Common Functions
userAge = input("Input your age:")
print("Now showing the shop items filtered by age: {}".format(userAge))
