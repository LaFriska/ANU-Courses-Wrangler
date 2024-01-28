# courses.xml should be retrieved via the below command:
# curl https://programsandcourses.anu.edu.au/data/CourseSearch/GetCourses?ShowAll=true

import xml.etree.ElementTree as ET

tree = ET.parse('courses.xml')
root = tree.getroot()
items = root[0]


def getSpecificCourses(courseType, careerFilter):
    res = []
    for child in items:
        if child[1].text.startswith(courseType) & ((careerFilter is None) | (child[0].text == careerFilter)):
            res.append(child)
    return res


compCourses = getSpecificCourses("MATH", None)

for course in compCourses:
    print(course[3].text)
