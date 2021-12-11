import sys
import tkinter as tk
from time import strftime
from tkinter import *
from tkinter import BOTH, END, Frame, Tk

import numpy as np
import pandas as pd
from PIL import Image, ImageTk
pd.set_option('display.max_rows', None)


class formMoFile(tk.Toplevel):
    def __init__(self, parent):
        tk.Toplevel.__init__(self, parent)
        self.title("Mở file")
        self.geometry("650x550")
        self.iconbitmap("image/icons8-align-text-left-48.ico")
        self.configure(bg='#8ddbff')
        self.resizable(False, False)

        def open_DS():
            my_text.delete('1.0', END)
            text_file = open("DanhSach.txt", 'r')
            stuff = text_file.read()
            my_text.insert(END, stuff)
            text_file.close()

        def open_CTDT():
            my_text.delete('1.0', END)
            text_file = open("ChiTietDT.txt", 'r')
            stuff = text_file.read()
            my_text.insert(END, stuff)
            text_file.close()

        def open_DT():
            my_text.delete('1.0', END)
            text_file = open("DiemThi.txt", 'r')
            stuff = text_file.read()
            my_text.insert(END, stuff)
            text_file.close()

        def clear_text():
            my_text.delete('1.0', END)

        my_text = Text(self, width=70, height=30)
        my_text.pack()

        openNV_btn = Button(self, text="DanhSach.txt", activebackground="#42a5f5", width=12, height=1, command=open_DS)
        openNV_btn.place(x=40, y=500)
        openCT_btn = Button(self, text="ChiTietDT.txt", activebackground="#42a5f5", width=12, height=1, command=open_CTDT)
        openCT_btn.place(x=160, y=500)
        openCV_btn = Button(self, text="DiemThi.txt", activebackground="#42a5f5", width=12, height=1, command=open_DT)
        openCV_btn.place(x=280, y=500)
        openPB_btn = Button(self, text="Clear", activebackground="#42a5f5", width=12, height=1, command=clear_text)
        openPB_btn.place(x=390, y=500)

List_SinhVien = [(1, 'Nguyen Viet', 'Hong', 0, '04/04/1981', 3),
                 (2, 'Nguyen Hong', 'Lanh', 1, '15/03/1982', 1),
                 (3, 'Nguyen Minh', 'Quang', 0, '10/07/1982', 3),
                 (4, 'Dinh Thi', 'Tam', 1, '18/02/1982', 1),
                 (5, 'Nguyen Hoai', 'Anh', 1, '21/08/1982', 3),
                 (6, 'Dang Bich', 'Thuy', 1, '22/10/1982', 1),
                 (7, 'Hoang Thanh', 'Trang', 1, '12/08/1982', 3),
                 (8, 'Tran Cat', 'Dung', 1, '04/12/1981', 3),
                 (9, 'Pham Hoai', 'Bong', 0, '11/10/1980', 3),
                 (10, 'Tran Minh', 'Nguyet', 1, '07/12/1981', 1),
                 (11, 'Ma Thi Hong', 'Xuan', 1, '19/10/1981', 3),
                 (12, 'Le Thao', 'Dung', 1, '03/11/1982', 1),
                 (13, 'Luu Phuong', 'Thanh', 1, '25/02/1982', 1),
                 (14, 'Phan', 'Thanh', 0, '03/07/1981', 1),
                 (15, 'Pham Thu', 'Thuy', 1, '04/12/1981', 1),
                 (16, 'Dang Dinh', 'Tam', 0, '24/11/1981', 1),
                 (17, 'Tong Duc', 'Cuong', 0, '25/06/1982', 1),
                 (18, 'Tran Thu', 'Nga', 1, '14/09/1981', 1),
                 (19, 'Tran Thi Thanh', 'Giang', 1, '18/03/1982', 1),
                 (20, 'Truong Thi', 'My', 1, '16/08/1982', 1),
                 (21, 'Nguyen Thi', 'Hoa', 1, '27/11/1982', 1),
                 (22, 'Ha Son', 'Tri', 0, '27/08/1981', 1),
                 (23, 'Tang My', 'Hanh', 1, '28/10/1980', 1),
                 (24, 'Tran Thi', 'Tam', 1, '22/02/1982', 1),
                 (25, 'Pham Thi', 'Lua', 1, '24/07/1981', 1),
                 (26, 'Huynh Bach', 'Cuc', 1, '21/09/1980', 2),
                 (27, 'Nguyen Thi', 'Tuyet', 1, '20/12/1981', 1),
                 (28, 'Vu Thi', 'No', 1, '02/04/1982', 1),
                 (29, 'Tran My', 'Dung', 1, '12/01/1982', 2),
                 (30, 'Truong Minh', 'Thang', 0, '26/02/1982', 2),
                 (31, 'Le Kim', 'Thoa', 1, '01/04/1982', 1),
                 (32, 'Huynh Thanh', 'Nga', 1, '07/12/1980', 2),
                 (33, 'Tran Thi', 'Loan', 1, '25/11/1981', 1),
                 (34, 'Tran Thi', 'Nhi', 1, '18/11/1982', 1),
                 (35, 'Lam Ngoc', 'Quan', 0, '28/08/1981', 2),
                 (36, 'Nguyen Ngoc', 'Bich', 1, '26/08/1981', 1),
                 (37, 'Vuong Kim', 'Anh', 1, '18/04/1982', 2),
                 (38, 'Nguyen Thu', 'Van', 1, '16/09/1982', 1),
                 (39, 'Phan Mai', 'Phuong', 1, '11/07/1981', 1),
                 (40, 'Pham Thi', 'Thu', 1, '26/01/1982', 2),
                 (41, 'Nguyen Thi', 'Dung', 1, '25/11/1982', 1),
                 (42, 'Doan Thuy', 'Trang', 1, '19/11/1982', 2),
                 (43, 'Hoang Van', 'Hoa', 0, '10/01/1982', 2),
                 (44, 'Nguyen Van', 'Tien', 1, '07/10/1981', 1),
                 (45, 'Du Thi Lieu', 'Dung', 0, '17/06/1982', 2),
                 (46, 'Vu Kieu', 'Oanh', 1, '09/03/1982', 2),
                 (47, 'Nguyen Trong', 'Nghiep', 0, '20/07/1981', 2),
                 (48, 'Nguyen Thuy', 'Huong', 1, '14/12/1981', 1),
                 (49, 'Bui Van', 'Hung', 0, '25/08/1981', 1),
                 (50, 'Ly Cong', 'Duy', 0, '14/02/1982', 2),
                 (51,         'Le Thi',         'Ly',     1, '28/05/1981', 2),
                 (52,         'Nguyen Lien',    'Phuong', 1, '17/09/1982', 1),
                 (53,         'Hoang Thi',      'Thuan',  1, '25/10/1981', 2),
                 (54,         'To Phuong',      'Lan',    1, '10/10/1982', 1),
                 (55,         'Tran Thi',       'Phuong', 1, '10/04/1981', 2),
                 (56,         'Nguyen Dong',    'Lan',    1, '29/07/1982', 2),
                 (57,         'Nguyen Van',     'Toan',   0, '09/06/1982', 1),
                 (58,         'Diep Thuy',      'Phuong', 1, '13/12/1981', 2),
                 (59,         'Dao Thi',        'Tue',    1, '23/12/1982', 1),
                 (60,         'Tran Thi',       'Phan',   1, '24/01/1982', 2),
                 (61,         'Tran Thi',       'Thuy',   1, '08/11/1982', 3),
                 (62,         'Nguyen Mong',    'Kieu',   1, '23/08/1982', 2),
                 (63,         'Duong Thi',      'Tuoi',   1, '24/12/1981', 3),
                 (64,         'Nguyen Thi',     'Thuy',   1, '05/01/1982', 2),
                 (65,         'Nguyen Thi',    'Le',     1, '21/06/1982', 3),
                 (66,        'Nguyen Thi',     'Hanh',   1, '19/01/1981', 3),
                 (67,         'Nguyen Van',     'Tam',    0, '02/07/1982', 3),
                 (68,        'Lam Ngoc',       'Phuoc',  0, '17/02/1981', 1),
                 (69,         'Phan Kim',       'Nga',    1, '24/08/1982', 3),
                 (70,         'Huynh Thi',      'Huong',  1, '19/05/1981', 1),
                 (71,         'Nguyen Thu',     'Ha',     1, '03/04/1982', 1),
                 (72,        'Nguyen Van',     'Dung',   0, '17/12/1981', 3),
                 (73,         'Tran Tham',      'Tuoi',   1, '04/02/1982', 1),
                 (74,         'Duong Cong',     'Bang',  0, '27/06/1981', 1 ),
                 (75,         'Le Trung',       'Kien',   0, '09/02/1982', 1),
                 (76,         'Nguyen Van',     'Nghiep', 0, '14/09/1982', 1),
                 (77,         'Nguyen Van',     'Minh',   0, '07/02/1981', 1),
                 (78,         'Ho Duong',       'Thanh',  0, '09/11/1981', 1),
                 (79,         'Quach Kieu',     'Mai',    1, '17/02/1982', 1),
                 (80,         'Dao Thi',        'Phuong', 1, '29/03/1982', 1),
                 (81,         'Tran Thi Ngoc',  'Han',    1, '26/07/1982', 3),
                 (82,         'Tran Tuyet',     'Anh',    1, '12/06/1982', 2),
                 (83,         'Nguyen Cam',     'Huong',  1, '02/03/1981', 3),
                 (84,         'Nguyen Ngoc',    'Suong',  1, '11/09/1981', 3),
                 (85,        'Nguyen Van',     'Loi',    0, '02/02/1982', 1),
                 (86,         'Nguyen Duc',     'Thang',  0, '24/05/1981', 1),
                 (87,         'Bui Thi',        'Hue',    1, '19/12/1981', 1),
                 (88,         'Pham Thi',       'Mai',    1, '22/08/1981', 1),
                 (89,         'Nguyen Thi',     'Huong',  1, '30/11/1981', 1),
                 (90,         'Pham Van',       'Trang',  0, '06/05/1981', 1),
                 (91,         'Tran Thuy',      'Tien',   1, '27/11/1980', 2),
                 (92,         'Nguyen Minh',    'Dan',    0, '11/12/1982', 3),
                 (93,         'Do Thi',         'Thao',   1, '18/10/1980', 2),
                 (94,         'Phan Thi',       'Anh',    1, '13/07/1981', 3),
                 (95,         'Dang Kim',       'Anh',    1, '18/10/1981', 2),
                 (96,         'Le Tien',        'Dat',    0, '01/12/1982', 3),
                 (97,        'Pham Hong',     'Tuyet',  1, '05/10/1981', 2),
                 (98,         'Pham Thi',       'Chien',  1, '29/10/1981', 3),
                 (99,         'Nguyen Thi',     'Binh',   1, '09/12/1982', 2),
                 (100,        'Tran Van',       'Viet',   0, '15/07/1982', 2),
                 (101,        'Nguyen Bui',     'Hoa',    0, '18/02/1981', 3),
                 (102,        'Ho Cam',        'Ly',     1, '30/08/1982', 2),
                 (103,        'Huynh Van',      'Khoa',   0, '17/04/1981', 3),
                 (104,        'Huynh Minh',     'Hieu',   1, '18/04/1982', 2),
                 (105,        'Huynh Thanh',    'Viet',   0, '02/02/1981', 3),
                 (106,        'Le Hong',        'Nhung',  1, '01/12/1981', 2),
                 (107,        'Nguyen Thi',     'Van',    1, '22/02/1982', 3),
                 (108,        'Tran Van',       'Quang',  0, '24/09/1981', 2),
                 (109,        'Dang Minh',      'Quan',   0, '17/02/1982', 1),
                 (110,        'Le Thanh',       'Khoa',   0, '28/07/1981', 2),
                 (111,        'Nguyen Tan',     'Tai',    0, '22/08/1981', 2),
                 (112,        'Do Thi',         'Thuy',   1, '17/08/1982', 2),
                 (113,        'Vu Van',         'An',     0, '31/01/1982', 2),
                 (114,       'Nguyen Van',    'Thanh',  0, '13/11/1981',1),
                 (115,        'Bui Van',        'Thanh',  0, '12/08/1982', 2),
                 (116,       'Do Phuong',      'Nam',    0, '01/01/1982', 1),
                 (117,        'Truong Kieu',    'Oanh',   1, '14/09/1982', 2),
                 (118,        'Tran My',        'Thanh',  1, '07/10/1981', 1),
                 (119,        'Pham Van',       'Hoang',  0, '27/10/1982', 1),
                 (120,        'Nguyen Thi',     'Nhung',  1, '31/10/1981', 2),
                 (121,        'Nguyen Thi',    'Lan',    1, '12/11/1980', 2),
                 (122,        'Nguyen Hong',    'Hoa',    1, '14/12/1981', 1),
                 (123,        'Tran Van',       'Phuong', 0, '16/10/1982', 2),
                 (124,        'Tran Van',       'Minh',   0, '11/07/1982', 1),
                 (125,        'Vo Quoc',        'Vuong',  0, '29/09/1982', 2),
                 (126,        'Nguyen Thanh',   'Trung',  0, '07/12/1982', 1),
                 (127,        'Nguyen Thi',     'Thao',   1, '30/01/1981', 1),
                 (128,        'Vo Kim',         'Yen',    1, '16/12/1981', 2),
                 (129,        'Tran Van',       'Son',    0, '20/07/1981', 2),
                 (130,        'Nguyen Van',     'Hai',    0, '09/05/1981', 2),
                 (131,        'Nguyen Thanh',   'Lam',    0, '24/03/1982', 1),
                 (132,        'Pham Lan',       'Anh',    1, '06/10/1981', 2),
                 (133,        'Nguyen Van',     'Doan',   0, '15/10/1981', 1),
                 (134,        'Le Hong',        'Hoa',    1, '16/12/1981', 2),
                 (135,        'Nguyen Van',     'Ngan',   0, '06/08/1981', 1),
                 (136,        'Pham Hong',      'Chung',  0, '19/05/1981', 2),
                 (137,        'Nguyen Hong',    'Hoa',    1, '06/09/1981', 1),
                 (138,        'Le Hong',        'Hanh',   1, '16/12/1981', 1),
                 (139,        'Le Anh',         'Thu',    1, '31/01/1981', 1),
                 (140,        'Tran Le',        'Nga',    1, '27/11/1980', 1),
                 (141,        'Nguyen Thi',     'Huong',  1, '04/04/1981', 3),
                 (142,        'Vuong Cong',     'Hon',    0, '18/09/1981', 3),
                 (143,        'Ta Ngoc',        'Dieu',   0, '14/08/1981', 3),
                 (144,        'Nguyen Duc',     'Hien',   0, '19/04/1982', 3),
                 (145,        'Nguyen Thanh',   'Hai',    0, '07/12/1981', 1),
                 (146,        'Dao Thanh',      'Xuan',   0, '30/12/1980', 2),
                 (147,        'Mai Ngoc',       'Bich',   1, '08/10/1981', 1),
                 (148,        'Pham Thu',       'Han',    1, '04/12/1982', 2),
                 (149,        'Phan Huy',       'Hung',   0, '03/02/1981', 1),
                 (150,        'Nguyen Phuoc',   'Lam',   0, '05/11/1980', 2),
                 (151,        'Dao Minh',       'Than',   0, '21/04/1982', 1),
                 (152,        'Le Van',         'Dung',   0, '03/12/1981', 2),
                 (153,        'Tran Viet',      'Hong',   0, '07/04/1982', 1),
                 (154,        'Nguyen Thanh',   'Hao',    0, '20/07/1982', 2),
                 (155,        'Nguyen Kim',     'Loan',   1, '19/02/1981', 1),
                 (156,        'Nguyen Cong',    'Truong', 0, '11/08/1982', 1)]

