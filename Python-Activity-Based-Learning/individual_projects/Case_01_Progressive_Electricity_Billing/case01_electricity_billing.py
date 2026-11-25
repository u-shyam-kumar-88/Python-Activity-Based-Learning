# Case Study 1: Progressive Electricity Billing
# Slabs: 1-100 units @ Rs 3.00, 101-200 @ Rs 4.50, above 200 @ Rs 6.00

fixed_charge = 50
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
units_list = [90, 150, 180, 320, 250, 100]
previous_bill = 0

print("Month  Units  Energy   Fixed  Surch  Rebate   Total  Remark")
print("-" * 62)

for i in range(len(months)):
    units = units_list[i]

    # slab calculation
    if units <= 100:
        energy = units * 3.0
    elif units <= 200:
        energy = 100 * 3.0 + (units - 100) * 4.5
    else:
        energy = 100 * 3.0 + 100 * 4.5 + (units - 200) * 6.0

    # surcharge and rebate
    surcharge = 0
    rebate = 0
    if units > 300:
        surcharge = energy * 0.10
    if units <= 100:
        rebate = energy * 0.05

    total = energy + fixed_charge + surcharge - rebate

    # compare with previous month (unusual increase of more than 25%)
    remark = ""
    if previous_bill > 0:
        increase = (total - previous_bill) / previous_bill * 100
        if increase > 25:
            remark = "UNUSUAL +" + str(round(increase, 1)) + "%"

    print(f"{months[i]:<6}{units:>6}{energy:>8.2f}{fixed_charge:>8.2f}"
          f"{surcharge:>7.2f}{rebate:>7.2f}{total:>9.2f}  {remark}")

    previous_bill = total
