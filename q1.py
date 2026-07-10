def student_required(Rollno, name):
    print("Roll no:", Rollno)
    print("name:", name)

student_required(1, "sanika")


def student_keyword(Rollno, name):
    print("name:", name)
    print("Roll no:", Rollno)
student_keyword(name="pqr", Rollno=10)


def student_default(Rollno, name, Class="sy4"):
    print("Rollno:", Rollno)
    print("name:", name)
    print("Class:", Class)
student_default(1, "sanika")
student_default(2, "ABC", "sy5")


def student_length(*sub):
    print("*sub:", *sub)
student_length("Python")
student_length("Python", "C", "C++")
    