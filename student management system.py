from pymongo import MongoClient


def get_collection():
    client = MongoClient("mongodb://localhost:27017/")
    db = client["student_db"]
    return db["students"]

def insert_student():
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    course = input("Enter course: ")

    student = {
        "name": name,
        "age": age,
        "course": course
    }

    collection = get_collection()
    collection.insert_one(student)
    print("Student inserted successfully!")

def update_student():
    name = input("Enter student name to update: ")
    new_course = input("Enter new course: ")

    collection = get_collection()
    result = collection.update_one(
        {"name": name},
        {"$set": {"course": new_course}}
    )

    if result.modified_count > 0:
        print("Student updated successfully!")
    else:
        print("Student not found!")


def delete_student():
    name = input("Enter student name to delete: ")

    collection = get_collection()
    result = collection.delete_one({"name": name})

    if result.deleted_count > 0:
        print("Student deleted successfully!")
    else:
        print("Student not found!")


def search_student():
    name = input("Enter student name to search: ")

    collection = get_collection()
    student = collection.find_one({"name": name})

    if student:
        print("Name:", student["name"])
        print("Age:", student["age"])
        print("Course:", student["course"])
    else:
        print("Student not found!")


def menu():
    while True:
        print("\n--- Student Management System (MongoDB) ---")
        print("1. Insert Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. Search Student")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            insert_student()
        elif choice == '2':
            update_student()
        elif choice == '3':
            delete_student()
        elif choice == '4':
            search_student()
        elif choice == '5':
            print("Exiting program...")
            break
        else:
            print("Invalid choice!")

# Run application
menu()
