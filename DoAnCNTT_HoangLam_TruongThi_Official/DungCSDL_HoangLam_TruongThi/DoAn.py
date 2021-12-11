import sys
import pandas as pd
import tkinter as tk
from tkinter import Frame, Tk, BOTH, END, ttk
from time import strftime
from tkinter import *
import  tkinter.messagebox as MessageBox
import mysql.connector as mysql
from tkcalendar import DateEntry
from datetime import date
from PIL import ImageTk, Image

#Thay đổi 4 thông số sau tùy vào từng máy
user = 'root' #Tên tài khoản MySQL WorkBench của máy
password ='truongthi123' #Mật khẩu MySQL WorkBench của máy
database = 'doancnttthiquachhoanglam' #Tên cơ sở dữ liệu của máy
host="localhost"#Tên host sử dụng

class formMoFile(tk.Toplevel):
    def __init__(self, parent):
        tk.Toplevel.__init__(self, parent)
        self.title("Mở file")
        self.geometry("650x550")
        self.iconbitmap("HinhAnh/icons8-align-text-left-48.ico")
        self.configure(bg='')
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

        openDS_btn = Button(self, text="Nhanvien.txt", activebackground="#42a5f5", width=12, height=1, command=open_DS)
        openDS_btn.place(x=40, y=500)
        openCTDT_btn = Button(self, text="ChiTiet.txt", activebackground="#42a5f5", width=12, height=1, command=open_CTDT)
        openCTDT_btn.place(x=160, y=500)
        openDT_btn = Button(self, text="HSChuVu.txt", activebackground="#42a5f5", width=12, height=1, command=open_DT)
        openDT_btn.place(x=280, y=500)
        openPB_btn = Button(self, text="Clear", activebackground="#42a5f5", width=12, height=1, command=clear_text)
        openPB_btn.place(x=390, y=500)
class formSinhVien(tk.Toplevel):
    def __init__(self, parent):
        tk.Toplevel.__init__(self, parent)
        self.title("Sinh Viên")
        self.geometry("920x420")
        self.iconbitmap("HinhAnh/icons8-employee-48_1.ico")
        self.configure(bg='#8ddbff')
        self.resizable(False,False)

        def clock():
            string = strftime('%I:%M:%S:%p')
            lb_clock.config(text=string)
            lb_clock.after(1000, clock)
        
        def DTDT():
            connection = mysql.connect(host = host, user=user, password=password, database=database)
            cursor = connection.cursor()
            cursor.execute("select DoiTuongDT from chitietdt")
            DTDTs = cursor.fetchall()
            cursor.close()
            connection.close()
            return DTDTs

        def xem():
            tree.delete(*tree.get_children())
            connection = mysql.connect(host = host, user=user, password=password, database=database)
            cursor = connection.cursor()
            cursor.execute("select * from sinhvien")
            i = 0
            for row in cursor:
                tree.insert('', i, values=(row[0], row[1], row[2], row[3], row[4], row[5]))
                i = i + 1
            connection.close()
            tree.pack()


        def xoa():
            SBD = tb_xoa.get()
            connection = mysql.connect(host = host, user=user, password=password, database=database)
            cursor = connection.cursor()
            cursor.execute("delete from sinhvien where SBD = "+SBD+"")
            cursor.execute("commit")
            tb_xoa.delete(0, END)
            MessageBox.showerror("Thông báo", "Xoá thành công")
            connection.close()
            xem()
        def chen():
            SBD = tb_SBD.get()
            Ho = tb_Ho.get()
            Ten = tb_Ten.get()
            Phai = tb_Phai.get()
            NgaySinh = tb_NgaySinh.get()
            DTDT = tb_DTDT.get()
            connection = mysql.connect(host = host, user=user, password=password, database=database)
            cursor = connection.cursor()
            cursor.execute("insert into sinhvien(SBD,Ho,Ten,Phai,NgaySinh,DTDT) values('" + SBD + "','" + Ho + "','" + Ten + "','" + Phai + "',STR_TO_DATE('" + NgaySinh + "', '%d/%m/%Y'),'" + DTDT + "')")
            cursor.execute("commit")

            tb_Ho.delete(0, END)
            tb_Ten.delete(0, END)
            tb_Phai.delete(0, END)
            tb_NgaySinh.delete(0, END)
            tb_DTDT.delete(0, END)

            MessageBox.showinfo("Thông báo", "Thêm thành công")
            connection.close()
            xem()

        lb_data = tk.LabelFrame(self, padx=20, pady=15, text="Bảng sinh viên")
        lb_data.place(x=10, y=10)

        tree = ttk.Treeview(lb_data, height=16)
        tree['show'] = 'headings'
        tree["columns"] = ['SBD', 'Ho', 'Ten', 'Phai', 'NgaySinh', 'DTDT']
        tree.column("SBD", width=50, anchor=tk.W)
        tree.column("Ho", width=100, anchor=tk.W)
        tree.column("Ten", width=50, anchor=tk.W)
        tree.column("Phai", width=50, anchor=tk.W)
        tree.column("NgaySinh", width=100, anchor=tk.W)
        tree.column("DTDT", width=50, anchor=tk.W)

        tree.heading("SBD", text="MaNV", anchor=tk.W)
        tree.heading("Ho", text="Ho", anchor=tk.W)
        tree.heading("Ten", text="Ten", anchor=tk.W)
        tree.heading("Phai", text="Phai", anchor=tk.W)
        tree.heading("NgaySinh", text="NgaySinh", anchor=tk.W)
        tree.heading("DTDT", text="DTDT", anchor=tk.W)
        xem()
        tree.pack()

        lb_clock = Label(self, font=("Digital-7", 20), background="#8ddbff", foreground='black')
        lb_clock.place(x=570, y=10)
        clock()

        # Lable Information
        lb_info = tk.LabelFrame(self, padx=10, pady=15, text="Thông tin")
        lb_info.place(x=570, y=50)
        tk.Label(lb_info, text="Số Báo Danh").grid(row=0, column=0, sticky='W')
        tb_SBD = tk.Entry(lb_info)
        tb_SBD.grid(row=0, column=1, sticky=tk.W, padx=5, pady=5)

        tk.Label(lb_info, text="Họ & tên đệm").grid(row=1, column=0, sticky='W')
        tb_Ho = tk.Entry(lb_info)
        tb_Ho.grid(row=1, column=1, sticky=tk.W, padx=5, pady=5)

        tk.Label(lb_info, text="Tên").grid(row=2, column=0, sticky='W')
        tb_Ten = tk.Entry(lb_info)
        tb_Ten.grid(row=2, column=1, sticky=tk.W, padx=5, pady=5)

        tk.Label(lb_info, text="Phái").grid(row=3, column=0, sticky='W')
        tb_Phai = tk.Spinbox(lb_info, from_ = 0, to_=1, width=5)
        tb_Phai.grid(row=3, column=1, sticky=tk.W, padx=5, pady=5)

        tk.Label(lb_info, text="Ngày sinh").grid(row=4, column=0, sticky='W')
        tb_NgaySinh = DateEntry(lb_info, locale='en_US', date_pattern='d/m/Y')
        tb_NgaySinh.grid(row=4, column=1, sticky=tk.W, padx=5, pady=5)
        dt=date.today()
        tb_NgaySinh.set_date(dt)


        tk.Label(lb_info, text="Đối Tượng Dự Thi").grid(row=5, column=0, sticky='W')
        tb_DTDT = ttk.Combobox(lb_info,values=DTDT(), width=5)
        tb_DTDT.grid(row=5, column=1, sticky=tk.W, padx=6, pady=5)

        # Lable Control
        lb_control = tk.LabelFrame(self, padx=10)
        lb_control.place(x=570, y=315)

        tk.Label(lb_control, text="Xóa số báo danh ").grid(row=0, column=0, sticky='W')
        tb_xoa = tk.Entry(lb_control, width=10)
        tb_xoa.grid(row=0, column=1, sticky=tk.W, padx=10, pady=5)

        tk.Label(lb_control, text="Thêm sinh viên:").grid(row=1, column=0, sticky='W')

        btn_chen = tk.Button(lb_control, text="Thêm", width=8, height=1, command=chen)
        btn_chen.grid(row=1, column=2, padx=7)

        btn_xoa = tk.Button(lb_control, text="Xóa", width=8, height=1, command=xoa)
        btn_xoa.grid(row=0, column=2, padx=7)
