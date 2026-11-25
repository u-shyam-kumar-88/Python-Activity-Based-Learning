# Case Study 4: Attendance Recovery Computation
# Find minimum consecutive classes to attend to reach the threshold

threshold = 75
students = [("Ravi", 40, 28), ("Sita", 60, 50), ("Kiran", 50, 30)]  # (name, held, attended)
future_rates = [100, 90, 80, 70]  # % of future classes the student will attend

for name, held, attended in students:
    current = attended / held * 100
    print(f"{name}: held={held}, attended={attended}, current={current:.2f}%")
    if current >= threshold:
        print("   Already eligible. No extra classes needed.")
        continue

    for rate in future_rates:
        n = 0
        got_it = False
        while n <= 500:
            new_attended = attended + n * rate / 100
            new_percent = new_attended / (held + n) * 100
            if new_percent >= threshold:
                got_it = True
                break
            n = n + 1

        if got_it:
            print(f"   If attending {rate}% of future classes: need {n} more classes ({new_percent:.2f}%)")
        else:
            print(f"   If attending {rate}% of future classes: threshold can NEVER be reached")
