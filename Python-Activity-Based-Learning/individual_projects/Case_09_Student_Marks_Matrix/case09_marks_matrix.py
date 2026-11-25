# Case Study 9: Student Marks Matrix Analysis

students = ["Asha", "Bala", "Chitra", "Dev", "Esha"]
subjects = ["Maths", "Physics", "Chem", "English"]
marks = [
    [85, 78, 92, 70],
    [60, 45, 50, 65],
    [95, 88, 90, 85],
    [40, 35, 48, 55],
    [72, 66, 58, 80],
]

print("Row-wise (student) statistics")
best_total = -1
best_student = ""
for i in range(len(students)):
    total = sum(marks[i])
    avg = total / len(subjects)
    print(f"  {students[i]:<7} total={total:<4} avg={avg:.2f} max={max(marks[i])} min={min(marks[i])}")
    if total > best_total:
        best_total = total
        best_student = students[i]

print("Top performer:", best_student, "with", best_total, "marks")

print("\nColumn-wise (subject) statistics")
for j in range(len(subjects)):
    col_total = 0
    for i in range(len(students)):
        col_total = col_total + marks[i][j]
    col_avg = col_total / len(students)
    remark = ""
    if col_avg < 65:
        remark = "<-- LOW AVERAGE"
    print(f"  {subjects[j]:<8} avg={col_avg:.2f} {remark}")
