period = int(input())
reviewed = 0
unreviewed = 0
days = 1
doctors = 7
total_patients = 0
for day in range(period):
    if days % 3 == 0:
        if reviewed < unreviewed:
            doctors += 1
    patients = int(input())
    days += 1
    if patients <= doctors:
        reviewed += patients
    else:
        reviewed += doctors
        unreviewed += patients - doctors
total_patients = reviewed + unreviewed
print(f"Treated patients: {reviewed}.")
print(f"Untreated patients: {unreviewed}.")
