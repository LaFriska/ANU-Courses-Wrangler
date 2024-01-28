# courses.xml should be retrieved via the below command:
# curl https://programsandcourses.anu.edu.au/data/CourseSearch/GetCourses?ShowAll=true

import xml.etree.ElementTree as ET

tree = ET.parse('courses.xml')
root = tree.getroot()
items = root[0]

print(len(items))