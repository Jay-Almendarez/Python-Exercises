starting_balance = 0

def curr_bal():
    return starting_balance

def credit():
    dp = float(input('Absolutely! How much would you like to deposit?'))
    '''
    The function credit will take an input from the user and will make changes to the current balance (adding the input to the existing balance).
    
    return: float
    
    '''
    if starting_balance == 0:
        alt_bal = starting_balance + dp
    elif starting_balance < 0 or starting_balance > 0:
        alt_bal = curr_bal() + dp
    return alt_bal

def debit():
    wd = float(input('No problem! How much are we taking out?'))
    '''
    The function debit will take an input from the user and will make changes to the current balance (subtracting the input from the existing balance).
    
    return: float
    
    '''
    if starting_balance == 0:
        alt_bal2 = starting_balance - wd
    elif starting_balance < 0 or starting_balance > 0:
        alt_bal2 = curr_bal() - wd
    return alt_bal2


def exit():
    '''
    The function exit will tell user to have a great day then close.
    '''
    return print('\nHave a great rest of your day!')


# Actual start of program
print("Hello there. \nWhat can we help you with today?")
while True:
    base = input('1 view current balance\n2 add a credit (deposit funds) \n3 add a debit (withdraw funds) \n4 exit\n: ') 
    if base in '1' or base.lower() in 'view current balance':
        print("Sure! Let's take a look...")
        print('')
        print(f'Your current balance is ${curr_bal()}')
        print('')
        add_help_bal = input("Is there anything else I can help you with while you're here? (yes/no):")
        if add_help_bal.lower() == 'yes':
            continue
        elif add_help_bal.lower() == 'no':
            break
        else:
            print('Invalid entry. Try entering yes or no')
            # gotta have my personal space
            print('')
        continue
    elif base in '3' or base.lower() in 'withdraw funds' or base.lower() in 'add a debit':
        print('')
        print(f'Your new balance is ${debit()}')
        print('')
        add_help_wd = input("Is there anything else I can help you with while you're here? (yes/no):")
        if add_help_wd.lower() == 'yes':
            continue
        elif add_help_wd.lower() == 'no':
            break
        else:
            print('Invalid entry. Try entering yes or no')
            # gotta have my personal space
            print('')
        continue
    elif base in '2' or base.lower() in 'deposit' or base.lower() in 'add a credit':
        print('')
        print(f'Your new balance is ${credit()}')
        print('')
        add_help_dp = input("Is there anything else I can help you with while you're here? (yes/no):")
        if add_help_dp.lower() == 'yes':
            continue
        elif add_help_dp.lower() == 'no':
            break
        else:
            print('Invalid entry. Try entering yes or no')
            # gotta have my personal space
            print('')
        continue
    elif base in '4' or base.lower() in 'exit':
        exit()
        break
    else:
        print("Invalid entry. Try to enter 1, 2, 3, or 4")
        # gotta have my personal space
        print('')
    continue