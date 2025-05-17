class Student:
    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name
        self.courses = []  # Each course is stored as a tuple: (credits, GPA value)

    def add_course(self, credits, letter_grade):
        gpa_points = self.letter_to_gpa(letter_grade)
        if gpa_points is not None:
            self.courses.append((credits, gpa_points))
        else:
            print(f"Invalid grade '{letter_grade}' entered. Please try again.")

    def letter_to_gpa(self, letter):
        grade_scale = {
            "A": 4.0, "A-": 3.7,
            "B+": 3.3, "B": 3.0, "B-": 2.7,
            "C+": 2.3, "C": 2.0, "C-": 1.7,
            "D+": 1.3, "D": 1.0, "D-": 0.7,
            "F": 0.0
        }
        return grade_scale.get(letter.upper())

    def calculate_gpa(self):
        total_points = 0
        total_credits = 0
        for credits, gpa in self.courses:
            total_points += credits * gpa
            total_credits += credits
        return round(total_points / total_credits, 2) if total_credits > 0 else 0.0

    def get_total_credits(self):
        return sum(credits for credits, _ in self.courses)

    def get_year(self):
        credits = self.get_total_credits()
        if credits < 30:
            return "Freshman"
        elif credits < 60:
            return "Sophomore"
        elif credits < 90:
            return "Junior"
        else:
            return "Senior"


class DeclaredStudent(Student):
    def __init__(self, first_name, last_name, concentration):
        super().__init__(first_name, last_name)
        self.concentration = concentration

    def get_concentration(self):
        return self.concentration


# Prompting the user for personal information
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
concentration = input("Enter your concentration: ")

# Create declared student object
student = DeclaredStudent(first_name, last_name, concentration)

# Prompt user to enter multiple courses
print("\nNow enter your course information:")
while True:
    credits_input = input("Enter course credits (or type -1 to stop): ")
    if credits_input.strip() == "-1":
        break
    try:
        credits = float(credits_input)
        grade = input("Enter the letter grade for the course (e.g., A, B+, C-): ").strip().upper()
        student.add_course(credits, grade)
    except ValueError:
        print("Invalid input. Please enter numeric credits and a valid letter grade.")

# Display student results
print("\nStudent Summary:")
print(f"Name: {first_name} {last_name}")
print(f"Concentration: {student.get_concentration()}")
print(f"Total Credits: {student.get_total_credits()}")
print(f"Cumulative GPA: {student.calculate_gpa()}")
print(f"Student Year: {student.get_year()}")
