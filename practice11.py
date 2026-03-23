menu = {
    "pizza": 200,
    "burger": 100,
    "pasta": 150,
    "coffee": 50
}

total = 0

while True:
    print("\nMenu:", menu)
    item = input("Enter item (or 'done'): ").lower()

    if item == "done":
        break

    if item in menu:
        qty = int(input("Enter quantity: "))
        total += menu[item] * qty
    else:
        print("Item not available")

# Tax (10%)
tax = total * 0.10
bill = total + tax

print("Total:", total)
print("Tax:", tax)
print("Final Bill:", bill)