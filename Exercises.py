#QUESTION ONE
# The volume of a sphere with radius r is (4/3)*pie*r**2
# What is the volume Of a sphere with radius 5.
# Make sure the program enters the radius from the Keyboard and provide the answer in 2 decimal places

radius = float(input('Enter the radius'))
pie = float(22/7)
volume = (4/3)*pie*(radius**2)
print(f"The volume of the sphere is: {volume:.2f}")


#QUESTION TWO
# Create a program to calculate the area of atriangle (1/2 * base *height).
# Base and height should be entered using the keyboard.
base = float(input("Enter the base of the triangle:"))
height = float(input("Enter the height of the triangle:"))
area = (1/2)*base*height



#QUESTION THREE
# 1. WITI has tasked you to automate a simple grading system.
#As a python student, write a program that you are going to use to display the grades that
#the student will be recieving based on the marks scored in a subject
#The grades are;
# 90% - 100% Grade A
# 80% - 89% Grade B
# 70% - 79% Grade C
# 60% - 60% Grade D
# 50% - 59$ Grade E
# < 50% - Fail
#ANS.,
def calculateGrade():
    mark = int(input('Enter the marks scored:\t'))
    if mark >= 90 and mark <=100:
        print("Grade A")
    elif mark >= 80 and mark <=89:
        print("Grade B") 
    elif mark >= 70  and mark <=79:
        print("Grade C") 
    elif mark >= 60 and mark <=69:
        print("Grade  D") 
    elif mark >= 50 and mark <=59:
        print("Grade E")   
    else:
        print("Fail")  

        calculateGrade()           



#QUESTION FOUR
# WITI Academy is proposing a sacco to help students save their money.
#  Design a platform that will do the following. 
#  Welcome to WITI Academy Sacco
# 1. Deposit Money
# 2. Withdraw Money
# 3. Check Balance
#Ensure if the student select 1, money is deposited and the minimum deposit should be 1000.
#If the student selects 2, money should be withdrawn and  the minimum withdraw is 500.
#If the student selects 3, the account balance should be displayed.
#Make sure you run the program until the student decides to quit.

def saccoTransactions():

    accountBalance = 0
    run = 1

    while run ==1:
        print("\nWelcome to, WITIACADEMY sacco.")

        #menu
        print('1. Deposit Money')
        print('2. Withdraw Money')
        print('3. Check Money')

        studentChoice = int(input("Enter your selection here either (1,2,3):"))
        if studentChoice == 1:
            depositAmount = int(input("Enter the amount to be deposited"))
            print(f'Dear student, you have deposited {depositAmount:,} and your new account balance is {accountBalance:}')
        elif studentChoice == 2:
            print('\n....Processing a withdraw transaction....')
            withdrawAmount = int(input("Enter the amount to be withdrawn:"))
        if accountBalance == 0:
            print("Your balance is  0")   
        elif withdrawAmount < 500:
            print("Minimum withdraw amount is 500") 
        elif withdrawAmount > accountBalance:
            print(f"Withdraw failed, insufficient funds")  
        else:
            accountBalance -= withdrawAmount

            print(f'Dear student, you have withdrawn {withdrawAmount:,} and your new account balance is {accountBalance:,}')
    if studentChoice ==3:
         print(f"Your account balance is {accountBalance:,}")
    else:
         print("You enter a wrong choice!! please select 1,2,3\n")

run = int(input("Enterv1 to continue or any other number to exit:,"))
if run!= 1:
    print("Thanks for using our sacco")

saccoTransactions()
    
             




