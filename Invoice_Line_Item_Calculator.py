def get_price():
    while True:
        try:
            price = float(input("Enter the price: $"))
            if price < 0:
                raise ValueError
            return price
        except ValueError:
            print("Invalid decimal number. Please try again.")

def get_quantity():
    while True:
        try:
            quantity = int(input("Enter the quantity: "))
            if quantity < 0:
                raise ValueError
            return quantity
        except ValueError:
            print("Invalid integer. Please try again.")

def get_exit_loop():
    while True:
        try:
            choice = input("Do you want to enter another line item? (y/n): ")
            if choice.lower() == 'y':
                return choice
            elif choice.lower() == 'n':
                return choice
            else:
                raise ValueError
        except ValueError:    
                print("Invalid integer. Please try again.")
                continue
def main():
    print("The invoice line item calculator \n")
    total = 0.0
    
    while True:
        print()
        price = get_price()
        quantity = get_quantity()
        
        line_total = round(price * quantity,)
        total += line_total
        print()
        print("Price: ${:.2f}".format(price))
        print(f"Quantity: {quantity}")
        print("Total: ${:.2f}".format(line_total))
        
        choice = get_exit_loop()
        if choice == "n":
            print()
            print("Invoice Total: ${:.2f}".format(total))
            print("Thank you, Good buy ;)")
            break
        
        
if __name__ == "__main__":
    main()