DF_SinhVien = pd.DataFrame.from_records(List_SinhVien, columns=['SBD', 'Ho', 'Ten', 'Phai', 'NgaySinh', 'DTDT'])
f = open("sinhvien/SinhVien_data.txt", "w")
print(DF_SinhVien, file=f)
f.close()

# <--------------Giao diện sinh viên-------------->
class formSinhVien(tk.Toplevel):
    def __init__(self, parent):
        tk.Toplevel.__init__(self, parent)
        self.title("Sinh viên")
        self.geometry("1110x500")
        self.iconbitmap("image/icons8-employee-48_1.ico")
        self.configure(bg='#8ddbff')
        self.resizable(False,False)

        def clock():
            string = strftime('%I:%M:%S:%p')
            lb_clock.config(text=string)
            lb_clock.after(1000, clock)

        def xoa():
            global DF_SinhVien
            my_text.delete("1.0", END)
            DF_SinhVien.drop(DF_SinhVien.index[[int(tb_xoa.get())]], inplace=True)
            DF_SinhVien.reset_index(inplace=True, drop=True)

            f = open("sinhvien/SinhVien_xoa.txt", "w+")
            print(DF_SinhVien, file=f)
            f.close()

            text_file = open("sinhvien/SinhVien_xoa.txt", "r")
            stuff = text_file.read()
            my_text.insert(END, stuff)
            text_file.close()

            tb_xoa.delete(0, END)

        # https://www.geeksforgeeks.org/insert-row-at-given-position-in-pandas-dataframe/
        def Insert_row(row_number, df, row_value):
            # Starting value of upper half
            start_upper = 0
            # End value of upper half
            end_upper = row_number
            # Start value of lower half
            start_lower = row_number
            # End value of lower half
            end_lower = df.shape[0]
            # Create a list of upper_half index
            upper_half = [*range(start_upper, end_upper, 1)]
            # Create a list of lower_half index
            lower_half = [*range(start_lower, end_lower, 1)]
            # Increment the value of lower half by 1
            lower_half = [x.__add__(1) for x in lower_half]
            # Combine the two lists
            index_ = upper_half + lower_half
            # Update the index of the dataframe
            df.index = index_
            # Insert a row at the end
            df.loc[row_number] = row_value
            # Sort the index labels
            df = df.sort_index()
            # return the dataframe
            return df

        def chenTruoc():
            global DF_SinhVien
            my_text.delete("1.0", END)
            id = tb_SBD.get()
            hoTenDem = tb_hoTenDem.get()
            ten = tb_ten.get()
            phai = tb_phai.get()
            ngaySinh = tb_ngaySinh.get()
            doiTuongDT = tb_doiTuongDT.get()
            input_data = [id, hoTenDem, ten, phai, ngaySinh, doiTuongDT]
            DF_SinhVien = Insert_row(int(tb_chenTruoc.get()), DF_SinhVien, input_data)
            DF_SinhVien.reset_index(inplace=True, drop=True)

            f = open("sinhvien/SinhVien_chenTruoc.txt", "w+")
            print(DF_SinhVien, file=f)
            f.close()

            text_file = open("sinhvien/SinhVien_chenTruoc.txt", "r")
            stuff = text_file.read()
            my_text.insert(END, stuff)
            text_file.close()

            tb_SBD.delete(0, END)
            tb_hoTenDem.delete(0, END)
            tb_ten.delete(0, END)
            tb_phai.delete(0, END)
            tb_ngaySinh.delete(0, END)
            tb_doiTuongDT.delete(0, END)
            tb_chenTruoc.delete(0, END)

        def chenSau():
            global DF_SinhVien
            my_text.delete("1.0", END)
            id = tb_SBD.get()
            hoTenDem = tb_hoTenDem.get()
            ten = tb_ten.get()
            phai = tb_phai.get()
            ngaySinh = tb_ngaySinh.get()
            doiTuongDT = tb_doiTuongDT.get()
            input_data = [id, hoTenDem, ten, phai, ngaySinh, doiTuongDT]
            DF_SinhVien = Insert_row(int(tb_chenSau.get()) + 1, DF_SinhVien, input_data)
            DF_SinhVien.reset_index(inplace=True, drop=True)

            f = open("sinhvien/SinhVien_chenSau.txt", "w+")
            print(DF_SinhVien, file=f)
            f.close()

            text_file = open("sinhvien/SinhVien_chenSau.txt", "r")
            stuff = text_file.read()
            my_text.insert(END, stuff)
            text_file.close()

            tb_SBD.delete(0, END)
            tb_hoTenDem.delete(0, END)
            tb_ten.delete(0, END)
            tb_phai.delete(0, END)
            tb_ngaySinh.delete(0, END)
            tb_doiTuongDT.delete(0, END)
            tb_chenTruoc.delete(0, END)


        # Lable data
        lb_data = tk.LabelFrame(self, padx=20, pady=15, text="Bảng sinh viên")
        lb_data.place(x=10, y=10)

        my_text = tk.Text(lb_data, width=68)
        my_text.grid(row=3, column=0, sticky=tk.W, padx=10, pady=10)
        text_file = open("sinhvien/SinhVien_data.txt", "r")
        stuff = text_file.read()
        my_text.insert(END, stuff)
        text_file.close()

        #Lable clock
        lb_clock = Label(self, font=("Digital-7", 20), background="#8ddbff", foreground='black')
        lb_clock.place(x=650, y=10)
        clock()

        # Lable Information
        lb_info = tk.LabelFrame(self, padx=10, pady=15, text="Thông tin")
        lb_info.place(x=650, y=50)

        tk.Label(lb_info, text="Số báo danh").grid(row=0, column=0,sticky='W')
        tb_SBD = tk.Entry(lb_info)
        tb_SBD.grid(row=0, column=1, sticky=tk.W, padx=5, pady=5, ipadx=50)

        tk.Label(lb_info, text="Họ & tên đệm").grid(row=1, column=0,sticky='W')
        tb_hoTenDem = tk.Entry(lb_info)
        tb_hoTenDem.grid(row=1, column=1, sticky=tk.W, padx=5, pady=5, ipadx=50)

        tk.Label(lb_info, text="Tên").grid(row=2, column=0,sticky='W')
        tb_ten = tk.Entry(lb_info)
        tb_ten.grid(row=2, column=1, sticky=tk.W, padx=5, pady=5, ipadx=50)

        tk.Label(lb_info, text="Phái (Nam: 0, Nữ: 1)").grid(row=3, column=0,sticky='W')
        tb_phai = tk.Entry(lb_info)
        tb_phai.grid(row=3, column=1, sticky=tk.W, padx=5, pady=5, ipadx=50)

        tk.Label(lb_info, text="Ngày sinh").grid(row=4, column=0,sticky='W')
        tb_ngaySinh = tk.Entry(lb_info)
        tb_ngaySinh.grid(row=4, column=1, sticky=tk.W, padx=5, pady=5, ipadx=50)

        tk.Label(lb_info, text="Đối tượng dự thi").grid(row=5, column=0,sticky='W')
        tb_doiTuongDT = tk.Entry(lb_info)
        tb_doiTuongDT.grid(row=5, column=1, sticky=tk.W, padx=5, pady=5, ipadx=50)


        # Lable Control
        lb_control = tk.LabelFrame(self, padx=10)
        lb_control.place(x=650, y=310)

        tk.Label(lb_control, text="Xóa sinh viên thứ").grid(row=0, column=0,sticky='W')
        tb_xoa = tk.Spinbox(lb_control, from_=0, to_=sys.maxsize, width=10)
        tb_xoa.grid(row=0, column=1, sticky=tk.W, padx=10, pady=5)

        tk.Label(lb_control, text="Chèn trước sinh viên thứ:").grid(row=1, column=0,sticky='W')
        tb_chenTruoc = tk.Spinbox(lb_control, from_=0, to_=sys.maxsize, width=10)
        tb_chenTruoc.grid(row=1, column=1, sticky=tk.W, padx=10, pady=5)

        tk.Label(lb_control, text="Chèn sau sinh viên thứ:").grid(row=2, column=0,sticky='W')
        tb_chenSau = tk.Spinbox(lb_control, from_=0, to_=sys.maxsize, width=10)
        tb_chenSau.grid(row=2, column=1, sticky=tk.W, padx=10, pady=5)

        btn_xoa = tk.Button(lb_control, text="Xóa", width=8, height=1, command=xoa)
        btn_xoa.grid(row=0, column=2, padx=7)

        btn_chenTruoc = tk.Button(lb_control, text="Chèn trước", width=8, height=1, command=chenTruoc)
        btn_chenTruoc.grid(row=1, column=2, padx=7)

        btn_chenSau = tk.Button(lb_control, text="Chèn sau", width=8, height=1, command=chenSau)
        btn_chenSau.grid(row=2, column=2, padx=7)


