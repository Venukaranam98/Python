class Students:

    def __init__(self, name, marks):

        self.name = name
        self.marks = marks

    def calculate_grade(self):

        if self.marks >= 90:
            return "A Grade"

        elif self.marks >= 75:
            return "B Grade"

        elif self.marks >= 50:
            return "C Grade"

        elif self.marks >= 35:
            return "D Grade"

        else:
            return "Fail"

    def display(self):

        grade = self.calculate_grade()

        print("\n--- STUDENT REPORT ---")
        print("Name :", self.name)
        print("Marks:", self.marks)
        print("Grade:", grade)

s1 = Students("Venu", 85)

s1.display()