# 🎓 EduSphere - School Management System

EduSphere is a console-based school management system built using Python and Object-Oriented Programming (OOP) principles. It models a real-world academic environment where users can manage classrooms, students, teachers, subjects, and exam results efficiently.

## 🚀 Features

- 📚 Manage multiple Classrooms
- 👩‍🏫 Add Teachers and assign them to Subjects
- 🧑‍🎓 Admit Students into Classrooms
- 🧪 Conduct Semester Final Exams
- 📈 Calculate & View Grades with GPA
- ✅ Static methods for grading logic
- 💡 Friendly CLI with error handling and clear prompts

## 🧩 Object-Oriented Structure

The project is divided into well-structured classes:

### 1. `School`

- Attributes: `name`, `address`, `teachers`, `classrooms`
- Methods: `add_classroom()`, `add_teacher()`, `student_admission()`, `calculate_grade()`, `grade_to_value()`, `value_to_grade()`

### 2. `ClassRoom`

- Attributes: `name`, `students`, `subjects`
- Methods: `add_student()`, `add_subject()`, `take_semester_final_exam()`

### 3. `Subject`

- Attributes: `name`, `teacher`, `max_marks`, `pass_marks`
- Methods: `exam(students)`

### 4. `Person` (Base class)

- Attributes: `name`

### 5. `Teacher` (Inherits `Person`)

- Methods: `evaluate_exam()` - generates random exam scores

### 6. `Student` (Inherits `Person`)

- Attributes: `marks`, `subject_grade`, `grade`, `classroom`
- Methods: `calculate_final_grade()`
- Properties: `id`

## 🖥️ User Interface

The app provides an interactive **CLI menu** that supports:
