"""Counting Passengers in a Bus. A city bus stops at different stations, and passengers board at each stop.
 The bus conductor notes down the number of passengers at each stop for 5 stops. 
 Write a Python program to take input for each stop and calculate the total number of passengers at the end."""

passengers = 0
for i in range(5):
  added = int(input(f"Enter No. of Passengers board at stop {i+1} :"))
  passengers = passengers + added
print("Total No. of passengers at the end :",passengers)