List_DiemThi = [(1,          8.00,         5.00,         8.00),
                (2,          6.50,         7.00,         5.00),
                (3,          7.50,         6.50,         4.00),
                (4,          5.00,         8.50,         5.50),
                (5,          6.50,         6.00,         6.00),
                (6,          10.00,        9.00,         9.00),
                (7,          7.00,         10.00,        6.50),
                (8,          10.00,        8.00,         9.00),
                (9,          10.00,        8.50,         10.00),
                (10,         4.50,         4.00,         4.00),
                (11,         8.00,         10.00,        7.00),
                (12,         5.00,         6.50,         5.50),
                (13,         9.00,         6.00,         8.00),
                (14,         6.00,         5.50,         8.00),
                (15,         8.00,         6.50,         7.50),
                (16,         4.00,         6.00,         5.00 ),
                (17,         5.00,         6.50,         4.00 ),
                (18,         4.00,         6.50,         6.00),
                (19,         4.00,         6.00,         6.00),
                (20,         5.00,         7.00,         7.00),
                (21,         10.00,        8.00,         9.00),
                (22,         5.00,         8.00,         5.00),
                (23,         8.00,         6.00,         7.00),
                (24,         7.00,         5.00,         7.00),
                (25,         5.00,         6.00,         6.00),
                (26,         10.00,        8.50,         9.00),
                (27,         8.00,         6.00,         9.00),
                (28,         6.00,         8.00,         4.00),
                (29,         6.00,         5.00,         6.00),
                (30,         6.00,         6.50,        6.00),
                (31,         7.00,         5.50,         5.00),
                (32,         6.00,         6.00,         4.50),
                (33,         6.50,         6.50,         6.00),
                (34,         5.00,         8.00,         5.00),
                (35,         10.00,        8.00,         9.00),
                (36,         6.00,         6.00,         6.50),
                (37,         7.00,         5.00,         5.50),
                (38,         6.50,         5.50,         5.00),
                (39,         8.00,         6.00,         8.00),
                (40,         4.00,         4.00,         4.00),
                (41,         5.00,         7.00,         7.00),
                (42,         5.50,         6.50,         8.00),
                (43,         9.00,         7.00,         10.00),
                (44,         6.00,         6.00,         9.00),
                (45,         8.00,         5.00,         7.00),
                (46,         5.50,         5.00,         4.00),
                (47,         9.50,         8.00,         10.00),
                (48,         10.00,        8.00,         10.00),
                (49,         6.00,         7.00,         5.50),
                (50,         10.00,        8.50,         9.50),
                (51,         8.00,         6.00,         9.00),
                (52,         4.50,         5.50,         5.00),
                (53,         9.00,         8.50,         10.00),
                (54,         6.50,         6.50,         4.00),
                (55,         7.50,         4.50,         6.00),
                (56,         7.00,         5.50,         8.00),
                (57,         9.00,         6.00,         6.50),
                (58,         4.00,         5.50,         4.00),
                (59,         10.00,        8.50,         9.00),
                (60,         5.50,         6.00,         5.50),
                (61,         5.00,         5.00,         6.00),
                (62,         6.50,         4.00,         5.50),
                (63,         10.00,        6.00,         7.00),
                (64,         6.00,         5.00,         6.00),
                (65,         4.00,         6.00,         4.50),
                (66,         7.00,         5.00,         3.00),
                (67,         10.00,        9.00,         10.00),
                (68,         8.00,         4.00,         5.00),
                (69,         9.00,         8.00,        8.00),
                (70,         5.50,         5.50,         7.50),
                (71,         5.00,         9.00,         7.00),
                (72,         6.50,         5.00,        8.00),
                (73,         6.00,         7.50,         8.00),
                (74,         10.00,        6.00,         8.00),
                (75,         8.50,         6.50,         6.00),
                (76,         8.00,         7.00,         8.50),
                (77,         8.00,         7.50,         9.00),
                (78,         4.50,         6.50,         4.00),
                (79,         10.00,        9.00,         10.00),
                (80,         3.50,         4.00,         5.50),
                (81,         6.00,         6.50,         4.50),
                (82,         8.00,         6.00,         4.00),
                (83,         5.00,         8.50,         5.00),
                (84,         10.00,        7.00,         9.00),
                (85,         7.00,         7.00,         10.00),
                (86,         5.50,         6.50,         6.50),
                (87,         8.00,         4.50,         8.00),
                (88,         5.00,         5.50,         6.00),
                (89,         4.50,         6.00,         5.00),
                (90,         4.50,         6.50,         4.50),
                (91,         6.00,         5.00,         6.50),
                (92,         6.00,         5.50,         6.50),
                (93,         4.00,         5.00,         4.00),
                (94,         6.00,         4.50,         3.00),
                (95,         5.00,         5.50,         6.00),
                (96,         6.00,         6.50,         5.50),
                (97,         8.00,         6.00,         7.00),
                (98,         7.00,         6.00,         6.00),
                (99,         8.00,         7.00,         7.00),
                (100,        6.50,         5.00,         3.00),
                (101,        7.00,         7.00,         8.50),
                (102,        7.00,         6.50,         6.00),
                (103,        6.50,         4.00,         4.00),
                (104,        6.50,         7.00,         6.50),
                (105,        4.00,         6.50,         3.50),
                (106,        5.00,         6.00,         6.00),
                (107,        5.40,         5.70,         4.90),
                (108,        5.00,         5.00,         4.50),
                (109,        7.00,         7.00,         8.00),
                (110,        5.00,         6.80,         5.20),
                (111,        8.00,         7.00,         8.00),
                (112,        5.50,         5.50,         7.50),
                (113,        6.00,         3.00,         5.00),
                (114,        10.00,        10.00,        10.00),
                (115,        5.50,         7.00,         5.50),
                (116,        7.50,         7.00,         10.00),
                (117,        10.00,        9.00,         9.50),
                (118,        4.00,         4.00,         4.50),
                (119,        4.50,         5.50,         6.50),
                (120,        5.00,         6.00,         6.00),
                (121,        10.00,        8.50,         9.00),
                (122,        6.50,         6.50,         6.00),
                (123,        4.00,         7.50,         5.50),
                (124,        5.50,         5.00,         5.00),
                (125,        9.00,         7.00,         8.00),
                (126,        4.50,         6.50,         4.50),
                (127,        5.50,         4.00,         5.50),
                (128,        7.00,         4.00,         8.00),
                (129,        8.00,         5.00,         5.50),
                (130,        5.00,         5.00,         5.00),
                (131,        4.00,         4.00,         5.50),
                (132,        4.50,         4.50,         6.50),
                (133,        9.00,         8.00,         7.50),
                (134,        10.00,        8.00,         9.00),
                (135,        10.00,        8.50,         9.00),
                (136,        6.00,         4.00,         5.00),
                (137,        5.00,         6.00,         5.50),
                (138,        6.00,         5.50,         6.50),
                (139,        6.50,         9.00,         6.50),
                (140,        6.50,         5.50,         6.50),
                (141,        9.00,         7.00,         8.00),
                (142,        6.00,         7.00,         5.00),
                (143,        3.50,         5.50,         6.00),
                (144,        9.00,         6.00,         8.00),
                (145,        3.00,         5.00,         4.00),
                (146,        5.00,         6.50,         6.50),
                (147,        10.00,        8.00,         10.00),
                (148,        9.50,         8.50,         9.00),
                (149,        9.00,         8.50,         10.00),
                (150,        8.00,         9.00,         6.00),
                (151,        5.00,         5.00,        6.00),
                (152,        10.00,        7.00,         7.00),
                (153,        7.50,         6.00,         8.00),
                (154,        4.00,         5.50,         7.00),
                (155,        7.00,         5.50,         3.50),
                (156,        4.00,         7.50,         5.00)]

DF_DiemThi = pd.DataFrame.from_records(List_DiemThi, columns=['SBD', 'Toan', 'Van', 'AnhVan'])
f = open("diemthi/DiemThi_data.txt", "w")
print(DF_DiemThi, file=f)
f.close()

