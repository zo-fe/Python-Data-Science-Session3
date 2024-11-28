#To add grades and compute a student's GPA, we need to extend the Student, Course, and Registration classes
#%%
class Course:
    def __init__(self, name, description):
        """
        Initialize a Course object with a name, description, and an empty list of enrolled students.
        """
        self.name = name
        self.description = description
        self.students = []  # List to store enrolled student names

    def add_student(self, student_name):
        """
        Add a student to the course.
        :param student_name: The name of the student to add.
        """
        if student_name not in self.students:
            self.students.append(student_name)
            print(f"{student_name} has been added to the course {self.name}.")
        else:
            print(f"{student_name} is already enrolled in the course {self.name}.")

    def remove_student(self, student_name):
        """
        Remove a student from the course.
        :param student_name: The name of the student to remove.
        """
        if student_name in self.students:
            self.students.remove(student_name)
            print(f"{student_name} has been removed from the course {self.name}.")
        else:
            print(f"{student_name} is not enrolled in the course {self.name}.")

    def show_students(self):
        """
        Display all students enrolled in the course.
        """
        if self.students:
            print(f"Students enrolled in {self.name}:")
            for student in self.students:
                print(f"- {student}")
        else:
            print(f"No students are currently enrolled in the course {self.name}.")
#%%

#%%
class Student:
    def __init__(self, name, student_id, address):
        """
        Initialize a Student object with name, ID, address, and an empty dictionary for courses and grades.
        """
        self.name = name
        self.student_id = student_id
        self.address = address
        self.courses = {}  # Dictionary to store course names as keys and grades as values

    def enroll_in_course(self, course_name):
        """
        Enroll the student in a course without a grade initially.
        :param course_name: The name of the course to enroll in.
        """
        if course_name not in self.courses:
            self.courses[course_name] = None  # Grade is None initially
            print(f"{self.name} has been enrolled in the course {course_name}.")
        else:
            print(f"{self.name} is already enrolled in the course {course_name}.")

    def drop_course(self, course_name):
        """
        Drop a course from the student's list.
        :param course_name: The name of the course to drop.
        """
        if course_name in self.courses:
            self.courses.pop(course_name)
            print(f"{self.name} has dropped the course {course_name}.")
        else:
            print(f"{self.name} is not enrolled in the course {course_name}.")

    def add_grade(self, course_name, grade):
        """
        Add or update a grade for a course.
        :param course_name: The name of the course.
        :param grade: The grade to assign (0-100 scale).
        """
        if course_name in self.courses:
            self.courses[course_name] = grade
            print(f"Grade {grade} has been assigned to {self.name} for {course_name}.")
        else:
            print(f"{self.name} is not enrolled in the course {course_name}.")

    def calculate_gpa(self):
        """
        Calculate and return the GPA (Grade Point Average) based on enrolled courses with grades.
        """
        grades = [grade for grade in self.courses.values() if grade is not None]
        if grades:
            gpa = sum(grades) / len(grades)  # GPA calculation
            return round(gpa, 2)
        else:
            print(f"{self.name} has no grades yet.")
            return None
#%%

#%%
class Registration:
    def __init__(self):
        """
        Initialize the Registration class with lists to store students and courses.
        """
        self.students = []
        self.courses = []

    def add_student(self, student):
        """
        Add a student to the system.
        :param student: An instance of the Student class.
        """
        self.students.append(student)
        print(f"Student {student.name} has been added to the system.")

    def add_course(self, course):
        """
        Add a course to the system.
        :param course: An instance of the Course class.
        """
        self.courses.append(course)
        print(f"Course {course.name} has been added to the system.")

    def assign_grade(self, student_id, course_name, grade):
        """
        Assign a grade to a student for a specific course.
        :param student_id: The ID of the student.
        :param course_name: The name of the course.
        :param grade: The grade to assign.
        """
        student = next((s for s in self.students if s.student_id == student_id), None)
        if student:
            student.add_grade(course_name, grade)
        else:
            print(f"Student with ID {student_id} does not exist.")

    def calculate_gpa(self, student_id):
        """
        Calculate and return the GPA for a specific student by their ID.
        :param student_id: The ID of the student.
        """
        student = next((s for s in self.students if s.student_id == student_id), None)
        if student:
            gpa = student.calculate_gpa()
            if gpa is not None:
                print(f"{student.name}'s GPA is: {gpa}")
                return gpa
        else:
            print(f"Student with ID {student_id} does not exist.")
            return None
#%%