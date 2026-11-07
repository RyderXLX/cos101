number_of_students=int(input("Enter number of student:"))
while number_of_students <1:
    print("Invalid number of students")
    number_of_students=int(input("Enter number of student"))

passed_count=0
failed_count=0


for student in range(1,number_of_students+1):
    score=float(input(f"Enter score for student {student}:"))

    if score>=50:
        passed_count+=1
    else:
        failed_count+=1


print(f"Total students: {number_of_students}")
print(f"Passed: {passed_count}")
print(f"Failed: {failed_count}")
