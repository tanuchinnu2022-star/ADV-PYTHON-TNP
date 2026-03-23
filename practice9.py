employees = {}

while True:
    print("\n1.Add 2.Remove 3.Display 4.Exit")
    ch = input("Enter choice: ")

    if ch == "1":
        name = input("Enter name: ")
        employees[name] = "Present"

    elif ch == "2":
        name = input("Enter name: ")
        employees.pop(name, None)

    elif ch == "3":
        print(employees)

    elif ch == "4":
        break