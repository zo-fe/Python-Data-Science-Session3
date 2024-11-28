class Student:
    def __init__(self, name, student_id, address):
        """
        Initialize a Student object with name, student ID, address, and an empty list of enrolled courses.
        """
        self.name = name
        self.student_id = student_id
        self.address = address
        self.courses = []  # List to store enrolled courses

    def enroll_in_course(self, course_name):
        """
        Enroll the student in a course.
        :param course_name: The name of the course to enroll in.
        """
        if course_name not in self.courses:
            self.courses.append(course_name)
            print(f"{self.name} has been enrolled in the course {course_name}.")
        else:
            print(f"{self.name} is already enrolled in the course {course_name}.")

    def drop_course(self, course_name):
        """
        Drop a course from the student's list of enrolled courses.
        :param course_name: The name of the course to drop.
        """
        if course_name in self.courses:
            self.courses.remove(course_name)
            print(f"{self.name} has dropped the course {course_name}.")
        else:
            print(f"{self.name} is not enrolled in the course {course_name}.")

    def show_registered_courses(self):
        """
        Display all courses the student is currently enrolled in.
        """
        if self.courses:
            print(f"Courses enrolled by {self.name}:")
            for course in self.courses:
                print(f"- {course}")
        else:
            print(f"{self.name} is not enrolled in any courses.")