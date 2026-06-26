def result_generator(students):
    for name, marks in students.items():

        if marks >= 90:
            result = "Distinction"
        elif marks >= 75:
            result = "First Class"
        else:
            result = "Pass"

        yield f"{name} - {result}"

students = {
    "Rithika": 95,
    "Arjun": 82,
    "Neha": 70
}

for student in result_generator(students):
    print(student) 