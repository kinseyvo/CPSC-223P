students = ['male', 'female']
counties = ['Orange County', 'LA County', 'Riverside County']

student_location = [(student, county) for student in students for county in counties]
print(student_location)