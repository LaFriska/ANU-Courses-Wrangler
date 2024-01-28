class Course:
    def __init__(self, courseCode, career, title, semesters, units, requirements, incompatible, specialRequirements):
        self.courseCode = courseCode
        self.career = career
        self.title = title
        self.semesters = semesters
        self.units = units
        self.requirements = requirements
        self.incompatible = incompatible
        self.specialRequirements = specialRequirements


class Courses:
    def __init__(self):
        self.courseArray = []

    def append(self, course):
        self.courseArray.append(course)
