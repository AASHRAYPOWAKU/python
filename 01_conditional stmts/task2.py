Student_id=int(input("Enter Student id:"))
Student_Name=input("Enter Student Name:")
Student_attendance=float(input("Enter attendance:"))
n=int(input("Enter no of subjects:"))
i=1
total=0
while i<=n:
    user_input=int(input(f"Enter Score for subject {i}:"))
    total+=user_input
    total_score=total/3
    user_input2=input("Do you want to enter another score:")
    if user_input2=="yes":
        pass
    else:
        break
    i+=1
print(f"Student id:{Student_id}")
print(f"Student name:{Student_Name}")
print(f"Student attendance:{Student_attendance}")
print(f"Total Score:{total_score}")
print(f"Total number of subjects:{n}")
print(f"Average score:{total/3}")
if total_score>90:
    print("Excellent")
elif total_score>70 and total_score<90:
    print("Well done")
else:
    print("Better luck next time")
if Student_attendance<=75:
    print("Warning!!Low Attendance")







