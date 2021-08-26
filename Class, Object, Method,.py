class student :
    roll = ""
    gpa = ""

    def set(self, roll, gpa) :
        self.roll = roll
        self.gpa = gpa

    def display(self) :
        print(f"Roll: {self.roll}, GPA: {self.gpa}")

rahim = student()
rahim.set(101,3.75)
rahim.display()