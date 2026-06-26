#Nested Dictionary Comprehension 
patients = ["P101", "P102", "P103"]

records = {
    patient: {
        "Heart Rate": 70 + len(patient),
        "Temperature": 98.6,
        "Status": "Stable"
    }
    for patient in patients
}

print(records)  