# <--------------Giao diện điểm thi-------------->
class formDiemThi(tk.Toplevel):
    def __init__(self, parent):
        tk.Toplevel.__init__(self, parent)
        self.title("Điểm thi")
        self.geometry("755x360")
        self.iconbitmap("image/icons8-table-48.ico")
        self.configure(bg='#8ddbff')
        self.resizable(False,False)

        def clock():
            string = strftime('%I:%M:%S:%p')
            lb_clock.config(text=string)
            lb_clock.after(1000, clock)

        def xoa():
            global DF_DiemThi
            my_text.delete("1.0", END)

            DF_DiemThi.drop(DF_DiemThi.index[int(tb_xoa.get())], inplace=True)
            DF_DiemThi.reset_index(inplace=True, drop=True)

            f = open("diemthi/DiemThi_xoa.txt", "w+")
            print(DF_DiemThi, file=f)
            f.close()

            text_file = open("diemthi/DiemThi_xoa.txt", "r")
            stuff = text_file.read()
            my_text.insert(END, stuff)
            text_file.close()

            tb_xoa.delete(0, END)

        # https://www.geeksforgeeks.org/insert-row-at-given-position-in-pandas-dataframe/
        def Insert_row(row_number, df, row_value):
            # Starting value of upper half
            start_upper = 0
            # End value of upper half
            end_upper = row_number
            # Start value of lower half
            start_lower = row_number
            # End value of lower half
            end_lower = df.shape[0]
            # Create a list of upper_half index
            upper_half = [*range(start_upper, end_upper, 1)]
            # Create a list of lower_half index
            lower_half = [*range(start_lower, end_lower, 1)]
            # Increment the value of lower half by 1
            lower_half = [x.__add__(1) for x in lower_half]
            # Combine the two lists
            index_ = upper_half + lower_half
            # Update the index of the dataframe
            df.index = index_
            # Insert a row at the end
            df.loc[row_number] = row_value
            # Sort the index labels
            df = df.sort_index()
            # return the dataframe
            return df

        def chenTruoc():
            global DF_DiemThi
            my_text.delete("1.0", END)

            input_data = [tb_SBD.get(), tb_Toan.get(), tb_Van.get(), tb_AnhVan.get()]
            DF_DiemThi = Insert_row(int(tb_chenTruoc.get()), DF_DiemThi, input_data)
            DF_DiemThi.reset_index(inplace=True, drop=True)

            f = open("diemthi/DiemThi_chenTruoc.txt", "w+")
            print(DF_DiemThi, file=f)
            f.close()

            text_file = open("diemthi/DiemThi_chenTruoc.txt", "r")
            stuff = text_file.read()
            my_text.insert(END, stuff)
            text_file.close()

            tb_SBD.delete(0, END)
            tb_Toan.delete(0, END)
            tb_Van.delete(0, END)
            tb_AnhVan.delete(0, END)
            tb_chenTruoc.delete(0, END)

        def chenSau():
            global DF_DiemThi
            my_text.delete("1.0", END)

            input_data = [tb_SBD.get(), tb_Toan.get(), tb_Van.get(), tb_AnhVan.get()]
            DF_DiemThi = Insert_row(int(tb_chenSau.get()) + 1, DF_DiemThi, input_data)
            DF_DiemThi.reset_index(inplace=True, drop=True)

            f = open("diemthi/DiemThi_chenSau.txt", "w+")
            print(DF_DiemThi, file=f)
            f.close()

            text_file = open("diemthi/DiemThi_chenSau.txt", "r")
            stuff = text_file.read()
            my_text.insert(END, stuff)
            text_file.close()

            tb_SBD.delete(0, END)
            tb_Toan.delete(0, END)
            tb_Van.delete(0, END)
            tb_AnhVan.delete(0, END)
            tb_chenSau.delete(0, END)

        # Label data
        lb_data = tk.LabelFrame(self, text="Điểm Thi")
        lb_data.place(x=10, y=10)

        my_text = tk.Text(lb_data, width=30, height=16)
        my_text.grid(row=0, column=0, sticky=tk.W, padx=10, pady=10)
        text_file = open("diemthi/DiemThi_data.txt", "r")
        stuff = text_file.read()
        my_text.insert(END, stuff)
        text_file.close()

        #Label clock
        lb_clock = Label(self, font=("Digital-7", 20), background="#8ddbff", foreground='black')
        lb_clock.place(x=300, y=10)
        clock()

        #Label information
        lb_info = tk.LabelFrame(self, padx=20, pady=15, text="Thông tin")
        lb_info.place(x=300, y=50)

        tk.Label(lb_info, text="Số báo danh").grid(row=0, column=0,sticky='W')
        tb_SBD = tk.Entry(lb_info)
        tb_SBD.grid(row=0, column=1, sticky=tk.W, padx=5, pady=5)

        tk.Label(lb_info, text="Toán").grid(row=1, column=0,sticky='W')
        tb_Toan = tk.Entry(lb_info)
        tb_Toan.grid(row=1, column=1, sticky=tk.W, padx=5, pady=5)

        tk.Label(lb_info, text="Văn").grid(row=2, column=0,sticky='W')
        tb_Van = tk.Entry(lb_info)
        tb_Van.grid(row=2, column=1, sticky=tk.W, padx=5, pady=5)

        tk.Label(lb_info, text="Anh Văn").grid(row=3, column=0,sticky='W')
        tb_AnhVan = tk.Entry(lb_info)
        tb_AnhVan.grid(row=3, column=1, sticky=tk.W, padx=5, pady=5)

        # Label control
        tk.Label(lb_info, text="Xóa mẫu tin thứ:").grid(row=4, column=0,sticky='W')
        tb_xoa = tk.Spinbox(lb_info, from_=0, to_=sys.maxsize)
        tb_xoa.grid(row=4, column=1, sticky=tk.W, padx=5, pady=5)

        tk.Label(lb_info, text="Chèn trước mẫu tin số:").grid(row=5, column=0,sticky='W')
        tb_chenTruoc = tk.Spinbox(lb_info, from_=0, to_=sys.maxsize)
        tb_chenTruoc.grid(row=5, column=1, sticky=tk.W, padx=5, pady=5)

        tk.Label(lb_info, text="Chèn sau mẫu tin số:").grid(row=6, column=0,sticky='W')
        tb_chenSau = tk.Spinbox(lb_info, from_=0, to_=sys.maxsize)
        tb_chenSau.grid(row=6, column=1, sticky=tk.W, padx=5, pady=5)

        btn_xoa = tk.Button(lb_info, text="Xóa", width=8, height=1, command=xoa)
        btn_xoa.grid(row=4, column=2, padx=5.5)

        btn_chenTruoc = tk.Button(lb_info, text="Chèn trước", width=8, height=1, command=chenTruoc)
        btn_chenTruoc.grid(row=5, column=2, padx=5.5)

        btn_chenSau = tk.Button(lb_info, text="Chèn sau", width=8, height=1, command=chenSau)
        btn_chenSau.grid(row=6, column=2, padx=5.5)

# <----------------------Giao diện xếp loại (yêu cầu 5,6,7,8)---------------------->