class formXepLoai(tk.Toplevel):
    def __init__(self, parent):
        tk.Toplevel.__init__(self, parent)
        self.title("Xếp loại")
        self.geometry("660x250")
        self.iconbitmap("HinhAnh/icons8-employee-48_1.ico")
        self.configure(bg='#8ddbff')
        self.resizable(False,False)
        def clock():
            string = strftime('%I:%M:%S:%p')
            lb_clock.config(text=string)
            lb_clock.after(1000, clock)

        def diemThi():
            connection = mysql.connect(host = host, user=user, password=password, database=database)
            cursor = connection.cursor()
            cursor.execute("select SBD from diemthi")
            DiemThi = cursor.fetchall()
            cursor.close()
            connection.close()
            return DiemThi


        def xepLoai():
            tree.delete(*tree.get_children())
            connection = mysql.connect(host = host, user=user, password=password, database=database)
            cursor = connection.cursor()
            query="select sv.SBD, sv.Ho, sv.Ten, sv.Phai, sv.NgaySinh, dt.Toan, dt.Van, dt.AnhVan, from sinhvien sv, diemthi dt where sv.SBD = dt.SBD order by sv.SBD"
            cursor.execute(query)
            DF_XepLoai = pd.DataFrame.from_records(cursor, columns=['SBD', 'Ho', 'Ten', 'Phai', 'NgaySinh', 'Toan', 'Van', 'AnhVan','DTN' , 'TongDiem', 'XepLoai', 'DoiTuongDT'])
            f = open("xeploai/XepLoaiSV.txt", "w+")
            print(DF_XepLoai, file=f)
            f.close()

            cursor.execute(query)
            i=0
            for row in cursor:
                tree.insert('',i,values=(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11]))
                i=i+1
            connection.close()
            tree.pack()

        def xem():
            tree.delete(*tree.get_children())
            connection = mysql.connect(host = host, user=user, password=password, database=database)
            cursor = connection.cursor()
            cursor.execute("select * from sinhvien")
            i=0
            for row in cursor:
                tree.insert('',i,values=(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11]))
                i=i+1
            connection.close()
            tree.pack()



        lb_data = tk.LabelFrame(self, padx=10, pady=10, text="Bảng xếp loại")
        lb_data.place(x=10, y=10)

        tree = ttk.Treeview(lb_data,height=8)
        tree['show'] = 'headings'
        tree["columns"] = ['SBD', 'Ho', 'Ten', 'Phai', 'NgaySinh', 'Toan', 'Van', 'AnhVan','DTN' , 'TongDiem', 'XepLoai', 'DoiTuongDT']
        tree.column("SBD", width=50, anchor=tk.W)
        tree.column("Ho", width=200, anchor=tk.W)
        tree.column("Ten", width=200, anchor=tk.W)
        tree.column("Phai", width=200, anchor=tk.W)
        tree.column("NgaySinh", width=200, anchor=tk.W)
        tree.column("Toan", width=200, anchor=tk.W)
        tree.column("Van", width=200, anchor=tk.W)
        tree.column("AnhVan", width=200, anchor=tk.W)
        tree.column("DTN", width=200, anchor=tk.W)
        tree.column("TongDiem", width=200, anchor=tk.W)
        tree.column("XepLoai", width=200, anchor=tk.W)
        tree.column("DoiTuongDT", width=200, anchor=tk.W)


        tree.heading("SBD", text="SBD", anchor=tk.W)
        tree.heading("Ho", text="Ho", anchor=tk.W)
        tree.heading("Ten", text="Ten", anchor=tk.W)
        tree.heading("Phai", text="Phai", anchor=tk.W)
        tree.heading("NgaySinh", text="NgaySinh", anchor=tk.W)
        tree.heading("Toan", text="Toan", anchor=tk.W)
        tree.heading("Van", text="Van", anchor=tk.W)
        tree.heading("AnhVan", text="AnhVan", anchor=tk.W)
        tree.heading("DTN", text="DTN", anchor=tk.W)
        tree.heading("TongDiem", text="TongDiem", anchor=tk.W)
        tree.heading("XepLoai", text="XepLoai", anchor=tk.W)
        tree.heading("DoiTuongDT", text="DoiTuongDT", anchor=tk.W)
        xem()
        tree.pack()

        lb_clock = Label(self, font=("Digital-7", 20), background="#8ddbff", foreground='black')
        lb_clock.place(x=300, y=10)
        clock()

        # Lable Information
        lb_info = tk.LabelFrame(self, padx=10, pady=15, text="Thông tin")
        lb_info.place(x=300, y=50)

        tk.Label(lb_info, text="Mã phòng ban").grid(row=0, column=0, sticky='W')
        tb_MaPB = tk.Entry(lb_info)
        tb_MaPB.grid(row=0, column=1, sticky=tk.W, padx=5, pady=5)

        tk.Label(lb_info, text="Tên phòng ban").grid(row=1, column=0, sticky='W')
        tb_TenPB = tk.Entry(lb_info)
        tb_TenPB.grid(row=1, column=1, sticky=tk.W, padx=5, pady=5)

        # Lable Control
        lb_control = tk.LabelFrame(self, padx=10)
        lb_control.place(x=300, y=170)

        tk.Label(lb_control, text="Xóa phòng ban có mã").grid(row=0, column=0, sticky='W')
        tb_xoa = tk.Entry(lb_control, width=10)
        tb_xoa.grid(row=0, column=1, sticky=tk.W, padx=10, pady=5)

        tk.Label(lb_control, text="Thêm phòng ban:").grid(row=1, column=0, sticky='W')

