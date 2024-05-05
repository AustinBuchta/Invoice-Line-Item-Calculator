def get_price():
    while True:
        try:
            price = float(input("Enter the price: $"))
            if price < 0:
                raise ValueError
            return price
        except ValueError:
            print("Invalid input. Please enter a valid price (a non-negative decimal number with two decimal places).")

def get_quantity():
    while True:
        try:
            quantity = int(input("Enter the quantity: "))
            if quantity < 0:
                raise ValueError
            return quantity
        except ValueError:
            print("Invalid input. Please enter a valid quantity (a non-negative integer).")
    
def main():
    print("The invoice line item calculator \n")
    total = 0.0
    
    while True:
        price = get_price()
        quantity = get_quantity()
        
        line_total = round(price * quantity, 2)
        total += line_total
        
        print("\nPrice: $ {:.2f}".format(price))
        print(f"Quantity: {quantity}")
        print("Total: $ {:.2f}".format(line_total))
        
        
        choice = input("Do you want to enter another line item? (y/n): ")
        print()
        if choice.lower() == 'y':
            continue
        else:
            print("Ending Total: $ {:.2f}".format(total))
            print("Thank you, Good buy ;)")
            break
        
if __name__ == "__main__":
    main()