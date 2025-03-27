"""Odd or Even Streetlight System A city uses an even-odd rule to manage electricity usage in streetlights. 
Streetlights with even numbers are turned on at night, while odd-numbered lights remain off.
 Write a program that takes a streetlight number as input and prints whether it should be ON or OFF."""

street_light_no = int(input("Enter Street light No.: "))
if street_light_no > 0 :
 if street_light_no % 2 == 0 :
  print("On")
 elif street_light_no % 2 != 0 :
  print("Off")
else:
  print("Enter Valid Street Light No.!!")