class formXepLoai(tk.Toplevel):

    def __init__(self, parent):
        tk.Toplevel.__init__(self, parent)
        self.title("Xếp loại")
        self.geometry("1410x650")
        self.iconbitmap("image/icons8-room-48_1.ico")
        self.configure(bg='#8ddbff')

        def clock():
            string = strftime('%I:%M:%S:%p')
            lb_clock.config(text=string)
            lb_clock.after(1000, clock)

        def xepLoaiSinhVien():
            my_text.delete("1.0", END)

            DF_XepLoai = DF_SinhVien.merge(DF_DiemThi)

            DF_XepLoai["DTN"] = np.nan

            DF_XepLoai["TongDiem"] = np.nan

            DF_XepLoai["XepLoai"] = np.nan

            DF_Fields = DF_XepLoai.filter(["SBD", "Ho", "Ten", "Phai", "NgaySinh", "Toan", "Van", "AnhVan", "DTN", "TongDiem", "XepLoai", "DTDT"])
        
            #Doi du lieu DTDT theo DiemUT de tinh TongDiem
            DF_TongDiem = DF_Fields.apply(lambda x: x.replace(3,0) if x.name == 'DTDT'  else x)
            DF_TongDiem = DF_TongDiem.apply(lambda x: x.replace(2,4) if x.name == 'DTDT'  else x)
            DF_TongDiem = DF_TongDiem.apply(lambda x: x.replace(1,2) if x.name == 'DTDT'  else x)
            DF_TongDiem = DF_TongDiem.apply(lambda x: x.replace(4,1) if x.name == 'DTDT'  else x)
            
            #Tinh tong diem
            DF_TongDiem["TongDiem"] = DF_TongDiem["Toan"]+DF_TongDiem["Van"]+DF_TongDiem["AnhVan"]+DF_TongDiem["DTDT"]
            
            #Doi ten cot DTDT thanh DoiTuongDT
            DF_DoiTenField = DF_TongDiem.rename({'DTDT': 'DoiTuongDT'},axis=1)

            DF_DoiTenField["DTN"] = DF_DoiTenField[['Toan','Van','AnhVan']].min(axis=1)

            DF_XepLoaiSV = DF_DoiTenField

            #https://www.youtube.com/watch?v=8bvCkiByf-g&list=LL&index=1&t=497s -> Link huong dan
            dieuKien = [(DF_XepLoaiSV["TongDiem"]>=24) & (DF_XepLoaiSV["DTN"]>=7),
                        (DF_XepLoaiSV["TongDiem"]>=21) & (DF_XepLoaiSV["DTN"]>=6),
                        (DF_XepLoaiSV["TongDiem"]>=15) & (DF_XepLoaiSV["DTN"]>=4)]
            xepLoai = ["Giỏi", "Khá", "Trung bình"]
            DF_XepLoaiSV["XepLoai"] = np.select(dieuKien, xepLoai, default = "Trượt")
            
            #Doi du lieu DoiTuongDT theo DiemUT ve gia tri ban dau
            DF_XepLoaiSV = DF_XepLoaiSV.apply(lambda x: x.replace(0,3) if x.name == 'DoiTuongDT'  else x)
            DF_XepLoaiSV = DF_XepLoaiSV.apply(lambda x: x.replace(1,4) if x.name == 'DoiTuongDT'  else x)
            DF_XepLoaiSV = DF_XepLoaiSV.apply(lambda x: x.replace(2,1) if x.name == 'DoiTuongDT'  else x)
            DF_XepLoaiSV = DF_XepLoaiSV.apply(lambda x: x.replace(4,2) if x.name == 'DoiTuongDT'  else x)

            f = open("xeploai/XepLoaiSV.txt", "w+", encoding="utf8")
            print(DF_XepLoaiSV, file=f)
            f.close()

            text_file = open("xeploai/XepLoaiSV.txt", "r", encoding="utf8")
            stuff = text_file.read()
            my_text.insert(END, stuff)
            text_file.close()
        
        def sinhVienThuKhoa():
            my_text.delete("1.0", END)

            DF_XepLoai = DF_SinhVien.merge(DF_DiemThi)

            DF_XepLoai["DTN"] = np.nan

            DF_XepLoai["TongDiem"] = np.nan

            DF_XepLoai["XepLoai"] = np.nan

            DF_Fields = DF_XepLoai.filter(["SBD", "Ho", "Ten", "Phai", "NgaySinh", "Toan", "Van", "AnhVan", "DTN", "TongDiem", "XepLoai", "DTDT"])
        
            #Doi du lieu DTDT theo DiemUT
            DF_TongDiem = DF_Fields.apply(lambda x: x.replace(3,0) if x.name == 'DTDT'  else x)
            DF_TongDiem = DF_TongDiem.apply(lambda x: x.replace(2,4) if x.name == 'DTDT'  else x)
            DF_TongDiem = DF_TongDiem.apply(lambda x: x.replace(1,2) if x.name == 'DTDT'  else x)
            DF_TongDiem = DF_TongDiem.apply(lambda x: x.replace(4,1) if x.name == 'DTDT'  else x)

            #Tinh tong diem
            DF_TongDiem["TongDiem"] = DF_TongDiem["Toan"]+DF_TongDiem["Van"]+DF_TongDiem["AnhVan"]+DF_TongDiem["DTDT"]
            
            #Doi ten cot DTDT thanh DoiTuongDT
            DF_DoiTenField = DF_TongDiem.rename({'DTDT': 'DoiTuongDT'},axis=1)

            DF_DoiTenField["DTN"] = DF_DoiTenField[['Toan','Van','AnhVan']].min(axis=1)

            DF_XepLoaiSV = DF_DoiTenField

            #https://www.youtube.com/watch?v=8bvCkiByf-g&list=LL&index=1&t=497s -> Link huong dan
            dieuKien = [(DF_XepLoaiSV["TongDiem"]>=24) & (DF_XepLoaiSV["DTN"]>=7),
                        (DF_XepLoaiSV["TongDiem"]>=21) & (DF_XepLoaiSV["DTN"]>=6),
                        (DF_XepLoaiSV["TongDiem"]>=15) & (DF_XepLoaiSV["DTN"]>=4)]
            xepLoai = ["Giỏi", "Khá", "Trung bình"]
            DF_XepLoaiSV["XepLoai"] = np.select(dieuKien, xepLoai, default = "Trượt")

            #Cau 8
            DF_SapXepGiam = DF_XepLoaiSV.sort_values(by=["TongDiem"], ascending=False)

            DF_SinhVienLoaiGioi = DF_SapXepGiam.loc[DF_SapXepGiam['XepLoai']=='Giỏi']
            sinhVienThuKhoa = DF_SinhVienLoaiGioi['TongDiem'].max()
            DF_SinhVienThuKhoa = DF_SinhVienLoaiGioi.loc[DF_SinhVienLoaiGioi['TongDiem']==sinhVienThuKhoa]

            #Doi du lieu DoiTuongDT theo DiemUT ve gia tri ban dau
            DF_SinhVienThuKhoa = DF_SinhVienThuKhoa.apply(lambda x: x.replace(0,3) if x.name == 'DoiTuongDT'  else x)
            DF_SinhVienThuKhoa = DF_SinhVienThuKhoa.apply(lambda x: x.replace(1,4) if x.name == 'DoiTuongDT'  else x)
            DF_SinhVienThuKhoa = DF_SinhVienThuKhoa.apply(lambda x: x.replace(2,1) if x.name == 'DoiTuongDT'  else x)
            DF_SinhVienThuKhoa = DF_SinhVienThuKhoa.apply(lambda x: x.replace(4,2) if x.name == 'DoiTuongDT'  else x)
 
            f = open("xeploai/SinhVienThuKhoa.txt", "w+", encoding="utf8")
            print(DF_SinhVienThuKhoa, file=f)
            f.close()

            text_file = open("xeploai/SinhVienThuKhoa.txt", "r", encoding="utf8")
            stuff = text_file.read()
            my_text.insert(END, stuff)
            text_file.close()

        def sinhVienTruot():
            my_text.delete("1.0", END)

            DF_XepLoai = DF_SinhVien.merge(DF_DiemThi)

            DF_XepLoai["DTN"] = np.nan

            DF_XepLoai["TongDiem"] = np.nan

            DF_XepLoai["XepLoai"] = np.nan

            DF_Fields = DF_XepLoai.filter(["SBD", "Ho", "Ten", "Phai", "NgaySinh", "Toan", "Van", "AnhVan", "DTN", "TongDiem", "XepLoai", "DTDT"])
        
            #Doi du lieu DTDT theo DiemUT
            DF_TongDiem = DF_Fields.apply(lambda x: x.replace(3,0) if x.name == 'DTDT'  else x)
            DF_TongDiem = DF_TongDiem.apply(lambda x: x.replace(2,4) if x.name == 'DTDT'  else x)
            DF_TongDiem = DF_TongDiem.apply(lambda x: x.replace(1,2) if x.name == 'DTDT'  else x)
            DF_TongDiem = DF_TongDiem.apply(lambda x: x.replace(4,1) if x.name == 'DTDT'  else x)

            #Tinh tong diem
            DF_TongDiem["TongDiem"] = DF_TongDiem["Toan"]+DF_TongDiem["Van"]+DF_TongDiem["AnhVan"]+DF_TongDiem["DTDT"]
            
            #Doi ten cot DTDT thanh DoiTuongDT
            DF_DoiTenField = DF_TongDiem.rename({'DTDT': 'DoiTuongDT'},axis=1)

            DF_DoiTenField["DTN"] = DF_DoiTenField[['Toan','Van','AnhVan']].min(axis=1)

            DF_XepLoaiSV = DF_DoiTenField

            #https://www.youtube.com/watch?v=8bvCkiByf-g&list=LL&index=1&t=497s -> Link huong dan
            dieuKien = [(DF_XepLoaiSV["TongDiem"]>=24) & (DF_XepLoaiSV["DTN"]>=7),
                        (DF_XepLoaiSV["TongDiem"]>=21) & (DF_XepLoaiSV["DTN"]>=6),
                        (DF_XepLoaiSV["TongDiem"]>=15) & (DF_XepLoaiSV["DTN"]>=4)]
            xepLoai = ["Giỏi", "Khá", "Trung bình"]
            DF_XepLoaiSV["XepLoai"] = np.select(dieuKien, xepLoai, default = "Trượt")
            
            #Cau 7
            #Doi du lieu DoiTuongDT theo DiemUT ve gia tri ban dau
            DF_SinhVienTruot = DF_XepLoaiSV.apply(lambda x: x.replace(0,3) if x.name == 'DoiTuongDT'  else x)
            DF_SinhVienTruot = DF_SinhVienTruot.apply(lambda x: x.replace(1,4) if x.name == 'DoiTuongDT'  else x)
            DF_SinhVienTruot = DF_SinhVienTruot.apply(lambda x: x.replace(2,1) if x.name == 'DoiTuongDT'  else x)
            DF_SinhVienTruot = DF_SinhVienTruot.apply(lambda x: x.replace(4,2) if x.name == 'DoiTuongDT'  else x)

            #https://www.youtube.com/watch?v=Q3rBgcRZB1E -> Sap xep
            DF_SapXep = DF_SinhVienTruot.sort_values(by=["DoiTuongDT", "TongDiem"], ascending=[True, False])

            DF_SinhVienTruot = DF_SapXep.loc[DF_SapXep['XepLoai']=='Trượt']

            f = open("xeploai/SinhVienTruot.txt", "w+", encoding="utf8")
            print(DF_SinhVienTruot, file=f)
            f.close()

            text_file = open("xeploai/SinhVienTruot.txt", "r", encoding="utf8")
            stuff = text_file.read()
            my_text.insert(END, stuff)
            text_file.close()

        def sinhVienKhaGioi():

            my_text.delete("1.0", END)

            DF_XepLoai = DF_SinhVien.merge(DF_DiemThi)

            DF_XepLoai["DTN"] = np.nan

            DF_XepLoai["TongDiem"] = np.nan

            DF_XepLoai["XepLoai"] = np.nan

            DF_Fields = DF_XepLoai.filter(["SBD", "Ho", "Ten", "Phai", "NgaySinh", "Toan", "Van", "AnhVan", "DTN", "TongDiem", "XepLoai", "DTDT"])
        
            #Doi du lieu DTDT theo DiemUT
            DF_TongDiem = DF_Fields.apply(lambda x: x.replace(3,0) if x.name == 'DTDT'  else x)
            DF_TongDiem = DF_TongDiem.apply(lambda x: x.replace(2,4) if x.name == 'DTDT'  else x)
            DF_TongDiem = DF_TongDiem.apply(lambda x: x.replace(1,2) if x.name == 'DTDT'  else x)
            DF_TongDiem = DF_TongDiem.apply(lambda x: x.replace(4,1) if x.name == 'DTDT'  else x)

            #Tinh tong diem
            DF_TongDiem["TongDiem"] = DF_TongDiem["Toan"]+DF_TongDiem["Van"]+DF_TongDiem["AnhVan"]+DF_TongDiem["DTDT"]
            
            #Doi ten cot DTDT thanh DoiTuongDT
            DF_DoiTenField = DF_TongDiem.rename({'DTDT': 'DoiTuongDT'},axis=1)

            DF_DoiTenField["DTN"] = DF_DoiTenField[['Toan','Van','AnhVan']].min(axis=1)

            DF_XepLoaiSV = DF_DoiTenField

            #https://www.youtube.com/watch?v=8bvCkiByf-g&list=LL&index=1&t=497s -> Link huong dan
            dieuKien = [(DF_XepLoaiSV["TongDiem"]>=24) & (DF_XepLoaiSV["DTN"]>=7),
                        (DF_XepLoaiSV["TongDiem"]>=21) & (DF_XepLoaiSV["DTN"]>=6),
                        (DF_XepLoaiSV["TongDiem"]>=15) & (DF_XepLoaiSV["DTN"]>=4)]
            xepLoai = ["Giỏi", "Khá", "Trung bình"]
            DF_XepLoaiSV["XepLoai"] = np.select(dieuKien, xepLoai, default = "Trượt")
            
            #Cau 6
            #https://www.youtube.com/watch?v=Q3rBgcRZB1E -> Sap xep
            DF_SapXep = DF_XepLoaiSV.sort_values(by=["XepLoai", "TongDiem"], ascending=[False, False])

            DF_DiemToiDa = DF_SapXep.loc[(DF_SapXep['Toan']==10) | (DF_SapXep['Van']==10) | (DF_SapXep['AnhVan']==10) ]
            DF_SinhVienKhaGioi = DF_DiemToiDa.loc[(DF_DiemToiDa['XepLoai']=='Giỏi') | (DF_DiemToiDa['XepLoai']=='Khá') ]

             #Doi du lieu DoiTuongDT theo DiemUT ve gia tri ban dau
            DF_SinhVienKhaGioi = DF_SinhVienKhaGioi.apply(lambda x: x.replace(0,3) if x.name == 'DoiTuongDT'  else x)
            DF_SinhVienKhaGioi = DF_SinhVienKhaGioi.apply(lambda x: x.replace(1,4) if x.name == 'DoiTuongDT'  else x)
            DF_SinhVienKhaGioi = DF_SinhVienKhaGioi.apply(lambda x: x.replace(2,1) if x.name == 'DoiTuongDT'  else x)
            DF_SinhVienKhaGioi = DF_SinhVienKhaGioi.apply(lambda x: x.replace(4,2) if x.name == 'DoiTuongDT'  else x)

            f = open("xeploai/SinhVienKhaGioi.txt", "w+", encoding="utf8")
            print(DF_SinhVienKhaGioi, file=f)
            f.close()

            text_file = open("xeploai/SinhVienKhaGioi.txt", "r", encoding="utf8")
            stuff = text_file.read()
            my_text.insert(END, stuff)
            text_file.close()

        # Label data
        lb_data = tk.LabelFrame(self, padx=10, pady=15, text="Thông tin")
        lb_data.place(x=10, y=10)
        my_text = tk.Text(lb_data, width=110)
        my_text.grid(row=3, column=0, sticky=tk.W, padx=10, pady=10)

        DF_XepLoai = DF_SinhVien.merge(DF_DiemThi)

        DF_XepLoai["DTN"] = np.nan
        DF_XepLoai["TongDiem"] = np.nan
        DF_XepLoai["XepLoai"] = np.nan

        fields = DF_XepLoai.filter(["SBD", "Ho", "Ten", "Phai", "NgaySinh", "Toan", "Van", "AnhVan", "DTN", "TongDiem", "XepLoai", "DTDT"])

        f = open("xeploai/XepLoai_data.txt", "w+")
        print(fields, file=f)
        f.close()

        text_file = open("xeploai/XepLoai_data.txt", "r")
        stuff = text_file.read()
        my_text.insert(END, stuff)
        text_file.close()

        # Label clock
        lb_clock = Label(self, font=("Digital-7", 20), background="#8ddbff", foreground='black')
        lb_clock.place(x=965, y=10)
        clock()

        # Label control
        lb_control = tk.LabelFrame(self, padx=10, pady=15, text="Chức năng")
        lb_control.place(x=965, y=60)

        tk.Label(lb_control, text="Xếp loại sinh viên").grid(row=0, column=0,sticky='W')
        tk.Label(lb_control, text="Sinh viên khá giỏi, ít nhất một môn 10").grid(row=1, column=0,sticky='W')
        tk.Label(lb_control, text="Sinh viên trượt").grid(row=2, column=0,sticky='W')
        tk.Label(lb_control, text="Sinh viên thủ khoa").grid(row=3, column=0,sticky='W')

        btn_Luong = tk.Button(lb_control, text="Xem", command=xepLoaiSinhVien, width=8,height=1, background="blue", foreground="white")
        btn_Luong.grid(row=0, column=1,pady=2, padx=2)
        btn_Luong = tk.Button(lb_control, text="Xem", command=sinhVienKhaGioi, width=8,height=1, background="blue", foreground="white")
        btn_Luong.grid(row=1, column=1,pady=2, padx=2)
        btn_Luong = tk.Button(lb_control, text="Xem", command=sinhVienTruot, width=8,height=1, background="blue", foreground="white")
        btn_Luong.grid(row=2, column=1, pady=2, padx=2)
        btn_Luong = tk.Button(lb_control, text="Xem", command=sinhVienThuKhoa, width=8,height=1, background="blue", foreground="white")
        btn_Luong.grid(row=3, column=1, pady=2, padx=2)

