students = {}

while True:
    print("\n1.Add 2.Update 3.Delete 4.Display 5.Exit")
    ch = input("Choice: ")

    if ch == "1":
        name = input("Name: ")
        marks = int(input("Marks: "))
        students[name] = marks

    elif ch == "2":
        name = input("Name: ")
        if name in students:
            students[name] = int(input("New Marks: "))

    elif ch == "3":
        name = input("Name: ")
        students.pop(name, None)

    elif ch == "4":
        print(students)

    elif ch == "5":
        break