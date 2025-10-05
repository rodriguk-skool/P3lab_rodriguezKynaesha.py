# Kynaesha Rodriguez
# 10/5/25

amount = float(input("Enter the amount of money as a float: $"))

cents = int(round(amount * 100))

if cents == 0:
    print("No change")
else:

    dollars = cents // 100
    cents = cents - (dollars * 100)

    quarters = cents // 25
    cents = cents - (quarters * 25)

    dimes = cents // 10
    cents = cents - (dimes * 10)

    nickels = cents // 5
    cents = cents - (nickels * 5)

    pennies = cents 

    if dollars > 0:
        if dollars == 1:
            print("1 Dollar")
        else:
            print(str(dollars) + " Dollars")

    if quarters > 0:
        if quarters == 1:
            print("1 Quarter")
        else:
            print(str(quarters) + " Quarters")

    if dimes > 0:
        if dimes == 1:
            print("1 Dime")
        else:
            print(str(dimes) + " Dimes")

    if nickels > 0:
        if nickels == 1:
            print("1 Nickel")
        else:
            print(str(nickels) + " Nickels")

    if pennies > 0:
        if pennies == 1:
            print("1 Penny")
        else:
            print(str(pennies) + " Pennies")