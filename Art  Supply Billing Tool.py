def greet_customer():
    print("Welcome to the art supply store !")
    print(" New art supplies of top brands just for you !")
greet_customer()

price_per_art = float(input("Enter the price per art in dollars :  "))
art_sold = int(input("Enter the number of art sold : "))
def calculate_total(price , item):
    total = price * item
    return total
total_cost = calculate_total(price_per_art , art_sold)
rounded_cost = (total_cost , 2)
print("Total cost : " , rounded_cost)

amount_paid = float(input("Enter the total amount paid by the customer :  "))
def calculate_change(paid , total):
    change = paid - total
    return change

change_due = calculate_change(amount_paid , rounded_cost)
rounded_change = (change_due , 2)

def thank_you_message():
    if art_sold >= 5:
        print("Thank you for taking this many art supplies")
    else:
        ("Thank you for coming !")

closing_message = thank_you_message(art_sold)

print("===============================")
print("======Art Supply Bill=====")
print("Price per Art : " , price_per_art)
print("Art Sold : " , art_sold)
print("Total Cost : " , rounded_cost)
print("Amount paid : " , amount_paid)
print("Change due :" , rounded_change)
print(closing_message)
print("===============================")

