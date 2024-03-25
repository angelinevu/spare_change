from change import penny, nickel, dime, quarter, dollar

#Main function
def main():
    balance = int(input("\nNumber of pennies: "))
    if balance == 0:
        print("\nNo change.")
    elif balance > 0:
        print("\nChange:")
        penny(nickel(dime(quarter(dollar(balance)))))
    else:
        print("\nInvalid Input.")

if __name__ == "__main__":
    main()