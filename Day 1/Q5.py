"""ATM PIN Verification A bank ATM allows a user to enter their PIN a maximum of 3 times.
 If the correct PIN (1234) is entered within 3 attempts, 
 the user gains access; otherwise, the card is blocked. Write a Python program for this."""

PIN = 1234
for i in range(3):
  pin = int(input("Enter Your PIN:"))
  if pin == PIN:
    print("Access Granted.")
    break
  else:
    print("Access denied.")
    print("You have",3-i-1, "attempt(s) left.")
    print("\n")
else:
  print("ATM PIN Limit is exceeded. You have Entered Wrong PIN 3 Times. Your Card Gets BLOCKED. Please Contact Home Branch!!")