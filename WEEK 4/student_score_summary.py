num_of_students=int(input("How many students?"))
while num_of_students <=0:
    print("Invalid Number of Students.")
    num_of_students=int(input("How many students?"))



total_score=0 
passed_count=0
failed_count=0


for student in range(1,num_of_students+1):
    student_score=float(input(f"Enter student {student} score:"))

    while student_score <0 or student_score >100:
        print("Invalid score")
        student_score=float(input(f"Enter student {student} score:"))

    total_score+=student_score

    if student_score>=50:
        passed_count+=1
    else:
        failed_count+=1

average_score=total_score/num_of_students




print(f"Total number of students: {num_of_students}")
print(f"Total score: {total_score}")
print(f"Average score: {average_score:.2f}")
print(f"Number of students who passed: {passed_count}")
print(f"Number of students who failed: {failed_count}")


