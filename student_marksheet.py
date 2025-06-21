
marksheet = {'Alice':85, 'ojasvi':99, 'jack':100, 'max': 98}
student_name = input('Enter the students name : ')
if student_name in marksheet:
    print(f"{student_name} marks : {marksheet.get(student_name)}")
else:
    print("student not found")


