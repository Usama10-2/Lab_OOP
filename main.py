
from course import Course, InvalidMarksError, Student, load_course

students = [Student("Ali", 72), Student("Sara", 45), Student("Omar", 50)]
for s in students:
    print(s)

c = Course("Programming for AI")
c.add_student("Ali", 88)
c.add_student("Sara", 92)
c.add_student("Omar", 78)
c.add_student("Rana", 89)
c.add_student("Hina", 99)
c.add_student("Ayshea", 85)
print(len(c))
print(c.average())
print(c.top_student())

try:
    c.add_student("Bilal", 120)
except InvalidMarksError as e:
    print("Error:", e)
print(c)

course = load_course("Programming for AI", "marks.txt")
print(course)
print("Top student:", course.top_student())
load_course("AI", "mark.txt")