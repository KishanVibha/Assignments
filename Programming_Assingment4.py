#!/usr/bin/env python
# coding: utf-8

# # 1.	Write a Python Program to Find the Factorial of a Number?

# In[3]:


def factorial(n):
    if n<0:
        return "Factorial does not exist for negative numbers."
    elif n==0 or n==1:
        return 1
    else:
        result = 1
        for i in range(2,n+1):
            result*=i
        return result
    
number = int(input("Enter a number to find its factorial: "))
print(f"The factorial of {number} is {factorial(number)}.")


# # 2.	Write a Python Program to Display the multiplication Table?

# In[18]:


num = int(input("Enter a number to display its multiplication table: "))
for i in range(1,11):
     print(f"{num}*{i} = {num*i}")
    


# In[6]:


# Function to display multiplication table
def display_table(number, up_to=10):
    print(f"Multiplication Table for {number}:")
    for i in range(1, up_to + 1):
        print(f"{number} x {i} = {number * i}")

# Input from the user
number = int(input("Enter a number to display its multiplication table: "))
up_to = int(input("Enter the range for the table (default is 10): "))

# Output the result
display_table(number, up_to)


# # 3.	Write a Python Program to Print the Fibonacci sequence?

# In[20]:


# Input from the user
num_terms = int(input("Enter the number of terms: "))

# Initialize first two terms
a, b = 0, 1

print("Fibonacci Sequence:")
for _ in range(num_terms):
    print(a, end=" ")
    a, b = b, a + b


# # 4.	Write a Python Program to Check Armstrong Number?

# In[25]:


# Input from the user
number = int(input("Enter a number: "))

# Calculate the Armstrong sum
armstrong_sum = sum(int(digit) ** len(str(number)) for digit in str(number))

# Check and display the result
if number == armstrong_sum:
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")


# # 5.	Write a Python Program to Find Armstrong Number in an Interval?

# In[28]:


# Input for the interval
start = int(input("Enter the start of the interval: "))
end = int(input("Enter the end of the interval: "))

# Find and display Armstrong numbers
print(f"Armstrong numbers between {start} and {end}:")
for num in range(start, end + 1):
    if num == sum(int(digit) ** len(str(num)) for digit in str(num)):
        print(num, end=" ")


# # 6.	Write a Python Program to Find the Sum of Natural Numbers?

# In[29]:


# Input from the user
n = int(input("Enter a positive integer: "))

# Calculate the sum of natural numbers
if n < 1:
    print("Please enter a positive integer.")
else:
    sum_natural = n * (n + 1) // 2
    print(f"The sum of the first {n} natural numbers is {sum_natural}.")

