import random


MAX_LINES = 3
MAX_BET = 1000
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count ={
    "A": 2,
    "B": 4,
    "C": 5,
    "D": 8,
}

def sloth_spin( rows , cols ,symbols):
    all_symbols = []
    for symbol , symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    
    columns = []
    for  _  in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for  _  in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns

def print_sloth_machine(columns):
    for row in range (len(columns[0])):
        for i ,column in enumerate(columns):
            if i != len(columns) -1 :
                print(column[row], end="|" )
            else:
                print(columns[row], end="")

        print()

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

    slots =  sloth_spin (ROWS ,COLS , symbol_count )
    print_sloth_machine(slots)
    
main()      