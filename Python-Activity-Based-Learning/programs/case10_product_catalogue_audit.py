# Case Study 10: Tuple-Based Product Catalogue Audit
# Record = (product_id, name, price, stock)

catalogue = [
    ("P101", "Pen", 10, 200),
    ("P102", "Notebook", 45, 8),
    ("", "Marker", 30, 15),
    ("P104", "Stapler", -60, 20),
    ("P105", "Calculator", 550, 5),
    ("P106", "Eraser", 5, -3),
]

reorder_level = 10
total_value = 0
valid_count = 0

print("Invalid records:")
for record in catalogue:
    pid, name, price, stock = record  # tuple unpacking
    if pid == "" or price <= 0 or stock < 0:
        print("  ", record)

print("\nValid records:")
print(f"{'ID':<6}{'Name':<12}{'Price':>6}{'Stock':>7}{'Value':>8}  Status")
for pid, name, price, stock in catalogue:
    if pid == "" or price <= 0 or stock < 0:
        continue
    value = price * stock
    total_value = total_value + value
    valid_count = valid_count + 1
    status = "OK"
    if stock < reorder_level:
        status = "REPLENISH"
    print(f"{pid:<6}{name:<12}{price:>6}{stock:>7}{value:>8}  {status}")

print("\nValid items      :", valid_count)
print("Total stock value:", total_value)
