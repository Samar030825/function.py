def greet_customer():
    print(" Welcome to the lemonade stand")
    print("Freshly made lemonade for you")
greet_customer()
price_per_cup = float(input("Enter the price of cup in dollars :"))
cup_sold = int(input("Enter the amount of cup sold : "))
def calculate_total(price , cup):
    total = price * cup
    return total
total_cost = calculate_total(price_per_cup , cup_sold)
rounded_cost = round( total_cost , 2)
print("total cost : " , rounded_cost)
amount_paid = float(input(" Enter the total amount paid by the customer :"))
def calculate_change(paid , total):
    change = paid - total
    return change

change_due = calculate_change( amount_paid , rounded_cost)
rounded_change = round(change_due , 2)
def thank_you_message(cup):
    if cup>= 5:
        return "wow big order thank you for your support"
    else:
        return  "Thank for stopping by the store"

closing_message = thank_you_message(cup_sold)
print("=======LEMONADE STAND RECIEPT=======")
print("price per cup : " , price_per_cup)
print("Cup sold : " , cup_sold)
print("Total cost : " , rounded_cost)
print("Amount paid : " , amount_paid)
print("Change due : " , change_due)
print(closing_message)
print("=========================================")