List_ChiTietDT = [(1,  'Doi tuong thuoc dien chinh sach',                 2),
                  (2,  'Can bo, cong nhan vien chuc nha nuoc',              1),
                  (3,  'Hoc sinh pho thong',                                0),]
DF_ChiTietDT = pd.DataFrame.from_records(List_ChiTietDT, columns=['DoiTuongDT', 'DienGiaiDT', 'DiemUT'])
f = open("chitietdt/ChiTietDT_data.txt", "w")
print(DF_ChiTietDT, file=f)
f.close()

# <----------------------Giao diện chi tiết DT---------------------->

class formChiTietDT(tk.Toplevel):
    def __init__(self, parent):
        tk.Toplevel.__init__(self, parent)
        self.title("Chi tiết")
        self.geometry("955x500")
        self.iconbitmap("image/icons8-more-details-48.ico")
        self.configure(bg='#8ddbff')

        def clock():
            string = strftime('%I:%M:%S:%p')
            lb_clock.config(text=string)
            lb_clock.after(1000, clock)

        # Label clock
        lb_clock = Label(self, font=("Digital-7", 20), background="#8ddbff", foreground='black')
        lb_clock.place(x=550, y=5)
        clock()
        # tạo label cho thao tác và các btn
        label_inf = tk.LabelFrame(self, padx=20, pady=15, text="Thông tin")
        label_inf.place(x=550, y=45)

        # label đối tượng dự thi
        tk.Label(label_inf, text="Đối tượng dự thi").grid(row=0, column=0)
        tb_doiTuongDT = tk.Entry(label_inf)
        tb_doiTuongDT.grid(row=0, column=1, sticky=tk.W, padx=5, pady=5)
        # label diễn giải đối tượng
        tk.Label(label_inf, text="Diễn giải đối tượng").grid(row=1, column=0)
        tb_dienGiaiDT = tk.Entry(label_inf)
        tb_dienGiaiDT.grid(row=1, column=1, sticky=tk.W, padx=5, pady=5)
        # label điểm ưu tiên
        tk.Label(label_inf, text="Điểm ưu tiên").grid(row=2, column=0)
        tb_diemUT = tk.Entry(label_inf)
        tb_diemUT.grid(row=2, column=1, sticky=tk.W, padx=5, pady=5)
        
        # label btn xoa
        tk.Label(label_inf, text="Vị trí muốn xóa").grid(row=3, column=0)
        tb_xoa = tk.Spinbox(label_inf, from_=0, to_=sys.maxsize)
        tb_xoa.grid(row=3, column=1, sticky=tk.W, padx=5, pady=5)
        # label btn chen trc
        tk.Label(label_inf, text="Vị trí muốn thêm trước").grid(row=4, column=0)
        tb_chenTruoc = tk.Spinbox(label_inf, from_=0, to_=sys.maxsize)
        tb_chenTruoc.grid(row=4, column=1, sticky=tk.W, padx=5, pady=5)
        # label btn chen sau
        tk.Label(label_inf, text="Vị trí muốn thêm sau").grid(row=5, column=0)
        tb_chenSau = tk.Spinbox(label_inf, from_=0, to_=sys.maxsize)
        tb_chenSau.grid(row=5, column=1, sticky=tk.W, padx=5, pady=5)

        # tạo label cho thông tin đọc đc từ file lên
        label_data = tk.LabelFrame(self, padx=10, pady=20, text="Bảng chi tiết")
        label_data.place(x=10, y=10)

        my_text = tk.Text(label_data, height=15, width=60)
        my_text.grid(row=0, column=0, sticky=tk.W, pady=15, padx=10)
        text_file = open("chitietdt/ChiTietDT_data.txt", "r")
        stuff = text_file.read()
        my_text.delete(1.0, END)
        my_text.insert(END, stuff)
        text_file.close()

        def xoa():
            global DF_ChiTietDT
            DF_ChiTietDT.drop(DF_ChiTietDT.index[[int(tb_xoa.get())]], inplace=True)
            DF_ChiTietDT.reset_index(drop=True, inplace=True)

            my_text.delete(1.0, END)
            f = open("chitietdt/ChiTietDT_xoa.txt", "w+")
            print(DF_ChiTietDT, file=f)
            f.close()

            text_file = open("chitietdt/ChiTietDT_xoa.txt", "r")
            stuff = text_file.read()
            my_text.insert(END, stuff)
            text_file.close()
            # Xóa giá trị trong textbox:
            tb_xoa.delete(0, END)

        # btn xóa
        btn_xoa = tk.Button(label_inf, text="Xóa", width=8, height=1, command=xoa)
        btn_xoa.grid(row=7, column=0, padx=5.5)

        # Hàm chèn dòng bất kỳ
        # https://www.geeksforgeeks.org/insert-row-at-given-position-in-pandas-dataframe/
        def Insert_row(row_number, df, row_value):
            # Starting value of upper half
            start_upper = 0
            # End value of upper half
            end_upper = row_number
            # Start value of lower half
            start_lower = row_number
            # End value of lower half
            end_lower = df.shape[0]
            # Create a list of upper_half index
            upper_half = [*range(start_upper, end_upper, 1)]
            # Create a list of lower_half index
            lower_half = [*range(start_lower, end_lower, 1)]
            # Increment the value of lower half by 1
            lower_half = [x.__add__(1) for x in lower_half]
            # Combine the two lists
            index_ = upper_half + lower_half
            # Update the index of the dataframe
            df.index = index_
            # Insert a row at the end
            df.loc[row_number] = row_value
            # Sort the index labels
            df = df.sort_index()
            # return the dataframe
            return df

        def chenTruoc():
            global DF_ChiTietDT
            intput_data = [tb_doiTuongDT.get(), tb_dienGiaiDT.get(), tb_diemUT.get()]
            DF_ChiTietDT = Insert_row(int(tb_chenTruoc.get()), DF_ChiTietDT, intput_data)
            DF_ChiTietDT.reset_index(drop=True,inplace=True)

            my_text.delete("1.0", END)
            f = open("chitietdt/ChiTietDT_chenTruoc.txt", "w+")
            print(DF_ChiTietDT, file=f)
            f.close()
            # đọc lại file vào textbox
            text_file = open("chitietdt/ChiTietDT_chenTruoc.txt", "r")
            stuff = text_file.read()
            my_text.insert(END, stuff)
            text_file.close()

            # xóa text field sau khi thêm thông tin
            tb_chenTruoc.delete(0, END)
            tb_doiTuongDT.delete(0, END)
            tb_dienGiaiDT.delete(0, END)
            tb_diemUT.delete(0, END)

        # btn chèn trước
        btn_chenTruoc = tk.Button(label_inf, text="Chèn trước", width=8, height=1, command=chenTruoc)
        btn_chenTruoc.grid(row=7, column=1, padx=5.5)

        def chenSau():
            global DF_ChiTietDT
            intput_data = [tb_doiTuongDT.get(), tb_dienGiaiDT.get(), tb_diemUT.get()]
            DF_ChiTietDT = Insert_row(int(tb_chenSau.get()) + 1, DF_ChiTietDT, intput_data)
            DF_ChiTietDT.reset_index(drop=True, inplace=True)

            my_text.delete("1.0", END)
            f = open("chitietdt/ChiTietDT_chenSau.txt", "w+")
            print(DF_ChiTietDT, file=f)
            f.close()
            # đọc lại file vào textbox
            text_file = open("chitietdt/ChitietDT_chenSau.txt", "r")
            stuff = text_file.read()
            my_text.insert(END, stuff)
            text_file.close()
            # xóa text field sau khi thêm thông tin
            tb_chenSau.delete(0, END)
            tb_doiTuongDT.delete(0, END)
            tb_dienGiaiDT.delete(0, END)
            tb_diemUT.delete(0, END)

        # btn chèn sau
        btn_chenSau = tk.Button(label_inf, text="Chèn Sau", width=8, height=1, command=chenSau)
        btn_chenSau.grid(row=7, column=2, padx=5.5)
        
# <----------------------Giao diện thống kê (câu 9)---------------------->

