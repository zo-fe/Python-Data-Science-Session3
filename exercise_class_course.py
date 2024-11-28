class Course:
    def __init__(self, name, description):
        """
        Initialize a Course object with a name, description, and an empty list of students.
        """
        self.name = name
        self.description = description
        self.students = []  # List to store enrolled students

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