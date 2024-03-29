#  https://programsandcourses.anu.edu.au/data/CourseSearch/GetCourses?ShowAll=true

import xml.etree.ElementTree as ET
import requests
from bs4 import BeautifulSoup
from Course import Course
from Course import Courses
from UncleanedRequisite import UncleanedRequisiteRecords
from UncleanedRequisite import UncleanedRequisite
import json

tree = ET.parse('courses.xml')
root = tree.getroot()
items = root[0]

def getSpecificCourses(subjectCodes, careerFilter):  # Deserialises XML and retrieves objects with specific course type
    res = []
    for child in items:
        if compare(child[1].text, subjectCodes) & ((careerFilter is None) | (child[0].text == careerFilter)):
            res.append(child)
    return res


def compare(text, subjectCodes):
    for code in subjectCodes:
        if text.startswith(code): return True
    return False


# This function isn't actually used, but I kept it here incase it is needed in the future
def fetchRequisites(courseCode):
    print(courseCode)
    response = requests.get(f"https://programsandcourses.anu.edu.au/2024/course/{courseCode}")
    soup = BeautifulSoup(response.text, "html.parser")
    program_requirements = soup.find("div", {"class": "requisite"})
    if program_requirements is None:
        err = "ERROR: CANNOT FETCH FOR " + courseCode
        print(err)
        return err
    return program_requirements.get_text(strip=True, separator="\n")


def serialiseUncleanedRequisites(records):
    res = UncleanedRequisiteRecords()
    for record in records:
        res.append(UncleanedRequisite(courseCode=record[1].text ,requisites=fetchRequisites(record[1].text)))
    return json.dumps(res, default=lambda o: o.__dict__, indent=4)


def serialiseToJSONTemplate(records):
    courses = Courses()
    for record in records:
        if record[4].text is None:
            semesters = []
        else:
            semesters = record[4].text.split("/")

        course = Course(courseCode=record[1].text,
                        career=record[0].text,
                        title=record[3].text,
                        semesters=semesters,
                        units=int(record[5].text),
                        requirements=[],
                        incompatible=[],
                        specialRequirements="")
        courses.append(course)
    return json.dumps(courses, default=lambda o: o.__dict__, indent=4)


courses = getSpecificCourses(["COMP", "MATH"], None)
print(serialiseToJSONTemplate(courses))
print(serialiseUncleanedRequisites(courses))
