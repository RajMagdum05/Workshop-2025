"""Reverse a Number Write a Python program to reverse a given number. 
For example, if the input is 12345, the output should be 54321."""

num = int(input("Enter the Number: "))
reversed_num = 0
while num != 0 :
  digit = num % 10
  reversed_num = reversed_num * 10 + digit
  num //= 10
print("Reversed Number: ",reversed_num)