class formXepLoai(tk.Toplevel):
    def __init__(self, parent):
        tk.Toplevel.__init__(self, parent)
        self.title("Xếp loại sinh viên")
        self.geometry("900x490")
        self.iconbitmap("HinhAnh/icons8-cash-in-hand-48.ico")
        self.configure(bg='#8ddbff')
        self.resizable(False,False)

        def clock():
            string = strftime('%I:%M:%S:%p')
            lb_clock.config(text=string)
            lb_clock.after(1000, clock)
        
        def diemThi():
            connection = mysql.connect(host = host, user=user, password=password, database=database)
            cursor = connection.cursor()
            cursor.execute("select SBD from diemthi")
            SBD = cursor.fetchall()
            cursor.close()
            connection.close()
            return SBD

        def xem():
            tree.delete(*tree.get_children())
            connection = mysql.connect(host = host, user=user, password=password, database=database)
            cursor = connection.cursor()
            cursor.execute("select sv.SBD, sv.Ho, sv.Ten, sv.Phai, sv.NgaySinh, dt.Toan, dt.Van, dt.AnhVan, from sinhvien sv, diemthi dt where sv.SBD = dt.SBD order by sv.SBD")
            i = 0
            for row in cursor:
                tree.insert('', i, values=(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11]))
                i = i + 1
            connection.close()
            tree.pack()
        def xepLoai():
            tree.delete(*tree.get_children())
            connection = mysql.connect(host = host, user=user, password=password, database=database)
            cursor = connection.cursor()
            query="select nv.MaNV, nv.Ho, nv.Ten, nv.Phai, ct.ChucVu, ct.HSLuong*250000 as Luong, nv.MaPB from nhanvien nv, chitiet ct where nv.MaNV = ct.MaNV order by nv.MaPB"
            cursor.execute(query)
            DF_Luong = pd.DataFrame.from_records(cursor, columns=['SBD', 'Ho', 'Ten', 'Phai', 'NgaySinh', 'Toan', 'Van', 'AnhVan','DTN' , 'TongDiem', 'XepLoai', 'DoiTuongDT'])
            f = open("xeploai/xepLoaiSV.txt", "w+")
            print(DF_Luong, file=f)
            f.close()

            cursor.execute(query)
            i=0
            for row in cursor:
                tree.insert('',i,values=(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11]))
                i=i+1
            connection.close()
            tree.pack()


        def sinhVienKhaGioi():
            tree.delete(*tree.get_children())
            khaGioi = sb_khaGioi.get()
            connection = mysql.connect(host = host, user=user, password=password, database=database)
            cursor = connection.cursor()
            query="select nv.MaNV, nv.Ho, nv.Ten, nv.Phai, ct.ChucVu, ct.HSLuong*250000 as Luong, nv.MaPB from nhanvien nv, chitiet ct where nv.MaNV = ct.MaNV order by Luong desc limit "+khaGioi+""
            cursor.execute(query)

            DF_Luong = pd.DataFrame.from_records(cursor, columns=['SBD', 'Ho', 'Ten', 'Phai', 'NgaySinh', 'Toan', 'Van', 'AnhVan','DTN' , 'TongDiem', 'XepLoai', 'DoiTuongDT'])
            f = open("Luong/LuongCaoNhat.txt", "w+")
            print(DF_Luong, file=f)
            f.close()

            cursor.execute(query)
            i=0
            for row in cursor:
                tree.insert('',i,values=(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11]))
                i=i+1
            connection.close()
            tree.pack()

        def sinhVienTruot():
            tree.delete(*tree.get_children())
            SBD =  cb_SBD.get()
            connection = mysql.connect(host = host, user=user, password=password,database=database)
            cursor = connection.cursor()
            query = "select nv.MaNV, nv.Ho, nv.Ten, nv.Phai, ct.ChucVu, ct.HSLuong*250000 as Luong, nv.MaPB from nhanvien nv, chitiet ct where nv.MaNV = ct.MaNV and nv.MaPB = '"+SBD+"' and ct.HSLuong = (select max(ct.HSLuong) from nhanvien nv, chitiet ct where nv.MaNV = ct.MaNV and nv.MaPB = '"+SBD+"')"
            cursor.execute(query)
            DF_Luong = pd.DataFrame.from_records(cursor, columns=['SBD', 'Ho', 'Ten', 'Phai', 'NgaySinh', 'Toan', 'Van', 'AnhVan','DTN' , 'TongDiem', 'XepLoai', 'DoiTuongDT'])
            f = open("Luong/LuongCaoNhatTheoPhongBan"+SBD+".txt", "w+")
            print(DF_Luong, file=f)
            f.close()
            cursor.execute(query)
            i = 0
            for row in cursor:
                tree.insert('', i, values=(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11]))
                i = i + 1
            connection.close()
            tree.pack()

        def sinhVienThuKhoa():
            tree.delete(*tree.get_children())
            MaPB = cb_SBDTK.get()
            connection = mysql.connect(host = host, user=user, password=password,database=database)
            cursor = connection.cursor()
            query = "select nv.MaNV, nv.Ho, nv.Ten, nv.Phai, ct.ChucVu, ct.HSLuong*250000 as Luong, nv.MaPB from nhanvien nv, chitiet ct where nv.MaNV = ct.MaNV and nv.MaPB = '"+MaPB+"' and ct.HSLuong = (select max(ct.HSLuong) from nhanvien nv, chitiet ct where nv.MaNV = ct.MaNV and nv.MaPB = '"+MaPB+"')"
            cursor.execute(query)
            DF_Luong = pd.DataFrame.from_records(cursor, columns=['SBD', 'Ho', 'Ten', 'Phai', 'NgaySinh', 'Toan', 'Van', 'AnhVan','DTN' , 'TongDiem', 'XepLoai', 'DoiTuongDT'])
            f = open("Luong/LuongCaoNhatTheoPhongBan"+MaPB+".txt", "w+")
            print(DF_Luong, file=f)
            f.close()
            cursor.execute(query)
            i = 0
            for row in cursor:
                tree.insert('', i, values=(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11]))
                i = i + 1
            connection.close()
            tree.pack()


        lb_data = tk.LabelFrame(self, padx=10, pady=10, text="Bảng xếp loại")
        lb_data.place(x=10, y=10)

        tree = ttk.Treeview(lb_data, height=20)
        tree['show'] = 'headings'
        tree["columns"] = ['SBD', 'Ho', 'Ten', 'Phai', 'NgaySinh', 'Toan', 'Van', 'AnhVan','DTN' , 'TongDiem', 'XepLoai', 'DoiTuongDT']
        tree.column("SBD", width=50, anchor=tk.W)
        tree.column("Ho", width=200, anchor=tk.W)
        tree.column("Ten", width=200, anchor=tk.W)
        tree.column("Phai", width=200, anchor=tk.W)
        tree.column("NgaySinh", width=200, anchor=tk.W)
        tree.column("Toan", width=200, anchor=tk.W)
        tree.column("Van", width=200, anchor=tk.W)
        tree.column("AnhVan", width=200, anchor=tk.W)
        tree.column("DTN", width=200, anchor=tk.W)
        tree.column("TongDiem", width=200, anchor=tk.W)
        tree.column("XepLoai", width=200, anchor=tk.W)
        tree.column("DoiTuongDT", width=200, anchor=tk.W)


        tree.heading("SBD", text="SBD", anchor=tk.W)
        tree.heading("Ho", text="Ho", anchor=tk.W)
        tree.heading("Ten", text="Ten", anchor=tk.W)
        tree.heading("Phai", text="Phai", anchor=tk.W)
        tree.heading("NgaySinh", text="NgaySinh", anchor=tk.W)
        tree.heading("Toan", text="Toan", anchor=tk.W)
        tree.heading("Van", text="Van", anchor=tk.W)
        tree.heading("AnhVan", text="AnhVan", anchor=tk.W)
        tree.heading("DTN", text="DTN", anchor=tk.W)
        tree.heading("TongDiem", text="TongDiem", anchor=tk.W)
        tree.heading("XepLoai", text="XepLoai", anchor=tk.W)
        tree.heading("DoiTuongDT", text="DoiTuongDT", anchor=tk.W)
        xem()
        tree.pack()

        #Label clock
        lb_clock = Label(self, font=("Digital-7", 20), background="#8ddbff", foreground='black')
        lb_clock.place(x=500, y=10)
        clock()

        # Label control
        lb_control = tk.LabelFrame(self, padx=10, pady=15, text="Chức năng")
        lb_control.place(x=500, y=60)

        tk.Label(lb_control, text="Xếp loại sinh viên").grid(row=0, column=0, sticky='W')
        tk.Label(lb_control, text="Sinh viên khá giỏi").grid(row=1, column=0, sticky='W')
        sb_khaGioi = Spinbox(lb_control, from_ = 1, to_ = sys.maxsize,width=5)
        sb_khaGioi.grid(row=1, column=1, sticky=tk.W, padx=6, pady=5)

        tk.Label(lb_control, text="Sinh viên trượt").grid(row=2, column=0, sticky='W')
        cb_SBD = ttk.Combobox(lb_control, values=(), width=5)
        cb_SBD.grid(row=2, column=1, sticky=tk.W, padx=6, pady=5)

        tk.Label(lb_control, text="Sinh viên thủ khoa").grid(row=3, column=0, sticky='W')
        cb_SBDTK = ttk.Combobox(lb_control, values=(), width=5)
        cb_SBDTK.grid(row=2, column=1, sticky=tk.W, padx=6, pady=5)

        btn_xepLoai = tk.Button(lb_control, text="Tính", command=xepLoai, width=8, height=1, background="green",foreground="white")
        btn_xepLoai.grid(row=0, column=1, pady=2, padx=2)

        btn_svkhaGioi = tk.Button(lb_control, text="Xem", command=sinhVienKhaGioi, width=8, height=1, background="green",foreground="white")
        btn_svkhaGioi.grid(row=1, column=2, pady=2, padx=2)

        btn_svTruot = tk.Button(lb_control, text="Xem", command=sinhVienTruot, width=8, height=1,background="green", foreground="white")
        btn_svTruot.grid(row=2, column=2, pady=2, padx=2)

        btn_svThuKhoa = tk.Button(lb_control, text="Xem", command=sinhVienThuKhoa, width=8, height=1,background="green", foreground="white")
        btn_svThuKhoa.grid(row=3, column=2, pady=2, padx=2)
