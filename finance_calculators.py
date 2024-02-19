"""" The program works to calculate how much money an investor gets after depositing money for some period at a chosen interst rate. 
      Also for those who wish to borrow, the expected monthly repayment amount is calculated based on property value, interest and 
      duration of repayment. """


import math

# Displaying options and corresponding information for the user
print('---------------------------------------------------------------------------------')
print('                                                                                 ')
print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond       - to calculate the amount you'll pay on your home loan\n")
print('---------------------------------------------------------------------------------')

# Inputing service request from the user
print('                                                                                 ')
user_input = input("Enter either 'investment' or 'bond' from the menu above to proceed:")

# Lowercasing the user input
user_input_lower = user_input.lower()
#print(user_input_lower)


# Checking if the user request is one of the available options
if(not((user_input_lower == 'investment') or (user_input_lower== 'bond'))):
    print(' There appears to be an error with your input. Please start again.')
    
# User data collection for investing individuals
elif user_input_lower == 'investment':
     
    print('                                                                                 ')
    print('                            INVESTMENT USER DATA                      ')
    print('   ')
    amount_inv = float(input('Please enter how much money you are depositing. '))
    rate_inv = int(input('What is the interest rate you wish to use? '))
    years_inv = int(input('How many years do you plan to invest? '))
    interest = input('Do you want simple or compound interest? ')
    print('')
    print('')

    # Calculating interest for investment- simple and compound
    total_simple = amount_inv *(1+(rate_inv/100)*years_inv)

    total_comp = amount_inv * math.pow((1+(rate_inv/100)),years_inv)

    # Printing interest gained for investment with simple and compound interest

    print('                            MONEY TO BE RECEIVED INVESTMENT                    ')
    print('')
    print('------------------------------------------------------------------------------')
    if interest == 'simple':
        print(f'The amount obtained after {years_inv} years and interest rate of {rate_inv}% is {round(total_simple,2)}')

    elif interest == 'compound':
        print(f'The amount obtained after {years_inv} years and interest rate of {rate_inv}% is {round(total_comp,2)}')

    print('------------------------------------------------------------------------------')
    print('')

# User data collection for borrowing individuals
elif user_input_lower == 'bond':
    print('                                                                                 ')
    
    print('                                                                                 ')
    print('                            BOND USER DATA                      ')
    print('   ')
    house_value = float(input("Please enter the value of your house. "))
    rate_bond = int(input('What is your desired interest rate? '))
    months = int(input('In how many months do you intend to replay the bond? '))
    print('   ')
    print('   ')

    # Calculating bond repayment value
     
    rate_bond_updated = (rate_bond/100)/12

    repayment = (rate_bond_updated * house_value)/(1 - (1 + rate_bond_updated)**(-months))

    # Printing the expected monthly payment
    print('                            MONTHLY REPAYMENT                     ')
    print('')
    print('-------------------------------------------------------------------------------------------------------------')
    print(f"The amount of money to be repaid every month at a interest rate of {rate_bond}% is {round(repayment,2)}.")
    print('--------------------------------------------------------------------------------------------------------------')
    print('')

# Add the advice
    
    if  user_input_lower== 'bond' and repayment > 0.25 * house_value:
        print("")
        print("")
        print('----------------------------------------------------------------------------------------------------------')
        print("The interest appears to be high. May we suggest that you lower the rate and/or extend period of payment")
        print('----------------------------------------------------------------------------------------------------------')
        print('')
        print('----------------------------------------------------------------------------------------------------------')
        print("If you wish to speak to our banker, please make an appointment at reception")
        print('----------------------------------------------------------------------------------------------------------')
        