class formThongKe(tk.Toplevel):
    def __init__(self, parent):
        tk.Toplevel.__init__(self, parent)
        self.title("Thống kê")
        self.geometry("1400x625")
        self.iconbitmap("image/icons8-total-sales-48.ico")
        self.configure(bg='#8ddbff')

        def clock():
            string = strftime('%I:%M:%S:%p')
            lb_clock.config(text=string)
            lb_clock.after(1000, clock)

        # Label clock
        lb_clock = Label(self, font=("Digital-7", 20), background="#8ddbff", foreground='black')
        lb_clock.place(x=1000, y=10)
        clock()

        # Label Info
        lb_control = tk.LabelFrame(self, padx=60, pady=15, text="Chức năng")
        lb_control.place(x=1000, y=60)

        tk.Label(lb_control, text="Đối tượng dự thi").grid(row=0, column=0,sticky='W')

        # Label control
        tk.Label(lb_control, text="").grid(row=1, column=1, sticky='W')

        # tạo label cho thông tin đọc đc từ file lên
        label_data = tk.LabelFrame(self, padx=10, pady=10, text="Bảng Thống Kê")
        label_data.place(x=10, y=10)

        def thongKeDT1():
            my_text.delete("1.0", END)

            DF_DTDT = DF_SinhVien.merge(DF_DiemThi)

            DF_DTDT["DTN"] = np.nan

            DF_DTDT["TongDiem"] = np.nan

            DF_DTDT["XepLoai"] = np.nan

            DF_Fields = DF_DTDT.filter(["SBD", "Ho", "Ten", "Phai", "NgaySinh", "Toan", "Van", "AnhVan", "DTN", "TongDiem", "XepLoai", "DTDT"])
        
            #Doi du lieu DTDT theo DiemUT
            DF_TongDiem = DF_Fields.apply(lambda x: x.replace(3,0) if x.name == 'DTDT'  else x)
            DF_TongDiem = DF_TongDiem.apply(lambda x: x.replace(2,4) if x.name == 'DTDT'  else x)
            DF_TongDiem = DF_TongDiem.apply(lambda x: x.replace(1,2) if x.name == 'DTDT'  else x)
            DF_TongDiem = DF_TongDiem.apply(lambda x: x.replace(4,1) if x.name == 'DTDT'  else x)
            
            #Tinh tong diem
            DF_TongDiem["TongDiem"] = DF_TongDiem["Toan"]+DF_TongDiem["Van"]+DF_TongDiem["AnhVan"]+DF_TongDiem["DTDT"]
            
            #Doi ten cot DTDT thanh DoiTuongDT
            DF_DoiTenField = DF_TongDiem.rename({'DTDT': 'DoiTuongDT'},axis=1)

            DF_DoiTenField["DTN"] = DF_DoiTenField[['Toan','Van','AnhVan']].min(axis=1)

            DF_XepLoaiSV = DF_DoiTenField

            #https://www.youtube.com/watch?v=8bvCkiByf-g&list=LL&index=1&t=497s -> Link huong dan
            dieuKien = [(DF_XepLoaiSV["TongDiem"]>=24) & (DF_XepLoaiSV["DTN"]>=7),
                        (DF_XepLoaiSV["TongDiem"]>=21) & (DF_XepLoaiSV["DTN"]>=6),
                        (DF_XepLoaiSV["TongDiem"]>=15) & (DF_XepLoaiSV["DTN"]>=4)]
            xepLoai = ["Giỏi", "Khá", "Trung bình"]
            DF_XepLoaiSV["XepLoai"] = np.select(dieuKien, xepLoai, default = "Trượt")

             #Doi du lieu DoiTuongDT theo DiemUT ve gia tri ban dau
            DF_SinhVienTruot = DF_XepLoaiSV.apply(lambda x: x.replace(0,3) if x.name == 'DoiTuongDT'  else x)
            DF_SinhVienTruot = DF_SinhVienTruot.apply(lambda x: x.replace(1,4) if x.name == 'DoiTuongDT'  else x)
            DF_SinhVienTruot = DF_SinhVienTruot.apply(lambda x: x.replace(2,1) if x.name == 'DoiTuongDT'  else x)
            DF_SinhVienTruot = DF_SinhVienTruot.apply(lambda x: x.replace(4,2) if x.name == 'DoiTuongDT'  else x)

            DF_ThongKe = DF_SinhVienTruot

            #DoiTuongDT1 -> thong ke so sinh vien dau, truot, ti le phan tram
            DF_DT1 = DF_ThongKe.loc[DF_ThongKe['DoiTuongDT'] == 1]
            tong_DT1 = len(DF_DT1)
            DT1_Truot = DF_DT1.loc[DF_DT1['XepLoai'] == 'Trượt']
            tong_DT1_Truot = len(DT1_Truot)
            DT1_Dau = DF_DT1.loc[DF_DT1['XepLoai'] == 'Giỏi'] + DF_DT1.loc[DF_DT1['XepLoai'] == 'Khá'] + DF_DT1.loc[DF_DT1['XepLoai'] == 'Trung bình']
            tong_DT1_Dau = len(DT1_Dau)
            tiLeDau_DT1 = (tong_DT1_Dau / tong_DT1) *100
            tiLeTruot_DT1 = (tong_DT1_Truot / tong_DT1) *100

            f = open("thongke/DoiTuongDT1.txt", "w+", encoding="utf8")
            print(DF_DT1, file=f)
            print("Tong sinh vien:", tong_DT1, file=f)
            print("Tong so truot:", tong_DT1_Truot, file=f)
            print("Tong so dau:", tong_DT1_Dau, file=f)
            print("Ti le truot:", tiLeTruot_DT1, file=f)
            print("Ti le dau:",  tiLeDau_DT1, file=f)
            f.close()

            text_file = open("thongke/DoiTuongDT1.txt", "r", encoding="utf8")
            stuff = text_file.read()
            my_text.insert(END, stuff)
            text_file.close()

        def thongKeDT2():

            my_text.delete("1.0", END)

            DF_DTDT = DF_SinhVien.merge(DF_DiemThi)

            DF_DTDT["DTN"] = np.nan

            DF_DTDT["TongDiem"] = np.nan

            DF_DTDT["XepLoai"] = np.nan

            DF_Fields = DF_DTDT.filter(["SBD", "Ho", "Ten", "Phai", "NgaySinh", "Toan", "Van", "AnhVan", "DTN", "TongDiem", "XepLoai", "DTDT"])
        
            #Doi du lieu DTDT theo DiemUT
            DF_TongDiem = DF_Fields.apply(lambda x: x.replace(3,0) if x.name == 'DTDT'  else x)
            DF_TongDiem = DF_TongDiem.apply(lambda x: x.replace(2,4) if x.name == 'DTDT'  else x)
            DF_TongDiem = DF_TongDiem.apply(lambda x: x.replace(1,2) if x.name == 'DTDT'  else x)
            DF_TongDiem = DF_TongDiem.apply(lambda x: x.replace(4,1) if x.name == 'DTDT'  else x)
            
            #Tinh tong diem
            DF_TongDiem["TongDiem"] = DF_TongDiem["Toan"]+DF_TongDiem["Van"]+DF_TongDiem["AnhVan"]+DF_TongDiem["DTDT"]
            
            #Doi ten cot DTDT thanh DoiTuongDT
            DF_DoiTenField = DF_TongDiem.rename({'DTDT': 'DoiTuongDT'},axis=1)

            DF_DoiTenField["DTN"] = DF_DoiTenField[['Toan','Van','AnhVan']].min(axis=1)

            DF_XepLoaiSV = DF_DoiTenField

            #https://www.youtube.com/watch?v=8bvCkiByf-g&list=LL&index=1&t=497s -> Link huong dan
            dieuKien = [(DF_XepLoaiSV["TongDiem"]>=24) & (DF_XepLoaiSV["DTN"]>=7),
                        (DF_XepLoaiSV["TongDiem"]>=21) & (DF_XepLoaiSV["DTN"]>=6),
                        (DF_XepLoaiSV["TongDiem"]>=15) & (DF_XepLoaiSV["DTN"]>=4)]
            xepLoai = ["Giỏi", "Khá", "Trung bình"]
            DF_XepLoaiSV["XepLoai"] = np.select(dieuKien, xepLoai, default = "Trượt")

             #Doi du lieu DoiTuongDT theo DiemUT ve gia tri ban dau
            DF_SinhVienTruot = DF_XepLoaiSV.apply(lambda x: x.replace(0,3) if x.name == 'DoiTuongDT'  else x)
            DF_SinhVienTruot = DF_SinhVienTruot.apply(lambda x: x.replace(1,4) if x.name == 'DoiTuongDT'  else x)
            DF_SinhVienTruot = DF_SinhVienTruot.apply(lambda x: x.replace(2,1) if x.name == 'DoiTuongDT'  else x)
            DF_SinhVienTruot = DF_SinhVienTruot.apply(lambda x: x.replace(4,2) if x.name == 'DoiTuongDT'  else x)

            DF_ThongKe = DF_SinhVienTruot

            #DoiTuongDT2 -> thong ke so sinh vien dau, truot, ti le phan tram
            DF_DT2 = DF_ThongKe.loc[DF_ThongKe['DoiTuongDT'] == 2]
            tong_DT2 = len(DF_DT2)
            DT2_Truot = DF_DT2.loc[DF_DT2['XepLoai'] == 'Trượt']
            tong_DT2_Truot = len(DT2_Truot)
            DT2_Dau = DF_DT2.loc[DF_DT2['XepLoai'] == 'Giỏi'] + DF_DT2.loc[DF_DT2['XepLoai'] == 'Khá'] + DF_DT2.loc[DF_DT2['XepLoai'] == 'Trung bình']
            tong_DT2_Dau = len(DT2_Dau)
            tiLeDau_DT2 = (tong_DT2_Dau / tong_DT2) *100
            tiLeTruot_DT2 = ((tong_DT2_Truot / tong_DT2) *100)

            f = open("thongke/DoiTuongDT2.txt", "w+", encoding="utf8")
            print(DF_DT2, file=f)
            print("Tong sinh vien:", tong_DT2, file=f)
            print("Tong so truot:", tong_DT2_Truot, file=f)
            print("Tong so dau:", tong_DT2_Dau, file=f)
            print("Ti le truot:", tiLeTruot_DT2, file=f)
            print("Ti le dau:",  tiLeDau_DT2, file=f)
            f.close()

            text_file = open("thongke/DoiTuongDT2.txt", "r", encoding="utf8")
            stuff = text_file.read()
            my_text.insert(END, stuff)
            text_file.close()

        def thongKeDT3():

            my_text.delete("1.0", END)

            DF_DTDT = DF_SinhVien.merge(DF_DiemThi)

            DF_DTDT["DTN"] = np.nan

            DF_DTDT["TongDiem"] = np.nan

            DF_DTDT["XepLoai"] = np.nan

            DF_Fields = DF_DTDT.filter(["SBD", "Ho", "Ten", "Phai", "NgaySinh", "Toan", "Van", "AnhVan", "DTN", "TongDiem", "XepLoai", "DTDT"])
        
            #Doi du lieu DTDT theo DiemUT
            DF_TongDiem = DF_Fields.apply(lambda x: x.replace(3,0) if x.name == 'DTDT'  else x)
            DF_TongDiem = DF_TongDiem.apply(lambda x: x.replace(2,4) if x.name == 'DTDT'  else x)
            DF_TongDiem = DF_TongDiem.apply(lambda x: x.replace(1,2) if x.name == 'DTDT'  else x)
            DF_TongDiem = DF_TongDiem.apply(lambda x: x.replace(4,1) if x.name == 'DTDT'  else x)
            
            #Tinh tong diem
            DF_TongDiem["TongDiem"] = DF_TongDiem["Toan"]+DF_TongDiem["Van"]+DF_TongDiem["AnhVan"]+DF_TongDiem["DTDT"]
            
            #Doi ten cot DTDT thanh DoiTuongDT
            DF_DoiTenField = DF_TongDiem.rename({'DTDT': 'DoiTuongDT'},axis=1)

            DF_DoiTenField["DTN"] = DF_DoiTenField[['Toan','Van','AnhVan']].min(axis=1)

            DF_XepLoaiSV = DF_DoiTenField

            #https://www.youtube.com/watch?v=8bvCkiByf-g&list=LL&index=1&t=497s -> Link huong dan
            dieuKien = [(DF_XepLoaiSV["TongDiem"]>=24) & (DF_XepLoaiSV["DTN"]>=7),
                        (DF_XepLoaiSV["TongDiem"]>=21) & (DF_XepLoaiSV["DTN"]>=6),
                        (DF_XepLoaiSV["TongDiem"]>=15) & (DF_XepLoaiSV["DTN"]>=4)]
            xepLoai = ["Giỏi", "Khá", "Trung bình"]
            DF_XepLoaiSV["XepLoai"] = np.select(dieuKien, xepLoai, default = "Trượt")

             #Doi du lieu DoiTuongDT theo DiemUT ve gia tri ban dau
            DF_SinhVienTruot = DF_XepLoaiSV.apply(lambda x: x.replace(0,3) if x.name == 'DoiTuongDT'  else x)
            DF_SinhVienTruot = DF_SinhVienTruot.apply(lambda x: x.replace(1,4) if x.name == 'DoiTuongDT'  else x)
            DF_SinhVienTruot = DF_SinhVienTruot.apply(lambda x: x.replace(2,1) if x.name == 'DoiTuongDT'  else x)
            DF_SinhVienTruot = DF_SinhVienTruot.apply(lambda x: x.replace(4,2) if x.name == 'DoiTuongDT'  else x)

            DF_ThongKe = DF_SinhVienTruot

            #DoiTuongDT3 -> thong ke so sinh vien dau, truot, ti le phan tram
            DF_DT3 = DF_ThongKe.loc[DF_ThongKe['DoiTuongDT'] == 3]
            tong_DT3 = len(DF_DT3)
            DT3_Truot = DF_DT3.loc[DF_DT3['XepLoai'] == 'Trượt']
            tong_DT3_Truot = len(DT3_Truot)
            DT3_Dau = DF_DT3.loc[DF_DT3['XepLoai'] == 'Giỏi'] + DF_DT3.loc[DF_DT3['XepLoai'] == 'Khá'] + DF_DT3.loc[DF_DT3['XepLoai'] == 'Trung bình']
            tong_DT3_Dau = len(DT3_Dau)
            tiLeDau_DT3 = (tong_DT3_Dau / tong_DT3) *100
            tiLeTruot_DT3 = (tong_DT3_Truot / tong_DT3) *100

            f = open("thongke/DoiTuongDT3.txt", "w+", encoding="utf8")
            print(DF_DT3, file=f)
            print("Tong sinh vien:", tong_DT3, file=f)
            print("Tong so truot:", tong_DT3_Truot, file=f)
            print("Tong so dau:", tong_DT3_Dau, file=f)
            print("Ti le truot:", tiLeTruot_DT3, file=f)
            print("Ti le dau:",  tiLeDau_DT3, file=f)
            f.close()

            text_file = open("thongke/DoiTuongDT3.txt", "r", encoding="utf8")
            stuff = text_file.read()
            my_text.insert(END, stuff)
            text_file.close()

        btn_ThongKeKH = tk.Button(lb_control, text="1", command=thongKeDT1, width=8, height=1,
                                  background="blue", foreground="white")
        btn_ThongKeKH.grid(row=0, column=1, pady=2, padx=2)

        btn_ThongKeKT = tk.Button(lb_control, text="2", command=thongKeDT2, width=8, height=1,
                                  background="blue", foreground="white")
        btn_ThongKeKT.grid(row=1, column=1, pady=2, padx=2)

        btn_ThongKeKT = tk.Button(lb_control, text="3", command=thongKeDT3, width=8, height=1,
                                  background="blue", foreground="white")
        btn_ThongKeKT.grid(row=2, column=1, pady=2, padx=2)

        my_text = tk.Text(label_data, height=32, width=115)
        my_text.grid(row=0, column=0, sticky=tk.W, pady=10, padx=10)


