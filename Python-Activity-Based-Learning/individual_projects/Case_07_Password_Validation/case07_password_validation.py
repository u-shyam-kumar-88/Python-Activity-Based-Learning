# Case Study 7: Password Policy Validation Engine

passwords = ["Hello@123", "abc", "PASSWORD1!", "Aaa@bbb111", "Str0ng#Pass"]
special = "!@#$%^&*"
banned = ["password", "1234", "admin", "qwerty"]

for pw in passwords:
    errors = []

    if len(pw) < 8:
        errors.append("Length is less than 8")

    up = low = dig = sp = 0
    for ch in pw:
        if "A" <= ch <= "Z":
            up = up + 1
        elif "a" <= ch <= "z":
            low = low + 1
        elif "0" <= ch <= "9":
            dig = dig + 1
        elif ch in special:
            sp = sp + 1

    if up == 0:
        errors.append("No uppercase letter")
    if low == 0:
        errors.append("No lowercase letter")
    if dig == 0:
        errors.append("No digit")
    if sp == 0:
        errors.append("No special character (!@#$%^&*)")

    # repetition: same character 3 times in a row
    for i in range(len(pw) - 2):
        if pw[i] == pw[i + 1] == pw[i + 2]:
            errors.append("Character repeated 3 times: '" + pw[i] + "'")
            break

    # prohibited substrings
    lower_pw = pw.lower()
    for word in banned:
        if word in lower_pw:
            errors.append("Contains prohibited text: " + word)

    if len(errors) == 0:
        print(pw, "-> VALID")
    else:
        print(pw, "-> INVALID")
        for e in errors:
            print("     *", e)
