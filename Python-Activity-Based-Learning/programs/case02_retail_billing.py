# Case Study 2: Retail Billing with Multiple Discount Rules
# Item = (name, category, price, quantity)

items = [
    ("Rice 5kg", "grocery", 320, 2),
    ("Headphones", "electronics", 1500, 1),
    ("T-Shirt", "clothing", 400, 3),
    ("Notebook", "stationery", 50, 10),
]

tax_rate = {"grocery": 5, "electronics": 18, "clothing": 12, "stationery": 12}
max_discount = 300

print("=========== INVOICE ===========")
print(f"{'Item':<12}{'Qty':>4}{'Price':>8}{'Amount':>9}{'Tax':>8}")

subtotal = 0
total_tax = 0

for name, category, price, qty in items:  # tuple unpacking
    amount = price * qty
    tax = amount * tax_rate[category] / 100
    subtotal = subtotal + amount
    total_tax = total_tax + tax
    print(f"{name:<12}{qty:>4}{price:>8}{amount:>9.2f}{tax:>8.2f}")

# threshold discount
if subtotal > 5000:
    discount = subtotal * 0.15
elif subtotal > 2000:
    discount = subtotal * 0.10
elif subtotal > 1000:
    discount = subtotal * 0.05
else:
    discount = 0

# maximum concession limit
if discount > max_discount:
    discount = max_discount
    print("(Discount capped at maximum limit)")

grand_total = subtotal - discount + total_tax

print("-" * 37)
print(f"Subtotal      : {subtotal:>10.2f}")
print(f"Discount      : {discount:>10.2f}")
print(f"Total Tax     : {total_tax:>10.2f}")
print(f"GRAND TOTAL   : {grand_total:>10.2f}")
