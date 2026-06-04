MAX_LINES = 3
MAX_BET = 1000
MIN_BET = 1

def deposit():
    while True:
        amount = input("what will you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0 :
                break
            else:
                print("amount must be greater than zero")
        else:
            print("please enter a number ")

    return amount 

def get_number_of_lines():
    while True:
        lines = input("enter number of lines you want to bet on ( 1 " + "- " + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES :
                break
            else:
                print("enter a valid number of lines")
        else:
            print("please enter a number of lines ")

    return lines 

def get_bet():
    while True:
        amount = input("what will you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET  <= amount <= MAX_BET :
                break
            else:
                print( f"amount must be between ${MIN_BET} - ${MAX_BET}")
        else:
            print("please enter a number ")

    return amount 


def main():
    balance = deposit()  
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"you dont have enough deposit, your current balance is ${balance} ")
        else:
            break

    print(f"you are beting ${bet} on ${lines} lines. total bet is equal to ${total_bet}  ")
    print(balance , lines)

main()      