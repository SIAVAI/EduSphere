import random

# Base Person class
class Person:
    def __init__(self, name):
        self.name = name


# Teacher class
class Teacher(Person):
    def __init__(self, name):
        super().__init__(name)

    def teach(self):
        print(f"{self.name} is teaching...")

    def evaluate_exam(self):
        return random.randint(30, 100)


# Student class
class Student(Person):
    def __init__(self, name, classroom):
        super().__init__(name)
        self.classroom = classroom
        self.__id = None
        self.marks = {}
        self.subject_grade = {}
        self.grade = None

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    def calculate_final_grade(self):
        try:
            if not self.subject_grade:
                return f"{self.name} has not attended any exams yet."

            total = sum(School.grade_to_value(g) for g in self.subject_grade.values())
            gpa = total / len(self.subject_grade)
            self.grade = School.value_to_grade(gpa)
            return f"🎓 {self.name}'s Final Grade: {self.grade} | GPA: {gpa:.2f}"
        except Exception as e:
            return f"Oops! Couldn't calculate grade for {self.name}. Error: {str(e)}"


# Subject class
class Subject:
    def __init__(self, name, teacher):
        self.name = name
        self.teacher = teacher
        self.max_marks = 100
        self.pass_marks = 33

    def exam(self, students):
        print(f"\n📘 Conducting Exam for {self.name}")
        for student in students:
            try:
                mark = self.teacher.evaluate_exam()
                student.marks[self.name] = mark
                student.subject_grade[self.name] = School.calculate_grade(mark)
                print(f"{student.name} scored {mark} in {self.name}")
            except Exception:
                print(f"❌ Couldn't evaluate {student.name}'s exam for {self.name}.")


# ClassRoom class
class ClassRoom:
    def __init__(self, name):
        self.name = name
        self.students = []
        self.subjects = []

    def add_student(self, student):
        try:
            roll_no = f"{self.name}-{len(self.students) + 1}"
            student.id = roll_no
            self.students.append(student)
            print(f"✅ {student.name} admitted with ID: {student.id}")
        except Exception:
            print(f"❌ Failed to admit student {student.name}.")

    def add_subject(self, subject):
        self.subjects.append(subject)
        print(f"📚 Subject {subject.name} added to {self.name}")

    def take_semester_final(self):
        print(f"\n📝 Semester Finals for {self.name}")
        for subject in self.subjects:
            subject.exam(self.students)
        for student in self.students:
            print(student.calculate_final_grade())

    def get_top_students(self):
        print("\n🏆 Top Students")
        try:
            sorted_students = sorted(
                self.students,
                key=lambda s: sum(School.grade_to_value(g) for g in s.subject_grade.values()),
                reverse=True
            )
            for idx, student in enumerate(sorted_students[:3], start=1):
                print(f"{idx}. {student.name} - Grade: {student.grade}")
        except Exception as e:
            print(f"❌ Could not determine top students: {str(e)}")


# School class
class School:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.teachers = {}
        self.classrooms = {}

    def add_classroom(self, classroom):
        self.classrooms[classroom.name] = classroom
        print(f"🏫 Classroom {classroom.name} added to school")

    def add_teacher(self, subject, teacher):
        self.teachers[subject] = teacher
        print(f"👩‍🏫 Teacher {teacher.name} assigned to {subject}")

    def student_admission(self, student):
        classname = student.classroom.name
        if classname in self.classrooms:
            self.classrooms[classname].add_student(student)
        else:
            print(f"❌ Classroom {classname} does not exist in school!")

    @staticmethod
    def calculate_grade(marks):
        if 80 <= marks <= 100:
            return 'A+'
        elif 70 <= marks < 80:
            return 'A'
        elif 60 <= marks < 70:
            return 'A-'
        elif 50 <= marks < 60:
            return 'B'
        elif 40 <= marks < 50:
            return 'C'
        elif 33 <= marks < 40:
            return 'D'
        else:
            return 'F'

    @staticmethod
    def grade_to_value(grade):
        grade_map = {
            'A+': 5.00,
            'A': 4.00,
            'A-': 3.50,
            'B': 3.00,
            'C': 2.00,
            'D': 1.00,
            'F': 0.00
        }
        return grade_map.get(grade, 0.00)

    @staticmethod
    def value_to_grade(value):
        if 4.5 <= value <= 5.00:
            return 'A+'
        elif 3.5 <= value < 4.5:
            return 'A'
        elif 3.0 <= value < 3.5:
            return 'A-'
        elif 2.5 <= value < 3.0:
            return 'B'
        elif 2.0 <= value < 2.5:
            return 'C'
        elif 1.0 <= value < 2.0:
            return 'D'
        else:
            return 'F'

    def __repr__(self):
        display = f"\n📍 Welcome to {self.name}\n📬 Address: {self.address}\n"
        display += "\n🏫 Classrooms:\n"
        for cname in self.classrooms:
            display += f" - {cname}\n"

        for cname, classroom in self.classrooms.items():
            display += f"\n👨‍🎓 Students in {cname}:\n"
            for student in classroom.students:
                display += f"   • {student.name} (ID: {student.id})\n"

            display += f"\n📘 Subjects in {cname}:\n"
            for subject in classroom.subjects:
                display += f"   • {subject.name} (Teacher: {subject.teacher.name})\n"

        return display


