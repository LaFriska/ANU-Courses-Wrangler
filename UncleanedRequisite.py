class UncleanedRequisite:

    def __init__(self, courseCode, requisites):
        self.courseCode = courseCode
        self.requirements = requisites


class UncleanedRequisiteRecords:

    def __init__(self):
        self.uncleanedRequisites = []

    def append(self, record):
        self.uncleanedRequisites.append(record)
