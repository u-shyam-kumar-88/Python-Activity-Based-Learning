# Case Study 6: Advanced Numeric Pattern Generator (Hollow Diamond)

sizes = [5, 3, 1, 0, -2]

for n in sizes:
    print("--- n =", n, "---")
    if n < 1:  # n = number of rows in the top half
        print("Invalid dimension! n must be 1 or more.")
        continue

    # upper half (including middle row)
    for i in range(1, n + 1):
        line = " " * (n - i) + str(i)
        if i > 1:
            line = line + " " * (2 * i - 3) + str(i)
        print(line)

    # lower half
    for i in range(n - 1, 0, -1):
        line = " " * (n - i) + str(i)
        if i > 1:
            line = line + " " * (2 * i - 3) + str(i)
        print(line)
