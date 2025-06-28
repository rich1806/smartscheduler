Alrich
# Smart Scheduler

exams = []

def add_exam():
    name = input("Enter exam name: ")
    date = input("Enter exam date (YYYY-MM-DD): ")
    time = input("Enter exam time (HH:MM): ")
    room = input("Enter assigned room: ")
    exams.append({
        "name": name,
        "date": date,
        "time": time,
        "room": room
    })
    print("Exam added successfully!\n")

def view_exams():
    if not exams:
        print("No exams scheduled.\n")
        return
    print("\nExam Schedule:")
    for idx, exam in enumerate(exams):
        print(f"{idx + 1}. {exam['name']} - {exam['date']} at {exam['time']} in Room {exam['room']}")
    print()

def edit_exam():
    view_exams()
    if not exams:
        return
    try:
        index = int(input("Enter exam number to edit: ")) - 1
        if 0 <= index < len(exams):
            print("Leave blank to keep current value.")
            new_name = input(f"New name (current: {exams[index]['name']}): ") or exams[index]['name']
            new_date = input(f"New date (current: {exams[index]['date']}): ") or exams[index]['date']
            new_time = input(f"New time (current: {exams[index]['time']}): ") or exams[index]['time']
            new_room = input(f"New room (current: {exams[index]['room']}): ") or exams[index]['room']
            exams[index] = {
                "name": new_name,
                "date": new_date,
                "time": new_time,
                "room": new_room
            }
            print("Exam updated successfully!\n")
        else:
            print("Invalid exam number.\n")
    except ValueError:
        print("Please enter a valid number.\n")

def delete_exam():
    view_exams()
    if not exams:
        return
    try:
        index = int(input("Enter exam number to delete: ")) - 1
        if 0 <= index < len(exams):
            deleted = exams.pop(index)
            print(f"Deleted exam: {deleted['name']}\n")
        else:
            print("Invalid exam number.\n")
    except ValueError:
        print("Please enter a valid number.\n")

def menu():
    while True:
        print("Smart Scheduler Menu")
        print("1. Add Exam")
        print("2. View All Exams")
        print("3. Edit Exam")
        print("4. Delete Exam")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")
        print()
        if choice == '1':
            add_exam()
        elif choice == '2':
            view_exams()
        elif choice == '3':
            edit_exam()
        elif choice == '4':
            delete_exam()
        elif choice == '5':
            print("Exiting Smart Scheduler. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

# Start the program
if _name_ == "_main_":
    menu()