class formThongKe(tk.Toplevel):
    def __init__(self,parent):
        tk.Toplevel.__init__(self,parent)
        self.title("Thống kê")
        self.geometry("610x300")
        self.iconbitmap("HinhAnh/icons8-total-sales-48.ico")
        self.configure(bg='#8ddbff')

        def clock():
            string = strftime('%I:%M:%S:%p')
            lb_clock.config(text=string)
            lb_clock.after(1000, clock)

        def ThongKe():
            tree.delete(*tree.get_children())
            connection = mysql.connect(host = host, user=user, password=password, database=database)
            cursor = connection.cursor()
            query = "select pb.TenPB, nam.SoNam, nu.SoNu, (nam.SoNam+nu.SoNu) as TongSo from phongban pb, (select MaPB, count(*) as SoNam from nhanvien where Phai = '0' group by MaPB ) nam, (select MaPB, count(*) as SoNu from nhanvien where Phai = '1' group by MaPB) nu where pb.MaPB = nam.MaPB and pb.MaPB=nu.MaPB group by pb.MaPB;"
            cursor.execute(query)
            DF_ThongKe = pd.DataFrame.from_records(cursor,columns=['SBD', 'Ho', 'Ten', 'Phai'])
            f = open("ThongKe/ThongKe.txt", "w+")
            print(DF_ThongKe, file=f)
            f.close()

            cursor.execute(query)
            i = 0
            for row in cursor:
                tree.insert('', i, values=(row[0], row[1], row[2], row[3]))
                i = i + 1
            connection.close()
            tree.pack()

        # Label clock
        lb_clock = Label(self, font=("Digital-7", 20), background="#8ddbff", foreground='black')
        lb_clock.place(x=350, y=10)
        clock()

        # Label control
        lb_control = tk.LabelFrame(self, padx=60, pady=15, text="Chức năng")
        lb_control.place(x=350, y=60)
        tk.Label(lb_control, text="Thống kê").grid(row=0, column=0, sticky='W')

        # tạo label cho thông tin đọc đc từ file lên
        label_data = tk.LabelFrame(self, padx=10, pady=10, text="Bảng Thống Kê")
        label_data.place(x=10, y=10)

        tree = ttk.Treeview(label_data, height=10)
        tree['show'] = 'headings'
        tree["columns"] = ['SBD', 'Ho', 'Ten', 'Phai']
        tree.column("SBD", width=150, anchor=tk.W)
        tree.column("Ho", width=50, anchor=tk.W)
        tree.column("Ten", width=50, anchor=tk.W)
        tree.column("Phai", width=50, anchor=tk.W)

        tree.heading("SBD", text="SBD", anchor=tk.W)
        tree.heading("Ho", text="Ho", anchor=tk.W)
        tree.heading("Ten", text="Ten", anchor=tk.W)
        tree.heading("Phai", text="Phai", anchor=tk.W)
        # xem()
        tree.pack()

        btn_ThongKe = tk.Button(lb_control, text="Thống kê", command=ThongKe, width=8, height=1, background="green",
                               foreground="white")
        btn_ThongKe.grid(row=0, column=1, pady=2, padx=2)
