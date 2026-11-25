# Case Study 3: Examination Result and Grace-Mark Validation
# Rules: max 100 per subject, pass mark 40, grace up to 5 marks per subject
# only to a failed subject, total grace per student <= 10, marks never exceed 100

names = ["Anil", "Bhavya", "Charan", "Divya"]
marks = [
    [78, 82, 90, 85],
    [38, 45, 60, 52],
    [35, 36, 37, 70],
    [30, 55, 65, 72],
]

subjects = 4
pass_mark = 40
max_mark = 100

for s in range(len(names)):
    grace_used = 0
    final = []
    for j in range(subjects):
        m = marks[s][j]
        if m < pass_mark and (pass_mark - m) <= 5:
            need = pass_mark - m
            if grace_used + need <= 10:
                m = m + need
                grace_used = grace_used + need
        if m > max_mark:
            m = max_mark
        final.append(m)

    failed = 0
    for m in final:
        if m < pass_mark:
            failed = failed + 1

    total = sum(final)
    percent = total / subjects

    if failed > 0:
        result = "FAIL"
    elif percent >= 75:
        result = "DISTINCTION"
    elif percent >= 60:
        result = "FIRST CLASS"
    elif percent >= 50:
        result = "SECOND CLASS"
    else:
        result = "PASS"

    print(names[s], "| Original:", marks[s], "| Final:", final,
          "| Grace:", grace_used, "| Avg:", percent, "|", result)
