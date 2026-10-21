

class InvalidMarksError(Exception):
    """Raised when marks are not between 0 and 100."""


class Student:
    
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def passed(self):
        return self.marks >= 50

    def __str__(self):
        return f"{self.name} ({self.marks}): {'Pass' if self.passed() else 'Fail'}"


class Course:

    def __init__(self, name):
        self.name = name
        self.marks = {}

    def add_student(self, student: str, marks: int) -> None:
        
        if not 0 <= marks <= 100:
            raise InvalidMarksError(f"Invalid marks for {student}: {marks}")
        self.marks[student] = marks

    def average(self):
        
        return sum(self.marks.values()) / len(self.marks)

    def top_student(self):
        
        return max(self.marks, key=self.marks.get)

    def __len__(self):
        """Return the number of students."""
        return len(self.marks)

    def __str__(self):
        """Return name, number of students and average."""
        return f"{self.name}: {len(self)} students, average {self.average():.1f}"


def load_course(name: str, filename: str) -> Course:
    """Load students from a file. Bad lines are skipped."""
    course = Course(name)
    try:
        with open(filename) as f:
            for line in f:
                student, mark = line.strip().split(",")
                try:
                    course.add_student(student, int(mark))
                except ValueError:
                    print(f"Skipping {student}: marks is not a number")
                except InvalidMarksError as e:
                    print("Skipping:", e)
    except FileNotFoundError:
        print(f"File not found: {filename}")
    return course


if __name__ == "__main__":
    test = Course("Test")
    test.add_student("Rana", 50)
    print(test)