class formChiTietDT(tk.Toplevel):
    def __init__(self, parent):
        tk.Toplevel.__init__(self, parent)
        self.title("ChiTietDT")
        self.geometry("700x420")
        self.iconbitmap("HinhAnh/icons8-brief-48.ico")
        self.configure(bg='#8ddbff')
        self.resizable(False,False)
    
        def clock():
            string = strftime('%I:%M:%S:%p')
            lb_clock.config(text=string)
            lb_clock.after(1000, clock)

        def xem():
            tree.delete(*tree.get_children())
            connection = mysql.connect(host = host, user=user, password=password, database=database)
            cursor = connection.cursor()
            cursor.execute("select * from chitietdt")
            i = 0
            for row in cursor:
                tree.insert('', i, values=(row[0], row[1], row[2]))
                i = i + 1
            connection.close()
            tree.pack()
        
        def xoa():
            SBD = tb_xoa.get()
            connection = mysql.connect(host = host, user=user, password=password, database=database)
            cursor = connection.cursor()
            cursor.execute("delete from chitietdt where SBD = "+SBD+"")
            cursor.execute("commit")
            tb_xoa.delete(0, END)
            MessageBox.showerror("Thông báo", "Xoá thành công")
            connection.close()
            xem()
        def chen():
            doiTuongDT = tb_doiTuongDT.get()
            DienGiaiDT = tb_DienGiaiDT.get()
            DiemUT = tb_DiemUT.get()
            #Vitri = tb_chenTruoc()
            connection = mysql.connect(host = host, user=user, password=password, database=database)
            cursor = connection.cursor()
            cursor.execute("insert into chitietdt(doiTuongDT,DienGiaiDT,DiemUT) values('" + doiTuongDT + "','" + DienGiaiDT + "','" + DiemUT + "','"  "')")
            cursor.execute("commit")

            tb_doiTuongDT.delete(0, END)
            tb_DienGiaiDT.delete(0, END)
            tb_DiemUT.delete(0, END)
            MessageBox.showinfo("Thông báo", "Thêm thành công")
            connection.close()
            xem()
        def chiTietDT():
            connection = mysql.connect(host = host, user=user, password=password, database=database)
            cursor = connection.cursor()
            cursor.execute("select DoiTuongDT from chitietdt")
            doiTuongDT = cursor.fetchall()
            cursor.close()
            connection.close()
            return doiTuongDT

        lb_data = tk.LabelFrame(self, padx=30, pady=15, text="Bảng chi tiết")
        lb_data.place(x=10, y=10)

        tree = ttk.Treeview(lb_data, height=16)
        tree['show'] = 'headings'
        tree["columns"] = ['DoiTuongDT', 'DienGiaiDT', 'DiemUT']
        tree.column("DoiTuongDT", width=80, anchor=tk.W)
        tree.column("DienGiaiDT", width=80, anchor=tk.W)
        tree.column("DiemUT", width=80, anchor=tk.W)
        
        

        tree.heading("DoiTuongDT", text="DoiTuongDT", anchor=tk.W)
        tree.heading("DienGiaiDT", text="DienGiaiDT", anchor=tk.W)
        tree.heading("DiemUT", text="DiemUT", anchor=tk.W)
        xem()
        tree.pack()

        lb_clock = Label(self, font=("Digital-7", 20), background="#8ddbff", foreground='black')
        lb_clock.place(x=400, y=10)
        clock()

            # Lable Information
        lb_info = tk.LabelFrame(self, padx=10, pady=15, text="Thông tin")
        lb_info.place(x=400, y=50)
        tk.Label(lb_info, text="Đối tượng dự thi").grid(row=0, column=0, sticky='W')
        tb_doiTuongDT = tk.Entry(lb_info)
        tb_doiTuongDT.grid(row=0, column=1, sticky=tk.W, padx=5, pady=5)

        tk.Label(lb_info, text="Diễn giải đối tượng").grid(row=1, column=0, sticky='W')
        tb_DienGiaiDT = ttk.Combobox(lb_info, value= chiTietDT(),width=17)
        tb_DienGiaiDT.grid(row=1, column=1, sticky=tk.W, padx=5, pady=5)

        tk.Label(lb_info, text="Điểm ưu tiên").grid(row=2, column=0, sticky='W')
        tb_DiemUT = tk.Entry(lb_info)
        tb_DiemUT.grid(row=2, column=1, sticky=tk.W, padx=5, pady=5)


            # Lable Control
        lb_control = tk.LabelFrame(self, padx=10)
        lb_control.place(x=400, y=215)

        tk.Label(lb_control, text="Xóa chi tiết đối tượng").grid(row=0, column=0, sticky='W')
        tb_xoa = tk.Entry(lb_control, width=10)
        tb_xoa.grid(row=0, column=1, sticky=tk.W, padx=10, pady=5)

        tk.Label(lb_control, text="Thêm đối tượng:").grid(row=1, column=0, sticky='W')

        btn_chen = tk.Button(lb_control, text="Thêm", width=8, height=1, command=chen)
        btn_chen.grid(row=1, column=2, padx=7)

        btn_xoa = tk.Button(lb_control, text="Xóa", width=8, height=1, command=xoa)
        btn_xoa.grid(row=0, column=2, padx=7)
