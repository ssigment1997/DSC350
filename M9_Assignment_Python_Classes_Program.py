class Student:
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName
        self.grade_points = 0.0  # Cumulative grade points
        self.credits = 0.0  # Total number of credits
        self.gpa = 0.0  # Cumulative GPA

    def calculateGpa(self, grade, credit):
        # Add the grade points for this course
        self.grade_points += grade * credit
        # Add the credits for this course
        self.credits += credit

    def getGpa(self):
        # Return the cumulative GPA, capped at 4.0
        if self.credits > 0:
            self.gpa = self.grade_points / self.credits
            if self.gpa > 4.0:  # Cap GPA at 4.0
                self.gpa = 4.0
        else:
            self.gpa = 0.0
        return self.gpa


# Main program
def main():
    # Prompt for student name
    firstName = input("Enter your first name: ")
    lastName = input("Enter your last name: ")

    # Create Student object
    student = Student(firstName, lastName)

    # Course input loop
    while True:
        try:
            credit = float(input("Enter number of credits for the course: "))
        except ValueError:
            print("Invalid credit value. Please enter a number.")
            continue

        grade_input = input("Enter grade for the course: ")
        try:
            grade = float(grade_input)
        except ValueError:
            print("Invalid grade. Please enter a numeric grade.")
            continue

        # Update student's GPA
        student.calculateGpa(grade, credit)

        # Ask if user wants to continue or finish
        final = input('To finish, type "done" or press Enter to continue: ').lower()
        if final == 'done':
            break

    # Final GPA calculation and output
    final_gpa = student.getGpa()
    full_name = f"{student.firstName} {student.lastName}"
    print(f"\n{full_name} has a cumulative GPA of: {final_gpa:.2f}")


# Run the program
main()
