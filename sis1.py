from datetime import datetime

# Student Class
class Student:
    def __init__(self, student_id, first_name, last_name, dob, email, phone):
        self.student_id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.email = email
        self.phone = phone
        self.courses = []
        self.payments = []
    
    def enroll_in_course(self, course):
        self.courses.append(course)
    
    def update_student_info(self, first_name, last_name, dob, email, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.email = email
        self.phone = phone
    
    def make_payment(self, amount, payment_date):
        payment = Payment(len(self.payments) + 1, self.student_id, amount, payment_date)
        self.payments.append(payment)
    
    def display_student_info(self):
        print(f"ID: {self.student_id}, Name: {self.first_name} {self.last_name}, DOB: {self.dob}, Email: {self.email}, Phone: {self.phone}")
    
    def get_enrolled_courses(self):
        return self.courses
    
    def get_payment_history(self):
        return self.payments

# Course Class
class Course:
    def __init__(self, course_id, course_name, course_code, instructor_name):
        self.course_id = course_id
        self.course_name = course_name
        self.course_code = course_code
        self.instructor_name = instructor_name
        self.enrollments = []
    
    def assign_teacher(self, teacher):
        self.instructor_name = teacher.first_name + " " + teacher.last_name
    
    def update_course_info(self, course_code, course_name, instructor):
        self.course_code = course_code
        self.course_name = course_name
        self.instructor_name = instructor
    
    def display_course_info(self):
        print(f"ID: {self.course_id}, Name: {self.course_name}, Code: {self.course_code}, Instructor: {self.instructor_name}")
    
    def get_enrollments(self):
        return self.enrollments

# Enrollment Class
class Enrollment:
    def __init__(self, enrollment_id, student, course, enrollment_date):
        self.enrollment_id = enrollment_id
        self.student = student
        self.course = course
        self.enrollment_date = enrollment_date
    
    def get_student(self):
        return self.student
    
    def get_course(self):
        return self.course

# Teacher Class
class Teacher:
    def __init__(self, teacher_id, first_name, last_name, email):
        self.teacher_id = teacher_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.courses = []
    
    def update_teacher_info(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
    
    def display_teacher_info(self):
        print(f"ID: {self.teacher_id}, Name: {self.first_name} {self.last_name}, Email: {self.email}")
    
    def get_assigned_courses(self):
        return self.courses

# Payment Class
class Payment:
    def __init__(self, payment_id, student_id, amount, payment_date):
        self.payment_id = payment_id
        self.student_id = student_id
        self.amount = amount
        self.payment_date = payment_date
    
    def get_student(self):
        return self.student_id
    
    def get_payment_amount(self):
        return self.amount
    
    def get_payment_date(self):
        return self.payment_date