class formDiemThi(tk.Toplevel):
    def __init__(self, parent):
        tk.Toplevel.__init__(self, parent)
        self.title("DiemThi")
        self.geometry("580x250")
        self.iconbitmap("HinhAnh/icons8-brief-48.ico")
        self.configure(bg='#8ddbff')
        self.resizable(False,False)
        def clock():
            string = strftime('%I:%M:%S:%p')
            lb_clock.config(text=string)
            lb_clock.after(1000, clock)


        def xem():
            tree.delete(*tree.get_children())
            connection = mysql.connect(host = host, user=user, password=password, database=database)
            cursor = connection.cursor()
            cursor.execute("select * from diemthi")
            i=0
            for row in cursor:
                tree.insert('',i,values=(row[0],row[1],row[2],row[3]))
                i=i+1
            connection.close()
            tree.pack()

        def xoa():
            SBD = tb_xoa.get()
            connection = mysql.connect(host = host, user=user, password=password, database=database)
            cursor = connection.cursor()
            cursor.execute("delete from diemthi where SBD = '"+SBD+"")
            cursor.execute("commit")
            tb_xoa.delete(0, END)
            MessageBox.showerror("Thông báo", "Xoá thành công")
            connection.close()
            xem()

        def chen():
            SBD = tb_SBD.get()
            Toan = tb_Toan.get()
            Van = tb_Van.get()
            AnhVan = tb_AnhVan.get()

            connection = mysql.connect(host = host, user=user, password=password, database=database)
            cursor = connection.cursor()
            cursor.execute("insert into diemthi(SBD,Toan,Van,AnhVan) values('"+ SBD +"','"+ Toan +"','"+ Van +"','"+ AnhVan +"')")
            cursor.execute("commit")

            tb_SBD.delete(0, END)
            tb_Toan.delete(0, END)
            tb_Van.delete(0, END)
            tb_AnhVan.delete(0, END)

            MessageBox.showinfo("Thông báo", "Thêm thành công")
            connection.close()
            xem()

        def diemThi1():
            connection = mysql.connect(host = host, user=user, password=password, database=database)
            cursor = connection.cursor()
            cursor.execute("select SBD from diemthi")
            DiemThis = cursor.fetchall()
            cursor.close()
            connection.close()
            return DiemThis

        lb_data = tk.LabelFrame(self, padx=10, pady=10, text="Bảng điểm thi")
        lb_data.place(x=10, y=10)    

        tree = ttk.Treeview(lb_data,height=8)
        tree['show'] = 'headings'
        tree["columns"] = ['SBD', 'Toan', 'Van', 'AnhVan']
        tree.column("SBD", width=100, anchor=tk.W)
        tree.column("Toan", width=100, anchor=tk.W)
        tree.column("Van", width=100, anchor=tk.W)
        tree.column("AnhVan", width=100, anchor=tk.W)

        tree.heading("SDB", text="SBD", anchor=tk.W)
        tree.heading("Toan", text="Toan", anchor=tk.W)
        tree.heading("Van", text="Van", anchor=tk.W)
        tree.heading("AnhVan", text="AnhVan", anchor=tk.W)
        xem()
        tree.pack()

        lb_clock = Label(self, font=("Digital-7", 20), background="#8ddbff", foreground='black')
        lb_clock.place(x=300, y=10)
        clock()

        # Lable Information
        lb_info = tk.LabelFrame(self, padx=10, pady=15, text="Thông tin")
        lb_info.place(x=300, y=50)

        tk.Label(lb_info, text="Số báo danh").grid(row=0, column=0, sticky='W')
        tb_SBD = tk.Entry(lb_info)
        tb_SBD.grid(row=0, column=1, sticky=tk.W, padx=5, pady=5)

        tk.Label(lb_info, text="Điểm toán").grid(row=1, column=0, sticky='W')
        tb_Toan = tk.Entry(lb_info)
        tb_Toan.grid(row=1, column=1, sticky=tk.W, padx=5, pady=5)

        tk.Label(lb_info, text="Điểm văn").grid(row=2, column=0, sticky='W')
        tb_Van = tk.Entry(lb_info)
        tb_Van.grid(row=2, column=1, sticky=tk.W, padx=5, pady=5)

        tk.Label(lb_info, text="Điểm anh văn").grid(row=3, column=0, sticky='W')
        tb_AnhVan = tk.Entry(lb_info)
        tb_AnhVan.grid(row=3, column=1, sticky=tk.W, padx=5, pady=5)

        # Lable Control
        lb_control = tk.LabelFrame(self, padx=10)
        lb_control.place(x=300, y=170)

        tk.Label(lb_control, text="Xóa điểm thi ").grid(row=0, column=0, sticky='W')
        tb_xoa = tk.Entry(lb_control, width=10)
        tb_xoa.grid(row=0, column=1, sticky=tk.W, padx=10, pady=5)

        btn_xoa = tk.Button(lb_control, text="Xóa", width=8, height=1, command=xoa)
        btn_xoa.grid(row=0, column=2, padx=7)

        btn_chen = tk.Button(lb_control, text="Thêm", width=8, height=1, command=chen)
        btn_chen.grid(row=1, column=2, padx=7)
