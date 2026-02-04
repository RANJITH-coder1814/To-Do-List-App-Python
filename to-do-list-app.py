tasks = []

while True:
    print("\n1.Add 2.View 3.Remove 4.Exit")
    ch = int(input("Choose: "))

    if ch == 1:
        tasks.append(input("Enter task: "))
    elif ch == 2:
        print("\nTasks:")
        for i, t in enumerate(tasks, 1):
            print(i, t)
    elif ch == 3:
        tasks.pop(int(input("Task number: ")) - 1)
    else:
        break
