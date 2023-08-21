# student_manager.py

students = []


def add_student():
    student_id = input("Nhập mã sinh viên: ")
    student_name = input("Nhập tên sinh viên: ")
    students.append({"id": student_id, "name": student_name})
    print("Thêm sinh viên thành công!")


def remove_student():
    student_id = input("Nhập mã sinh viên của sinh viên muốn xóa: ")
    for student in students:
        if student["id"] == student_id:
            students.remove(student)
            print("Xóa sinh viên thành công!")
            return
    print("Không tìm thấy sinh viên có mã", student_id)


def edit_student():
    student_id = input("Nhập mã sinh viên của sinh viên muốn sửa: ")
    for student in students:
        if student["id"] == student_id:
            new_name = input("Nhập tên mới cho sinh viên: ")
            student["name"] = new_name
            print("Sửa thông tin sinh viên thành công!")
            return
    print("Không tìm thấy sinh viên có mã", student_id)


def view_students():
    print("Danh sách sinh viên:")
    for student in students:
        print("Mã:", student["id"], "- Tên:", student["name"])


def main():
    while True:
        print("\nChọn chức năng:")
        print("1: Thêm sinh viên")
        print("2: Xóa sinh viên")
        print("3: Sửa sinh viên")
        print("4: Xem danh sách sinh viên")
        print("0: Thoát")

        choice = input("Nhập lựa chọn của bạn: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            remove_student()
        elif choice == "3":
            edit_student()
        elif choice == "4":
            view_students()
        elif choice == "0":
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")


if __name__ == "__main__":
    main()