class formTongKet(tk.Toplevel):
    def __init__(self, parent):
        tk.Toplevel.__init__(self, parent)
        self.title("Tổng kết")
        self.geometry("970x490")
        self.iconbitmap("HinhAnh/icons8-cash-in-hand-48.ico")
        self.configure(bg='#8ddbff')
        self.resizable(False,False)

        def clock():
            string = strftime('%I:%M:%S:%p')
            lb_clock.config(text=string)
            lb_clock.after(1000, clock)

        def maPB():
            connection = mysql.connect(host = host, user=user, password=password, database=database)
            cursor = connection.cursor()
            cursor.execute("select MaPB from phongban")
            MaPBs = cursor.fetchall()
            cursor.close()
            connection.close()
            return MaPBs
        def tinhLuong():
            tree.delete(*tree.get_children())
            connection = mysql.connect(host = host, user=user, password=password, database=database)
            cursor = connection.cursor()
            query="select nv.MaNV, nv.Ho, nv.Ten, nv.Phai, ct.ChucVu, ct.HSLuong*250000 as Luong, nv.MaPB from nhanvien nv, chitiet ct where nv.MaNV = ct.MaNV order by nv.MaPB"
            cursor.execute(query)
            DF_Luong = pd.DataFrame.from_records(cursor, columns=['MaNV', 'Ho', 'Ten', 'Phai', 'ChucVu', 'Luong', 'MaPB'])
            f = open("Luong/TinhLuong.txt", "w+")
            print(DF_Luong, file=f)
            f.close()

            cursor.execute(query)
            i=0
            for row in cursor:
                tree.insert('',i,values=(row[0],row[1],row[2],row[3],row[4],row[5],row[6]))
                i=i+1
            connection.close()
            tree.pack()
        def ThongKe(MaPB):
            tree_thongke.delete(*tree_thongke.get_children())
            connection = mysql.connect(host = host, user=user, password=password, database=database)
            cursor_thongke = connection.cursor()
            query = "select tong.MaPB, tong.TenPB, tong.SoNam, tong.SoNu, (tong.SoNam+tong.SoNu) as TongSo , sum(ct.HSLuong*250000) as TongLuong from nhanvien nv, chitiet ct,(select pb.MaPB, pb.TenPB, nam.SoNam, nu.SoNu, (nam.SoNam+nu.SoNu) as TongSo from phongban pb, (select MaPB, count(*) as SoNam from nhanvien where Phai = '0' group by MaPB ) nam, (select MaPB, count(*) as SoNu from nhanvien where Phai = '1' group by MaPB) nu where pb.MaPB = nam.MaPB and pb.MaPB=nu.MaPB and pb.MaPB ='"+MaPB+"' group by pb.MaPB) as tong where nv.MaNV = ct.MaNV and tong.MaPB=nv.MaPB order by nv.MaPB;"
            cursor_thongke.execute(query)
            DF_ThongKe = pd.DataFrame.from_records(cursor_thongke,columns=['MaPB','TenPB', 'SoNam', 'SoNu', 'TongSo','TongLuong'])
            f = open("Luong/TongKetLuongTheoPhongBan"+MaPB+".txt", "w+")
            print(DF_ThongKe, file=f)
            f.close()
            cursor_thongke.execute(query)
            i = 0
            for row in cursor_thongke:
                tree_thongke.insert('', i, values=(row[0], row[1], row[2], row[3],row[4], row[5]))
                i = i + 1
            connection.close()
            tree_thongke.pack()
        
        def luongTheoPhongBan():
            tree.delete(*tree.get_children())
            MaPB = cb_MaPB.get()
            connection = mysql.connect(host = host, user=user, password=password,database=database)
            cursor = connection.cursor()
            query = "select nv.MaNV, nv.Ho, nv.Ten, nv.Phai, ct.ChucVu, ct.HSLuong*250000 as Luong, nv.MaPB from nhanvien nv, chitiet ct where nv.MaNV = ct.MaNV and nv.MaPB = '"+MaPB+"'"
            cursor.execute(query)
            DF_Luong = pd.DataFrame.from_records(cursor,columns=['MaNV', 'Ho', 'Ten', 'Phai', 'ChucVu', 'Luong', 'MaPB'])
            
            f = open("Luong/LuongTheoPhongBan"+MaPB+".txt", "w+")
            print(DF_Luong, file=f)
            f.close()
            cursor.execute(query)
            i = 0
            for row in cursor:
                tree.insert('', i, values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
                i = i + 1
            connection.close()
            tree.pack()
            ThongKe(MaPB)
            

        lb_data = tk.LabelFrame(self, padx=10, pady=10, text="Bảng phòng ban")
        lb_data.place(x=10, y=10)

        tree = ttk.Treeview(lb_data, height=20)
        tree['show'] = 'headings'
        tree["columns"] = ['MaNV', 'Ho', 'Ten', 'Phai', 'ChucVu', 'Luong', 'MaPB']
        tree.column("MaNV", width=50, anchor=tk.W)
        tree.column("Ho", width=100, anchor=tk.W)
        tree.column("Ten", width=50, anchor=tk.W)
        tree.column("Phai", width=50, anchor=tk.W)
        tree.column("ChucVu", width=50, anchor=tk.W)
        tree.column("Luong", width=75, anchor=tk.W)
        tree.column("MaPB", width=50, anchor=tk.W)

        tree.heading("MaNV", text="MaNV", anchor=tk.W)
        tree.heading("Ho", text="Ho", anchor=tk.W)
        tree.heading("Ten", text="Ten", anchor=tk.W)
        tree.heading("Phai", text="Phai", anchor=tk.W)
        tree.heading("ChucVu", text="ChucVu", anchor=tk.W)
        tree.heading("Luong", text="Luong", anchor=tk.W)
        tree.heading("MaPB", text="MaPB", anchor=tk.W)
        tinhLuong()
        tree.pack()

        lb_data_thongke = tk.LabelFrame(self, padx=20, pady=5, text="Bảng thống kê")
        lb_data_thongke.place(x=480, y=175)

        tree_thongke=ttk.Treeview(lb_data_thongke, height=10)
        tree_thongke['show'] = 'headings'
        tree_thongke["columns"] = ['MaPB', 'TenPB', 'SoNam', 'SoNu', 'TongSo', 'TongLuong']
        tree_thongke.column("MaPB", width=40, anchor=tk.W)
        tree_thongke.column("TenPB", width=150, anchor=tk.W)
        tree_thongke.column("SoNam", width=50, anchor=tk.W)
        tree_thongke.column("SoNu", width=45, anchor=tk.W)
        tree_thongke.column("TongSo", width=50, anchor=tk.W)
        tree_thongke.column("TongLuong", width=70, anchor=tk.W)

        tree_thongke.heading("MaPB", text="MaPB", anchor=tk.W)
        tree_thongke.heading("TenPB", text="TenPB", anchor=tk.W)
        tree_thongke.heading("SoNam", text="SoNam", anchor=tk.W)
        tree_thongke.heading("SoNu", text="SoNu", anchor=tk.W)
        tree_thongke.heading("TongSo", text="TongSo", anchor=tk.W)
        tree_thongke.heading("TongLuong", text="TongLuong", anchor=tk.W)
        # tree_thongke.pack()


        #Label clock
        lb_clock = Label(self, font=("Digital-7", 20), background="#8ddbff", foreground='black')
        lb_clock.place(x=480, y=10)
        clock()

        # Label control
        lb_control = tk.LabelFrame(self, padx=10, pady=5, text="Chức năng")
        lb_control.place(x=480, y=60)

        tk.Label(lb_control, text="Lương nhân viên theo phòng").grid(row=2, column=0, sticky='W')
        cb_MaPB = ttk.Combobox(lb_control, values=maPB(), width=5)
        cb_MaPB.grid(row=2, column=1, sticky=tk.W, padx=6, pady=5)

        btn_LuongCaoNhatPhongBan = tk.Button(lb_control, text="Xem", command=luongTheoPhongBan, width=8, height=1,background="green", foreground="white")
        btn_LuongCaoNhatPhongBan.grid(row=0, column=1, pady=2, padx=2)




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
    def chiTietDT(self):
        chiTietDT = formChiTietDT(self)
        chiTietDT.grab_set()
    def diemThi(self):
        diemThi = formDiemThi(self)
        diemThi.grab_set()
    def xepLoai(self):
        xepLoai = formXepLoai(self)
        xepLoai.grab_set()
    def thongKe(self):
        thongKe = formThongKe(self)
        thongKe.grab_set()
    def tongKet(self):
        tongket =formTongKet(self)
        tongket.grab_set()

    def taoForm(self):
        self.other.title("Quản lý sinh viên")
        self.other.geometry("700x720")
        self.other.iconbitmap("HinhAnh/icons8-us-dollar-48.ico")
        self.configure(bg='#8ddbff')
        self.pack(fill=BOTH, expand=1)

        lb_truong = tk.Label(self, text="TRƯỜNG ĐẠI HỌC SƯ PHẠM KỸ THUẬT\n KHOA ĐÀO TẠO CHẤT LƯỢNG CAO", font=("",13), background="#8ddbff")
        lb_truong.pack(pady=10)

        self.img1 = ImageTk.PhotoImage(Image.open("HinhAnh/fhq.png"))
        panel1 = tk.Label(self, image = self.img1, background="#8ddbff")
        panel1.place(x=200, y = 80)
        self.img2 = ImageTk.PhotoImage(Image.open("HinhAnh/ute.png"))
        panel2 = tk.Label(self, image = self.img2, background="#8ddbff")
        panel2.place(x=350, y = 80)
        #Label title
        lb_title = tk.Label(self, text="Quản lý điểm thi của một kỳ thi", font=("",24), background="#8ddbff")
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
        lb_control = tk.LabelFrame(self, padx=10, pady=30, text="Chức năng",font=("", 13))
        lb_control.place(x=120, y = 440)

        tk.Label(lb_control, text="Mở 3 file ", font=("", 13)).grid(row=0, column=0, sticky='W', ipady = 10)
        tk.Label(lb_control, text="Mở trang sinh viên ",font=("", 13)).grid(row=1, column=0, sticky='W', ipady = 10)
        tk.Label(lb_control, text="Mở trang chi tiết đối tượng ",font=("", 13)).grid(row=2, column=0, sticky='W', ipady = 10)
        tk.Label(lb_control, text="Mở trang điểm thi ",font=("", 13)).grid(row=3, column=0, sticky='W', ipady = 10)
        # tk.Label(lb_control, text="        ").grid(row=3, column=3)
        tk.Label(lb_control, text="Mở trang xếp loại ",font=("", 13)).grid(row=0, column=4, sticky='W', ipady = 10)
        tk.Label(lb_control, text="Mở trang thống kê ",font=("", 13)).grid(row=1, column=4, sticky='W', ipady = 10)
        tk.Label(lb_control, text="Mở trang tổng kết ",font=("", 13)).grid(row=2, column=4, sticky='W', ipady = 10)
        # tk.Label(lb_control, text="Mở trang tổng kết ",font=("", 13)).grid(row=3, column=4, sticky='W', ipady = 10)

        Button(lb_control,text=" Mở ", command=self.moFile).grid(row=0, column=1)
        Button(lb_control, text=" Mở ",  command=self.sinhVien).grid(row=1, column=1)
        Button(lb_control,text=" Mở ", command=self.chiTietDT).grid(row=2, column=1)
        Button(lb_control,text=" Mở ", command=self.diemThi).grid(row=3, column=1)
        Button(lb_control, text=" Mở ",  command=self.xepLoai).grid(row=0, column=5)
        Button(lb_control,text=" Mở ", command=self.thongKe).grid(row=1, column=5)
        Button(lb_control,text=" Mở ", command=self.tongKet).grid(row=2, column=5)

root = Tk()
root.resizable(False, False)
formTrangChu(root)
root.mainloop()