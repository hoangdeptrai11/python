# # bài 1
# n = int(input("Nhập số Kẹo: "))
# m = int(input("Nhập vào số em Bé: "))
#
# if n % m == 0:
#     print("Yes")
# else:
#     print("No")

# bai 2
# n = int(input("Nhập vào thứ: "))
# if n ==2:
#     print("Thứ 2: Môn Toán")
# elif n == 3:
#     print("Thứ 3: Môn Tin")
# elif n == 4:
#     print("Thứ 4: Môn Văn")
# elif n == 5:
#     print("Thứ 5: Môn Khoa Học")
# elif n == 6:
#     print("Thứ 6: Môn Tự Nhiên")
# elif n == 7:
#     print("Thứ 7: Môn Sử")
# else:
#     print("Không có Thứ: ",n, "trong Tuần")

# Bài 3
#
# n = int(input("Nhập vào số (KWH): "))
# gia1 = 1678
# gia2 = 1734
# gia3 = 2014
# gia4 = 2536
# gia5 = 2834
# gia6 = 2927
#
# if n <0:
#     print("Vui Lòng Nhập Lại Số")
# elif n <= 50:
#     tiendien = n*gia1
#     print(n, " KWH","có giá: ",tiendien )
# elif n <=100:
#     tiendien = 50*gia1 +((n-50)*gia2)
# elif n <=200:
#     tiendien= 50*gia1 +(50*gia2) + ((n -100 )*gia3)
#     print(n, " KWH","có giá: ",tiendien )
# elif n <= 300:
#     tiendien= 50* gia1 +(50*gia2) +(100*gia3)+ ((n -200)*gia4)
#     print(n, " KWH","có giá: ",tiendien )
# elif n <=400:
#     tiendien = 50* gia1 +(50*gia2)+(100*gia3) +(100*gia4)+((n - 300)*gia5)
#     print(n, " KWH","có giá: ",tiendien )
# else:
#     tiendien= 50*gia1 +(50*gia2) + (100*gia3)+(100*gia4)+(100*gia5)+((n - 400)*gia6)
#     print(n, " KWH","có giá: ",tiendien )



# bai 4

# a
# n = int(input("Nhập Số Nguyên Dương N: "))
# s = 2022 + sum([2 * i for i in range(1, n+1)])
# print("Tổng của S là: ",s)

# b
# import math
# n = int(input("Nhap n: "))
# s = 0
# for i in range(1,n+1):
#     factorial_i = math.factorial(i)
#     s += 1 / factorial_i
# print(f"tong ",n, " la:",s)

# c
# n = int(input("nhap vào x: "))
# m = int(input("nhap vao y: "))
# if n>m:
#     tong = n**2
#     print("x^2= ", tong)
# elif n == m:
#     tong = n + m
#     print("x=y la: ", tong)
# elif n < m :
#     tong = m**2
#     print("y^2 = " , tong )





#  bài 5

# while True:
#     n = int(input("bạn cần xem bảng cửu chương bao nhiêu: "))
#
#
#     if n > 0 and n < 9:
#         for i in range(1, 11):
#             print(n, 'x', i, '=', n * i)
#     else:
#         print("nhập lại")
#     a = int(input("bạn có muốn tiếp tục không? (1 là Yes || 0 là No) "))
#     if a == 1: continue
#     else: break


# bai 6

# while True:
#     virus = int(input("Nhập vào số lượng virus: "))
#     cach = 2
#     tong = 1000000000
#     days = 0
#     while virus < tong:
#         virus *= cach
#         days +=1
#         print(f"so ngay can de so luong virus len 1 tỷ là {days} ngay")
#     a = int(input("bạn có muốn tiếp tục không? (1 là Yes || 0 là No) "))
#     if a == 1: continue
#     else: break


# bài 7
#
# n = int(input("nhâp vào số nguyên dương: "))
#
# if n <= 1:
#     print("NO")
# else:
#     duong = True
# for i in range(2, int(n ** 0.5) +1):
#     if n % i == 0:
#         duong =False
#     break
# if duong:
#         print("YES")
# else:
#         print("NO")

# bài 8

# year = int(input("Nhập một Năm để Kiểm tra: "))
# if year % 400 == 0 or (year % 4 == 0 and year %100 != 0):
#     print(f"Năm{year} là năm Nhuận.")
#     days = 366
# else:
#     print(f"năm {year } Không phải là năm nhuận")
#     days = 365
#
#     print(f"so ngày trong Năm {year} là {days} ngày")

# bài 9
#
# def is_leap_year(year):
#     return (year % 400 == 0) or (year % 4 == 0 and year %100 != 0)
#
# def days_in_month(month ,year):
#     if month in [1,3,5,7,8,10,12]:
#         return 31
#     elif month == 2:
#         if is_leap_year((year)):
#             return 29
#         else:
#             return 28
#     else:
#         return 30
# month = int(input("Nhập vào Tháng: "))
# year = int(input("nhap vao năm: "))
#
# days = days_in_month(month, year)
# print(f"số ngày trong tháng {month} năm {year} la {days} ngày")

# bài 10

# nhapvaoten = input("Nhập Họ và Tên: ")
# nhapsotientrongtk = int(input("Nhâpj Số Tiền: "))
# print("Chào: " ,nhapvaoten)
# print("Số Dư Hiện Tại là: ", nhapsotientrongtk)
# print("Bạn Muốn Rút (500000 thì nhập số 1) , (200000 thì nhập số 2), (100000 thì nhập số 3) (50000 thì nhập số 4)")
# while True:
#     sotiencanrut = int(input("số: "))
#     if sotiencanrut == 1:
#         if nhapsotientrongtk > sotiencanrut:
#             trutien = nhapsotientrongtk - 500000
#             print(nhapvaoten, "đã rút", 500000, "số Tiền Còn Lại trong tài khoản là:", trutien)
#
#         else:
#             print("Tài Khoản không đủ Tiền")
#
#     elif sotiencanrut ==2:
#         if nhapsotientrongtk > sotiencanrut:
#             trutien = nhapsotientrongtk - 200000
#             print(nhapvaoten, "đã rút", 200000, "số Tiền Còn Lại trong tài khoản là:", trutien)
#         else:
#             print("Tài Khoản không đủ Tiền")
#     elif sotiencanrut ==3:
#         if nhapsotientrongtk > sotiencanrut:
#             trutien = nhapsotientrongtk - 100000
#             print(nhapvaoten, "đã rút", 100000, "số Tiền Còn Lại trong tài khoản là:", trutien)
#         else:
#             print("Tài Khoản không đủ Tiền")
#     elif sotiencanrut ==2:
#         if nhapsotientrongtk > sotiencanrut:
#             trutien = nhapsotientrongtk - 50000
#             print(nhapvaoten, "đã rút", 50000, "số Tiền Còn Lại trong tài khoản là:", trutien)
#         else:
#             print("Tài Khoản không đủ Tiền")
#     a = int(input("bạn có muốn tiếp tục không? (1 là Yes || 0 là No) "))
#     if a == 1: continue
#     else: break



