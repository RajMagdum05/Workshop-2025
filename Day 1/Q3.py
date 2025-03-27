"""Imagine you are designing a basic ATM-like interface where users can:
1)Check Balance
2)Deposit Money
3)Withdraw Money
4)Exit the System. 
Your Task: Write a Python program that displays a menu, 
takes user input, and performs the respective operation based on the user's choice."""

print("Welcome !!")
print("Menu -> \n 1)Check Balance.\n 2)Deposit Money\n 3)Withdraw Money\n 4)Exit the system.\n")
choice = int(input("Enter Your Choice: "))
if choice == 1:
  print("Check Balance")
  print("Your Bank Balance is XXXXXX.")
elif choice == 2:
  print("Deposit Money.")
  print("Deposit Your Money Here: ")
elif choice == 3:
  print("Withdraw Money.")
  print("Enter Amount to withdraw Money: ")
elif choice == 4:
  print("Exited from the System.")
  print("Returned to main menu.")
else:
  print("Enter Valid Choice Number.")