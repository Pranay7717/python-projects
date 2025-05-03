from abc import ABC, abstractmethod

class Course(ABC): 
    @abstractmethod
    def enroll(self):
        pass  
    def complete(self):
        print("Course completed")  
class PythonCourse(Course):
    def enroll(self):
        print("Enrolled in Python Course")
c = PythonCourse()
c.enroll()
c.complete()
