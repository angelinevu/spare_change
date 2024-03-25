import math

#How many dollars?
def dollar(balance) -> int:
    dollar = math.trunc(balance / 100)
    if dollar == 1:
        print(dollar, 'dollar bill')
    if dollar > 1:
        print(dollar, 'dollar bills')

    residual = balance % 100
    return residual

#How many quarters?
def quarter(balance) -> int:
    quarter = math.trunc(balance / 25)
    if quarter == 1:
        print(quarter, 'quarter')
    if quarter > 1:
        print(quarter, 'quarters')

    residual = balance % 25
    return residual


#How many dimes?
def dime(balance) -> int:
    dime = math.trunc(balance / 10)
    if dime == 1:
        print(dime, 'dime')
    if dime > 1:
        print(dime, 'dimes')

    residual = balance % 10
    return residual

#How many nickels?
def nickel(balance) -> int:
    nickel = math.trunc(balance / 10)
    if nickel == 1:
        print(nickel, 'nickel')
    if nickel > 1:
        print(nickel, 'nickels')

    residual = balance % 5
    return residual

#How many pennies?
def penny(balance) -> int:
    penny = math.trunc(balance)
    if penny == 1:
        print(penny, 'penny')
    if penny > 1:
        print(penny, 'pennies') 
    return
