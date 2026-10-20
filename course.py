


class Course:
    """A course that stores students and their marks."""

    def __init__(self, name):
        self.name = name
        self.marks = {}            # student name -> marks

    def add_student(self, student, marks):
        if not (0 <= marks <= 100):
            raise ValueError(f"Invalid marks: {marks}")
        self.marks[student] = marks
        
    def average(self):
        if not self.marks:
            return 0.0
        return sum(self.marks.values()) / len(self.marks)

    def top_student(self):
        return max(self.marks, key=self.marks.get)
        
    def __len__(self):
        return len(self.marks)
