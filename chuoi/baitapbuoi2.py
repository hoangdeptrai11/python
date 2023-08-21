#bai1
# n = input("nhap vao ho ten: ")
# n= str.strip(n)
# n = str.title(n)
# n = str.split(n)
# print(" ".join(n))

# bài 2
# dauvao = input("Nhập vào một chuỗi: ")
# inrasokytu = len(dauvao)
# print("Số ký tự trong chuỗi: " ,inrasokytu)
# #tachchuoi
# tach = dauvao.split()
# # in ra so tu
# print("Số từ trong chuỗi là: " , len(tach))
# # in ra moi tu 1 dong
# for i in tach:
#     print(i)
# dauvao = str.title(dauvao)
# print("Chuẩn hóa các ký tự đầu của mỗi từ là chữ hoa: ", dauvao)

#bai 3
# from datetime import datetime
#
# ## Nhập vào ngày sinh theo định dạng dd/mm/yyyy
# nhapvao = input("Nhập vào ngày sinh của bạn (dd/mm/yyyy): ")
# dinhdang = datetime.strptime(nhapvao, "%d/%m/%Y")
#
# ## Tính tuổi
# today = datetime.today()
# age = today.year - dinhdang.year - ((today.month, today.day) < (dinhdang.month, dinhdang.day))
# print("Tuổi của bạn:", age)
#
# ## Tính số ngày đã trôi qua
# songaytroiqua = (today - dinhdang).days
# print("Số ngày đã trôi qua:", songaytroiqua)
#
# ## In ra thời gian hiện tại hệ thống
# thoigian = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
# print("Thời gian hiện tại:", thoigian)

#bai4
#
# numbers = []
# 
# while True:
#     number = float(input("Nhập số thực (nhập 0 để thoát): "))
#     if number == 0:
#         break
#     numbers.append(number)
# 
# print("Dãy số bạn vừa nhập:")
# for num in numbers:
#     print(num, end=" ")


#bai 5
# n = int(input("nhập vào các phần tử: "))
# mang = []
#
# for i in range(n):
#     phantu = int(input("Nhập vào phần tử thứ {i+1}: "))
#     mang.append(i)
# print("Các phần tử chẵn:")
# tongchan = 0
# for i in mang:
#     if i % 2 == 0:
#         print("Các Số Chẵn: ",i)
#         tongchan += i
# print("Tổng các số chẵn: " , tongchan)
#
# print("Các số lẻ: ")
# tongle = 0
# for i in mang:
#     if i % 2 != 0:
#         print("Các số lẻ: ",i)
#         tongle += i
# print("Tổng lẻ: " , tongle)

#bai 7
# sinhvien = [
#     {"mã": "SV001", "tên": "Nguyễn Văn Tuyên", "tuổi": 22, "thành phố": "Hà Nội"},
#     {"mã": "SV002", "tên": "Trần Thị Hải", "tuổi": 19, "thành phố": "Hồ Chí Minh"},
#     {"mã": "SV003", "tên": "Lê Quang Cao", "tuổi": 25, "thành phố": "Hà Nội"},
#     {"mã": "SV004", "tên": "Phạm Thị Đatj", "tuổi": 21, "thành phố": "Đà Nẵng"},
# ]
#
# # In tất cả danh sách sinh viên
# print("Danh sách sinh viên:")
# for i in sinhvien:
#     print(i)
#
# # In ra các sinh viên có tuổi từ 20 trở lên
# print("\nSinh viên có tuổi từ 20 trở lên:")
# for i in sinhvien:
#     if i["tuổi"] >= 20:
#         print(i)
#
# # In ra các sinh viên ở Hà Nội
# print("\nSinh viên ở Hà Nội:")
# for i in sinhvien:
#     if i["thành phố"] == "Hà Nội":
#         print(i)


# bài 8
# def bai8(number):
#     if number <= 1:
#         return False
#     for i in range(2, number):
#         if number % i == 0:
#             return False
#     return True
#
# n = int(input("Nhập n: "))
# print("Các số nguyên tố từ 2 đến", n, "là:")
# for i in range(2, n + 1):
#     if bai8(i):
#         print(i, end=" ")


#bài 9

# nhapvao = float(input("Nhập vào Chiều cao của bạn: "))
# nhapvaocannang = float(input("Nhập vào Cân nặng của bạn: "))
#
# BMI = nhapvaocannang /(nhapvao * nhapvao)
# print("BMI: " , BMI)
# if BMI < 18.5:
#     print("Gầy | Nguy cơ phát bệnh Thấp")
# elif BMI > 18.5 and BMI < 24.9:
#     print("Bình Thường | Nguy cơ phát bệnh Trung Bình")
# elif BMI > 25 and BMI < 29.9:
#     print("Hơi Béo | Nguy cơ phát bệnh Cao")
# elif BMI > 30 and BMI <34.9:
#     print("Béo Phì cấp độ 1 | Nguy cơ phát bệnh Cao")
# elif BMI > 35 and BMI < 39.9:
#     print("Béo Phì cấp độ 2 | Nguy cơ phát bệnh Rất Cao")
# elif BMI > 40:
#     print("Bình Thường | Nguy cơ phát bệnh Nguy Hiểm")

# bai 10

# import hoang
# hoang.main()