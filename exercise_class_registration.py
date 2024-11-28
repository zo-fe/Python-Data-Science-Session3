class Registration:
    def __init__(self):
        """
        Initialize the Registration class with lists to store students and courses.
        """
        self.students = []  # List to store Student objects
        self.courses = []   # List to store Course objects

    def add_course(self, course):
        """
        Add a course to the system.
        :param course: An instance of the Course class.
        """
        self.courses.append(course)
        print(f"Course {course.name} has been added to the system.")

    def add_student(self, student):
        """
        Add a student to the system.
        :param student: An instance of the Student class.
        """
        self.students.append(student)
        print(f"Student {student.name} has been added to the system.")

    def enroll_student_in_course(self, student_id, course_name):
        """
        Enroll a student in a specific course.
        :param student_id: The ID of the student.
        :param course_name: The name of the course.
        """
        student = next((s for s in self.students if s.student_id == student_id), None)
        course = next((c for c in self.courses if c.name == course_name), None)
        
        if student and course:
            student.enroll_in_course(course_name)
            course.add_student(student.name)
        else:
            print(f"Either the student (ID: {student_id}) or the course ({course_name}) does not exist.")

    def drop_student_from_course(self, student_id, course_name):
        """
        Drop a student from a specific course.
        :param student_id: The ID of the student.
        :param course_name: The name of the course.
        """
        student = next((s for s in self.students if s.student_id == student_id), None)
        course = next((c for c in self.courses if c.name == course_name), None)

        if student and course:
            student.drop_course(course_name)
            course.remove_student(student.name)
        else:
            print(f"Either the student (ID: {student_id}) or the course ({course_name}) does not exist.")

    def show_all_courses(self):
        """
        Display all courses available in the system.
        """
        if self.courses:
            print("Available courses:")
            for course in self.courses:
                print(f"- {course.name}: {course.description}")
        else:
            print("No courses are currently available.")

    def show_all_students(self):
        """
        Display all students registered in the system.
        """
        if self.students:
            print("Registered students:")
            for student in self.students:
                print(f"- {student.name} (ID: {student.student_id}, Address: {student.address})")
        else:
            print("No students are currently registered.")