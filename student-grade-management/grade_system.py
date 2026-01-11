# Student Grade Management System

def add_students():
    students = {}

    n = int(input("Enter number of students: "))

    for i in range(n):
        name = input(f"\nEnter name of student {i+1}: ")
        subjects = {}
        
        s = int(input(f"Enter number of subjects for {name}: "))
        
        for j in range(s):
            subject = input("Enter subject name: ")
            marks = float(input(f"Enter marks for {subject}: "))
            subjects[subject] = marks
        
        total = sum(subjects.values())
        average = total / s
        
        students[name] = {
            "subjects": subjects,
            "total": total,
            "average": average
        }

    return students


def display_students(students):
    print("\n Student Records")
    print("-" * 40)

    for name, data in students.items():
        print(f"\nStudent Name: {name}")
        print("Subjects & Marks:")
        
        for sub, marks in data["subjects"].items():
            print(f"  {sub}: {marks}")
        
        print(f"Total Marks: {data['total']}")
        print(f"Average Marks: {data['average']:.2f}")


def class_summary(students):
    class_avg = sum(s["average"] for s in students.values()) / len(students)
    topper = max(students.items(), key=lambda x: x[1]["total"])

    print("\n Class Summary")
    print("-" * 40)
    print(f"Class Average: {class_avg:.2f}")
    print(f"Topper: {topper[0]} with Total Marks = {topper[1]['total']}")


# Main Program
students_data = add_students()
display_students(students_data)
class_summary(students_data)
