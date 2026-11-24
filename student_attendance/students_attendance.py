students = [
    ["rishi", "CSECS", "26001863"],
    ["pranathi", "CSECS", "26001865"],
    ["supritha", "CSECS", "26001866"],
    ["bhavya", "CSECS", "26001867"],
    ["hari", "CSECS", "26001868"],
    ["harshith", "CSECS", "26001869"],
    ["sai", "CSECS", "26001870"],
    ["pujith", "CSECS", "26001871"],
    ["srija", "CSECS", "26001872"],
    ["sita", "CSECS", "26001873"],
    ["kavya", "CSECS", "26001874"],
    ["bindhu", "CSECS", "26001875"],
    ["moulika", "CSECS", "26001876"],
    ["lasya", "CSECS", "26001877"],
    ["samith", "CSECS", "26001878"],
    ["nithin", "CSECS", "26001879"],
    ["navya", "CSECS", "26001880"],
    ["lahari", "CSECS", "26001881"],
    ["sujitha", "CSECS", "26001882"],
    ["ajay", "CSECS", "26001883"]
]

present = 0
absent = 0

for student_list in students:
    print("\nName:", student_list[0])
    print("Section:", student_list[1])
    print("Roll Number:", student_list[2])

    status = input("Enter attendance (P/A): ").upper()

    while status != "P" and status != "A":
        print("Invalid input! Enter P or A.")
        status = input("Enter attendance (P/A): ").upper()

    if status == "P":
        student_list.append("Present")
        present += 1
    else:
        student_list.append("Absent")
        absent += 1

print("\n----- Attendance Report -----")

for student_list in students:
    print(student_list[0], student_list[1],
          student_list[2], student_list[3])

print("\nTotal students:", len(students))
print("Total students present:", present)
print("Total students absent:", absent)