# <----------------------Giao diện tổng kết (câu 10 giấy báo điểm)---------------------->

class formTongKet(tk.Toplevel):
    def __init__(self, parent):
        tk.Toplevel.__init__(self, parent)
        self.title("Tổng kết")
        self.geometry("910x600")
        self.iconbitmap("image/icons8-brief-48.ico")
        self.configure(bg='#8ddbff')

        def clock():
            string = strftime('%I:%M:%S:%p')
            lb_clock.config(text=string)
            lb_clock.after(1000, clock)

        # Label clock
        lb_clock = Label(self, font=("Digital-7", 20), background="#8ddbff", foreground='black')
        lb_clock.place(x=700, y=10)
        clock()

        # Label control
        lb_control = tk.LabelFrame(self, padx=55, pady=15, text="Chức năng")
        lb_control.place(x=633, y=60)
        tk.Label(lb_control, text="Giấy báo điểm:").grid(row=0, column=0, sticky='W')

        # tạo label cho thông tin đọc đc từ file lên
        label_data = tk.LabelFrame(self, padx=10, pady=10, text="Bảng Tổng kết")
        label_data.place(x=20, y=15)

        def tongKet():
            my_text.delete("1.0", END)

            DF_DTDT = DF_SinhVien.merge(DF_DiemThi)

            DF_DTDT["DTN"] = np.nan

            DF_DTDT["TongDiem"] = np.nan

            DF_DTDT["XepLoai"] = np.nan

            DF_Fields = DF_DTDT.filter(["SBD", "Ho", "Ten", "Phai", "NgaySinh", "Toan", "Van", "AnhVan", "DTN", "TongDiem", "XepLoai", "DTDT"])
        
            #Doi du lieu DTDT theo DiemUT
            DF_TongDiem = DF_Fields.apply(lambda x: x.replace(3,0) if x.name == 'DTDT'  else x)
            DF_TongDiem = DF_TongDiem.apply(lambda x: x.replace(2,4) if x.name == 'DTDT'  else x)
            DF_TongDiem = DF_TongDiem.apply(lambda x: x.replace(1,2) if x.name == 'DTDT'  else x)
            DF_TongDiem = DF_TongDiem.apply(lambda x: x.replace(4,1) if x.name == 'DTDT'  else x)
            
            #Tinh tong diem
            DF_TongDiem["TongDiem"] = DF_TongDiem["Toan"]+DF_TongDiem["Van"]+DF_TongDiem["AnhVan"]+DF_TongDiem["DTDT"]
            
            #Doi ten cot DTDT thanh DoiTuongDT
            DF_DoiTenField = DF_TongDiem.rename({'DTDT': 'DoiTuongDT'},axis=1)

            DF_DoiTenField["DTN"] = DF_DoiTenField[['Toan','Van','AnhVan']].min(axis=1)

            DF_XepLoaiSV = DF_DoiTenField

            #https://www.youtube.com/watch?v=8bvCkiByf-g&list=LL&index=1&t=497s -> Link huong dan
            dieuKien = [(DF_XepLoaiSV["TongDiem"]>=24) & (DF_XepLoaiSV["DTN"]>=7),
                        (DF_XepLoaiSV["TongDiem"]>=21) & (DF_XepLoaiSV["DTN"]>=6),
                        (DF_XepLoaiSV["TongDiem"]>=15) & (DF_XepLoaiSV["DTN"]>=4)]
            xepLoai = ["Giỏi", "Khá", "Trung bình"]
            DF_XepLoaiSV["XepLoai"] = np.select(dieuKien, xepLoai, default = "Trượt")

             #Doi du lieu DoiTuongDT theo DiemUT ve gia tri ban dau
            DF_SinhVienTruot = DF_XepLoaiSV.apply(lambda x: x.replace(0,3) if x.name == 'DoiTuongDT'  else x)
            DF_SinhVienTruot = DF_SinhVienTruot.apply(lambda x: x.replace(1,4) if x.name == 'DoiTuongDT'  else x)
            DF_SinhVienTruot = DF_SinhVienTruot.apply(lambda x: x.replace(2,1) if x.name == 'DoiTuongDT'  else x)
            DF_SinhVienTruot = DF_SinhVienTruot.apply(lambda x: x.replace(4,2) if x.name == 'DoiTuongDT'  else x)

            DF_TongKet = DF_SinhVienTruot

            f = open("tongket/GiayBaoDiem.txt", "w+", encoding="utf8")
            print(DF_TongKet, file=f)
            print("GIAY BAO DIEM")
            f.close()

            text_file = open("tongket/GiayBaoDiem.txt", "r", encoding="utf8")
            stuff = text_file.read()
            my_text.insert(END, stuff)
            text_file.close()


        btn_ThongKeKH = tk.Button(lb_control, text="Xem", command=tongKet, width=8, height=1,
                                  background="blue", foreground="white")
        btn_ThongKeKH.grid(row=0, column=1, pady=2, padx=2)

        my_text = tk.Text(label_data, height=32, width=70)
        my_text.grid(row=0, column=0, sticky=tk.W, pady=10, padx=10)


# <----------------------Giao diện chính---------------------->
class formTrangChu(Frame):
    def __init__(self, other):
        Frame.__init__(self, other)
        self.other = other
        self.taoForm()

    def moFile(self):
        moFile = formMoFile(self)
        moFile.grab_set()
    def sinhVien(self):
        sinhVien = formSinhVien(self)
        sinhVien.grab_set()
    def diemThi(self):
        diemThi = formDiemThi(self)
        diemThi.grab_set()
    def chiTietDT(self):
        chiTietDT = formChiTietDT(self)
        chiTietDT.grab_set()
    def xepLoai(self):
        xepLoaiSVien = formXepLoai(self)
        xepLoaiSVien.grab_set()
    def thongKe(self):
        thongKe = formThongKe(self)
        thongKe.grab_set()
    def tongKet(self):
        tongKet = formTongKet(self)
        tongKet.grab_set()

    def taoForm(self):
        self.other.title("Quản lý sinh viên")
        self.other.geometry("700x700")
        self.other.iconbitmap("image/icons8-us-dollar-48.ico")
        self.configure(bg='#8ddbff')
        self.pack(fill=BOTH, expand=1)

        lb_truong = tk.Label(self, text="TRƯỜNG ĐẠI HỌC SƯ PHẠM KỸ THUẬT\n KHOA ĐÀO TẠO CHẤT LƯỢNG CAO", font=("",13), background="#8ddbff")
        lb_truong.pack(pady=10)

        self.img1 = ImageTk.PhotoImage(Image.open("image/fhq.png"))
        panel1 = tk.Label(self, image = self.img1, background="#8ddbff")
        panel1.place(x=200, y = 80)
        self.img2 = ImageTk.PhotoImage(Image.open("image/ute.png"))
        panel2 = tk.Label(self, image = self.img2, background="#8ddbff")
        panel2.place(x=350, y = 80)
        #Label title
        lb_title = tk.Label(self, text="Quản lý điểm thi của một kì thi", font=("",24), background="#8ddbff")
        lb_title.place(x=120, y = 250)

        #Label information
        lb_infor = tk.LabelFrame(self, background="#8ddbff",borderwidth=0)
        lb_infor.place(x=120, y = 300)
        tk.Label(lb_infor, text="Giảng viên hướng dẫn:", font=("", 13), background="#8ddbff").grid(row=0, column=0, sticky='W', ipady = 10)
        tk.Label(lb_infor, text="Sinh viên thực hiện:", font=("", 13), background="#8ddbff").grid(row=1, column=0, sticky='W', ipady=10)
        tk.Label(lb_infor, text="GVC, ThS. Trần Tiến Đức", font=("", 13), background="#8ddbff").grid(row=0, column=1, sticky='W', ipady = 10)
        tk.Label(lb_infor, text="Quách Đinh Trường Thi", font=("", 13), background="#8ddbff").grid(row=1, column=1, sticky='W', ipady=10)
        tk.Label(lb_infor, text="Trần Võ Hoàng Lâm ", font=("", 13), background="#8ddbff").grid(row=2, column=1, sticky='W', ipady=10)
        tk.Label(lb_infor, text="19110294", font=("", 13), background="#8ddbff").grid(row=1, column=2, sticky='W',ipady=10)
        tk.Label(lb_infor, text="19110032", font=("", 13), background="#8ddbff").grid(row=2, column=2, sticky='W', ipady=10)

        #Label control
        lb_control = tk.LabelFrame(self, padx=10, pady=15, text="Chức năng",font=("", 13))
        lb_control.place(x=130, y = 440)

        tk.Label(lb_control, text="Mở 3 file ", font=("", 13)).grid(row=0, column=0, sticky='W', ipady = 10)
        tk.Label(lb_control, text="Mở trang sinh viên ",font=("", 13)).grid(row=1, column=0, sticky='W', ipady = 10)
        tk.Label(lb_control, text="Mở trang điểm thi ",font=("", 13)).grid(row=2, column=0, sticky='W', ipady = 10)
        tk.Label(lb_control, text="Mở trang chi tiết  ",font=("", 13)).grid(row=3, column=0, sticky='W', ipady = 10)
        tk.Label(lb_control, text="        ").grid(row=3, column=3)
        tk.Label(lb_control, text="Mở trang xếp loại ",font=("", 13)).grid(row=0, column=4, sticky='W', ipady = 10)
        tk.Label(lb_control, text="Mở trang thống kê ",font=("", 13)).grid(row=1, column=4, sticky='W', ipady = 10)
        tk.Label(lb_control, text="Mở trang tổng kết ",font=("", 13)).grid(row=2, column=4, sticky='W', ipady = 10)

        Button(lb_control,text=" Mở ", command=self.moFile).grid(row=0, column=1)
        Button(lb_control, text=" Mở ",  command=self.sinhVien).grid(row=1, column=1)
        Button(lb_control,text=" Mở ", command=self.diemThi).grid(row=2, column=1)
        Button(lb_control,text=" Mở ", command=self.chiTietDT).grid(row=3, column=1)
        Button(lb_control, text=" Mở ",  command=self.xepLoai).grid(row=0, column=5)
        Button(lb_control,text=" Mở ", command=self.thongKe).grid(row=1, column=5)
        Button(lb_control,text=" Mở ", command=self.tongKet).grid(row=2, column=5)

root = Tk()
root.resizable(False, False)
formTrangChu(root)
root.mainloop()
