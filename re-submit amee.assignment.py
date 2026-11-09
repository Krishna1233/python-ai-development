"""Task 1: Perform Basic Mathematical Operations

Problem Statement: Write a Python program that does the following:"""

#1.  Takes two numbers as input from the user.
num1= input("enter first number:- ")
num2= input("enter second number:- ")
print("first number:- ",num1)
print("second number:- ",num2)

#2.  Performs the basic mathematical operations on these two numbers:

"""o        Addition

o        Subtraction

o        Multiplication

o        Division"""

#addition

A = int(num1)
B = int(num2)

print("Addition:- ", A+B)

#subtraction

a1= int(num1)
b1= int(num2)

print("substraction:-", a1-b1)

#multiplication

M= int(num1)
N = int(num2)

print("Multiplication:-", M*N)

#Division

D1= int(num1)
D2 = int(num2)

print("Division:- ", D1/D2)

"""Task 2: Create a Personalized Greeting

Problem Statement: Write a Python program that:

1.  Takes a user's first name and last name as input.

2.  Concatenates the first name and last name into a full name.

3.  Prints a personalized greeting message using the full name."""

user = input("enter your good name:- ")
user1= input("enter your last name:- ")

print("hello", user ,user1+"!", "welcome to the python program")