def main():
    print("="*50)
    print("🎓 Welcome to EduSphere School Management System 🎓")
    print("="*50)
    
    school = School("Bright Future International School", "123 Sunshine Ave, Dhaka")
    
    while True:
        print("\n🧭 Main Menu:")
        print("1. Add Classroom")
        print("2. Add Teacher")
        print("3. Add Subject to Classroom")
        print("4. Admit Student")
        print("5. Take Semester Final Exam")
        print("6. View All Students")
        print("7. View Final Grades")
        print("8. Exit")

        try:
            choice = int(input("Enter your choice (1-8): "))
        except ValueError:
            print("❌ Please enter a valid number between 1 and 8.")
            continue

        if choice == 1:
            name = input("Enter classroom name: ").strip()
            if name in school.classrooms:
                print(f"⚠️ Classroom '{name}' already exists!")
            else:
                classroom = ClassRoom(name)
                school.add_classroom(classroom)
                print(f"✅ Classroom '{name}' added successfully.")

        elif choice == 2:
            subject = input("Enter subject name: ").strip()
            teacher_name = input("Enter teacher's name: ").strip()
            teacher = Teacher(teacher_name)
            school.add_teacher(subject, teacher)
            print(f"✅ Teacher '{teacher_name}' assigned to subject '{subject}'.")

        elif choice == 3:
            classroom_name = input("Enter classroom name: ").strip()
            subject_name = input("Enter subject name: ").strip()

            if classroom_name not in school.classrooms:
                print(f"❌ Classroom '{classroom_name}' not found!")
                continue
            if subject_name not in school.teachers:
                print(f"❌ No teacher assigned to '{subject_name}'. Please add a teacher first.")
                continue
            
            classroom = school.classrooms[classroom_name]
            teacher = school.teachers[subject_name]
            subject = Subject(subject_name, teacher)
            classroom.add_subject(subject)
            print(f"✅ Subject '{subject_name}' added to Classroom '{classroom_name}'.")

        elif choice == 4:
            student_name = input("Enter student name: ").strip()
            classroom_name = input("Enter classroom to admit the student into: ").strip()
            if classroom_name not in school.classrooms:
                print(f"❌ Classroom '{classroom_name}' not found!")
                continue
            classroom = school.classrooms[classroom_name]
            student = Student(student_name, classroom)
            school.student_admission(student)
            print(f"✅ Student '{student_name}' admitted to Classroom '{classroom_name}'.")

        elif choice == 5:
            classroom_name = input("Enter classroom name to conduct exams: ").strip()
            if classroom_name not in school.classrooms:
                print(f"❌ Classroom '{classroom_name}' not found!")
                continue
            classroom = school.classrooms[classroom_name]
            classroom.take_semester_final_exam()
            print(f"✅ Exams conducted for Classroom '{classroom_name}'.")

        elif choice == 6:
            print("\n📚 Students Info")
            print(school)

        elif choice == 7:
            print("\n📊 Final Grades Summary")
            for classroom in school.classrooms.values():
                for student in classroom.students:
                    print(student.calculate_final_grade())

        elif choice == 8:
            print("👋 Thank you for using EduSphere. Goodbye!")
            break

        else:
            print("❌ Invalid choice. Please enter a number from 1 to 8.")

if __name__ == "__main__":
    main()

