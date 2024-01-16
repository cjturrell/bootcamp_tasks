"""
Code to calculate either investment or bond as selected by user
Investment - to calculate the amount of interest you'll earn on your investment
User to select simple or compound interest
Bond - to calculate the amount you'll have to pay for a home loan repayment
"""

import math

print("-" * 50)
print("Welcome to the Finance Calculator.  You have two options: \n\
Investment - to calculate the amount of interest you'll earn \on your investment \n\
Bond - to calculate the amount you'll have to pay for a home loan repayment")
print("-" * 50)


user_option = input("Please enter 'investment' or 'bond' to proceed: ")

# Calculation for interest you will earn on investment
if user_option.lower() == "investment":  
    print("-" * 50)
    print("Let's calculate the amount of interest you will earn on your investment!\n")

    user_amount = float(input("How much are you depositing? £"))   
    interest = float(input("What is the interest rate (without %)? "))          
    years = int(input("How many years do you plan of investing? "))

    interest_type = input("\nplease enter 'simple' or 'compound' to proceed: ")

    # Simple interest calculation

    if interest_type.lower() == "simple":
        
        simple_interest = user_amount*(1+(interest/100)*years)               
        
        print("-" * 50)
        print(f"Amount earned with simple interest is £{simple_interest}")  
        print("-" * 50)    
        

    # Compound interest calculation    
    elif interest_type.lower() == "compound":
        
        compound_interest = user_amount*math.pow(1+(interest/100),years)     
        
        print("-" * 50)
        print(f"Amount earned with compound interest is £{compound_interest}")  
        print("-" * 50)

    else:
        print("Sorry option not recognized.")


# Calculation for bond repayments
elif user_option.lower() == "bond":
    print("-" * 50)
    print("Lets calculate your bond repayments!\n")

    house_value = float(input("What is the current value of your house? £"))
    annual_interest = float(input("What is the annual interest rate (without %)? "))
    monthly_interest = (annual_interest/100)/12
    months_repaid = int(input("How many months will the bond be repaid? "))

    repayment = (monthly_interest*house_value)/(1-(1+monthly_interest)**(-months_repaid))

    print("-" * 50)
    print(f"Your monthly repayments are £{repayment}")
    print("-" * 50)

# If 'investment' or 'bond' not input by user
else:
    print ("Sorry option not recognized.")