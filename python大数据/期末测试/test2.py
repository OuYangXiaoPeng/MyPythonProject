id_student = [2021001, 2021002, 2021003, 2021004, 2021005, 2021006, 2021007, 2021008]
name = ["Allen", "Olivia", "Christine", "Emma", "Mike", "Alice", "Tony", "Make"]

student_dict = dict(zip(id_student, name))
# print("学生字典:", student_dict)
def find(sid):
    if sid in student_dict:
        print(f"学生姓名: {student_dict[sid]}")
    else:
        print("无此学号存在!")
find(2021004)
find(2021999)
