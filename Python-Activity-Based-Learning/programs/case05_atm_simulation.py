# Case Study 5: ATM Transaction Sequence Simulation
# D = deposit, W = withdrawal. Withdrawal limit per transaction = 10000

balance = 5000
limit = 10000
transactions = [
    ("D", 2000), ("W", 1500), ("W", 20000), ("W", 9000),
    ("D", -100), ("X", 500), ("W", 4000), ("W", 12000)
]

deposits = 0
withdrawals = 0
rejected = 0
count = 0

print("No  Type  Amount   Status      Balance")
print("-" * 45)

for t, amount in transactions:
    count = count + 1
    status = "OK"

    if amount <= 0:
        status = "REJ-amount"
    elif t == "D":
        balance = balance + amount
        deposits = deposits + amount
    elif t == "W":
        if amount > limit:
            status = "REJ-limit"
        elif amount > balance:
            status = "REJ-funds"
        else:
            balance = balance - amount
            withdrawals = withdrawals + amount
    else:
        status = "REJ-type"

    if status != "OK":
        rejected = rejected + 1

    print(f"{count:<4}{t:<4}{amount:>8}   {status:<11}{balance:>7}")

print("-" * 45)
print("Total deposited  :", deposits)
print("Total withdrawn  :", withdrawals)
print("Rejected         :", rejected)
print("Final balance    :", balance)
