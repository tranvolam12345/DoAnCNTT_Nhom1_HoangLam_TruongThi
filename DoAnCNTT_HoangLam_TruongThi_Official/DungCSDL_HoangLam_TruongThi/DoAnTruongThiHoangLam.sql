Create database doancnttthiquachhoanglam;
use doancnttthiquachhoanglam;
  DROP TABLE IF EXISTS `diemthi`;
    DROP TABLE IF EXISTS `sinhvien`;
      DROP TABLE IF EXISTS `chitietdt`;
      INSERT INTO `chitietdt` VALUES (1,'Doi tuong thuoc dien chinh sach',2),(2,'Can bo, cong nhan vien chuc nha nuoc',1),(3,'Hoc sinh pho thong',0);
#INSERT INTO `sinhvien` VALUES (1,'Nguyen Viet','Hong','0', '04/04/1981',3),('2','Nguyen Hong','Lanh','1', '15/03/1982','1'),('3',' Nguyen Minh','Quang','0', '10/07/1982 ','3'),('4','Dinh Thi','Tam','1', '18/02/1982','1'),('5','Nguyen Hoai','Anh','1', '21/08/1982','3'),('6','Dang Bich','Thuy','1', '22/10/1982','1'),('7','Hoang Thanh','Trang','1', '12/08/1982','3'),('8','Tran Cat','Dung','1', '04/12/1981','3'),('9','Pham Hoai','Bong','0', '11/10/1980','3'),('10','Tran Minh','Nguyet','1', '07/12/1981','1'),('11','Ma Thi Hong','Xuan','1', '19/10/1981','3'),('12','Le Thao','Dung','1', '03/11/1982','1'),('13','Luu Phuong','Thanh','1', '25/02/1982','1'),('14','Pham','Thanh','0', '03/07/1981','1'),('15','Pham Thu','Thuy','1', '04/12/1981','1'),('16','Dang Dinh','Tam','0', '24/11/1981','1'),('17','Tong Duc','Cuong','0', '25/06/1982','1'),('18','Tran Thu','Nga','1', '14/09/1981','1'),('19','Tran Thi Thanh','Giang','1', '18/03/1982','1'),('20','Truong Thi','My','1', '16/08/1982','1'),('21','Nguyen Thi','Hoa','1', '27/11/1982','1'),('22','Ha Son','Tri','0', '27/08/1981','1'),('23','Tang My','Hanh','1', '28/10/1980','1'),('24','Tran Thi','Tam','1', '22/02/1982','1'),('25','Pham Thi','Lua','1', '24/07/1981','1'),('26','Huynh Bach','Cuc','1', '21/09/1980','2'),('27','Nguyen Thi','Tuyet','1', '20/12/1981','1'),('28','Vu Thi','No','1', '02/04/1982','1'),('29','Tran My','Dung','1', '12/01/1982','2'),('30','Truong Minh','Thang','0', '26/02/1982','2'),('31','Le Kim','Thoa','1', '01/04/1982','1'),('32','Huynh Thanh','Nga','1', '07/12/1980','2'),('33','Tran Thi','Loan','1', '25/11/1981','1'),('34','Tran Thi','Nhi','1', '18/11/1982','1'),('35','Lam Ngoc','Quan','0', '28/08/1981','2'),('36','Nguyen Ngoc','Bich','1', '26/08/1981','1'),('37','Vuong Kim','Anh','1', '18/04/1982','2'),('38','Nguyen Thu','Van','1', '16/09/1982','1'),('39','Phan Mai','Phuong','1', '11/07/1981','1'),('40','Pham Thi','Thu','1', '26/01/1982','2'),('41','Nguyen Thi','Dung','1', '25/11/1982','1'),('42','Doan Thuy','Trang','1', '19/11/1982','3'),('43','Hoang Van','Hoa','0', '10/01/1982','2'),('44','Nguyen Van','Tien','0', '07/10/1981','1'),('45','Du Thi Lieu','Dung','1', '17/06/1982','2'),('46','Vu Kieu','Oanh','1', '09/03/1982','2'),('47','Nguyen Trong','Nghiep','0', '20/07/1981','2'),('48','Nguyen Thuy','Huong','2', '24/23/1981','2'),('49','Bui Van','Hung','0', '25/08/1981','1'),('50','Ly Cong','Duy','0', '14/02/1982','2'),('51','Le Thi','Ly','1', '28/05/1981','2'),('52','Nguyen Lien','Phuong','1', '17/09/1982','1'),('53','Hoang Thi','Thuan','1', '25/10/1981','2'),('54','To Phuong','Lan','1', '10/10/1982','1'),('55','Tran Thi','Phuong','1', '17/09/1982','1'),('53','Hoang Thi','Thuan','1', '25/10/1981','2'),('54','To Phuong','Lan','1', '10/10/1982','1'),('55','Tran Thi','Phuong','1', '10/04/1981','2'),('56','Nguyen Dong','Lan','1', '29/07/1982','2'),('57','Nguyen Van','Toan','0', '09/06/1982','1'),('58','Diep Thuy','Phuong','1', '13/12/1981','2'),('59','Dao Thi','Tue','1', '23/12/1982','1'),('60','Tran Thi','Phan','1', '24/01/1982','2'),('61','Tran Thi','Thuy','1', '08/11/1982','3'),('62','Nguyen Mong','Kieu','1', '23/08/1982','2'),('63','Duong Thi','Tuoi','1', '24/12/1981','3'),('64',' Nguyen Viet',' Hong','0', '04/04/1981','3'),('65','Nguyen Thi','Le','1', '21/06/1982','3'),('66','Nguyen Thi','Hanh','1', '19/01/1981','3'),('67','Nguyen Van','Tam','0', '02/07/1982','3'),('68','Lam Ngoc','Phuoc','0', '17/02/1981','1'),('69','Phan Kim','Nga','1', '24/08/1982','3'),('70','Huynh Thi','Huong','1', '19/05/1981','1'),('71','Nguyen Van','Dung','0', '17/12/1981','3'),('72','Nguyen Van','Dung','0', '17/12/1981','3'),('73','Tran Tham','Tuoi','1', '04/02/1982','1'),('74','Duong Cong','Bang','0', '27/06/1981','1'),('75','Le Trung','Kien','0', '09/02/1981','1'),('76','Nguyen Van','Nghiep','0', '14/09/1982','1'),('77','Nguyen Van','Minh','0', '07/02/1981','1'),('78','Ho Duong','Thanh','0', '09/11/1981','1'),('79','Quach Kieu','Mai','1', '17/02/1982','1'),('80','Dao Thi','Phuong','1', '29/03/1982','1'),('81','Tran Thi Ngoc','Han','1', '26/07/1982','3'),('82','Tran Tuyet','Anh','1', '12/06/1982','2'),('83',' Nguyen Cam','Huong','1', '02/03/1981','3'),('84','Nguyen Ngoc','Suong','1', '11/09/1981','3'),('84','Nguyen Ngoc','Suong','1', '11/09/1981','3'),('84','Nguyen Ngoc','Suong','1', '11/09/1981','3'),('84','Nguyen Ngoc','Suong','1', '11/09/1981','3'),('84','Nguyen Ngoc','Suong','1', '11/09/1981','3'),('85','Nguyen Van','Loi','0', '02/02/1982','1'),('86','Nguyen Duc','Thang','0', '24/05/1981','1'),('87','Bui Thi','Hue','1', '19/12/1981','1'),('88','Pham Thi','Mai','1', '22/08/1981','1'),('89','Nguyen Thi','Huong','1', '30/11/1981','1'),('90','Pham Van','Trang','0', '06/05/1981','1'),('91','Tran Thuy','Tien','1', '27/11/1980','2'),('92','Nguyen Minh','Dan','0', '11/12/1982','3'),('93','Do Thi','Thao','1', '18/10/1980','2'),('94','Phan Thi','Anh','1', '13/07/1981','3'),('95','Dang Kim','Anh','1', '13/07/1981','3'),('96','Le Tien','Dat','0', '01/12/1982','3'),('97','Pham Hong','Tuyet','1', '05/10/1981','2'),('98','Pham Thi','Chien','1', '29/10/1981','3'),('99','Nguyen Thi','Binh','1', '09/12/1982','2'),('100','Tran Van','Viet','0', '15/07/1982','2'),('101','Nguyen Bui','Hoa','0', '18/02/1981','3'),('102','Ho Cam','Ly','1', '30/08/1982','2'),('103','Huynh Van','Khoa','0', '17/04/1981','3'),('104','Huynh Minh','Hieu','1', '18/04/1982','2'),('105','Huynh Thanh','Viet','0', '02/02/1981','3'),('106','Le Hong','Nhung','1', '01/12/1981','2'),('107','Nguyen Thi','Van','1', '22/02/1982','3'),('108','Tran Van','Quang','0', '24/09/1981','2'),('109','Dang Minh','Quan','0', '17/02/1982','1'),('110','Le Thanh','Khoa','0', '28/07/1981','2'),('111','Nguyen Thi','Tai','0', '22/08/1981','2'),('112','Do Thi','Thuy','1', '17/08/1982','2'),('113','Vu Van','An','0', '31/01/1982','2'),('114','Nguyen Van','Thanh','0', '13/11/1981','1'),('115','Bui Van','Thanh','0', '12/08/1982','2'),('116','Truong Kieu','Oanh','1', '14/09/1982','2'),('118','Tran My','Thanh','1', '07/10/1981','1'),('119','Pham Van','Hoang','0', '27/10/1982','1'),('120','Nguyen Thi','Nhung','1', '31/10/1981','2'),('121','Nguyen Thi','Lan','1', '12/11/1980','2'),('122','Nguyen Hong','Hoa','1', '14/12/1981','1'),('123','Tran Van','Phuong','0', '16/10/1982','2'),('124','Nguyen Ngoc','Suong','1', '11/09/1981','3'),('125','Vo Quoc','Vuong','0', '29/09/1982','2'),('126','Nguyen Thanh','Trung','0', '07/12/1982','1'),('127','Nguyen Thi','Thao','1', '30/01/1981','1'),('128','Vo Kim','Yen','1', '16/12/1981','2'),('129','Tran Van','Son','0', '09/05/1981','2'),('130','Nguyen Van','Hai','0', '24/03/1982','1'),('131','Nguyen Thanh','Lam','0', '24/03/1982','1'),('132','Pham Lan','Anh','0', '06/10/1981','2'),('133','Nguyen Van','Doan','0', '15/10/1981','1'),('134','Le Hong','Hoa','1', '16/12/1981','2'),('135','Nguyen Van','Ngan','0', '06/08/1981','1'),('136','Nguyen Ngoc','Suong','1', '11/09/1981','3'),('136','Nguyen Ngoc','Suong','1', '11/09/1981','3'),('136','Pham Hong','Chung','0', '19/05/1981','2'),('137','Nguyen Hong','Hoa','1', '06/09/1981','1'),('138','Le Hong','Hanh','1', '16/12/1981','1'),('139','Le Anh','Thu','1', '31/01/1981','1'),('140','Tran Le','Nga','1', '27/11/1980','1'),('141','Nguyen Thi','Huong','1', '04/04/1981','3'),('142','Vuong Cong','Hon','0', '18/09/1981','3'),('143','Ta Ngoc','Dieu','0', '14/08/1981','3'),('144','Nguyen Duc','Hien','0', '19/04/1982','3'),('145','Nguyen Thanh','Hai','0', '07/12/1981','1'),('146','Mai Ngoc','Bich','1', '08/10/1981','1'),('147','Dao Thanh','Xuan','0', '30/12/1980','2'),('148','Pham Thu','Han','1', '04/12/1982','2'),('149','Pham Huy','Hung','0', '03/02/1981','1'),('150','Dao Minh','Than','0', '21/04/1982','1'),('151','Nguyen Phuoc','Lam','0', '05/11/1980','2'),('152','Le Van','Dung','0', '03/12/1981','2'),('153','Tran Viet','Hong','0', '07/04/1982','1'),('154','Nguyen Thanh','Hao','0', '20/07/1982','2'),('155','Nguyen Kim','Loan','1', '19/02/1981','1'),('156','Nguyen Con','Truong','0', '11/08/1982','1'),
INSERT INTO `sinhvien` VALUES (1, 'Nguyen Viet', 'Hong', 0, '1981-04-04', 3),
                 (2, 'Nguyen Hong', 'Lanh', 1, '1982-03-15', 1),
                 (3, 'Nguyen Minh', 'Quang', 0, '1982-07-10', 3),
                 (4, 'Dinh Thi', 'Tam', 1, '1982-02-18', 1),
                 (5, 'Nguyen Hoai', 'Anh', 1, '1982-08-21', 3),
                 (6, 'Dang Bich', 'Thuy', 1, '1982-10-22', 1),
                 (7, 'Hoang Thanh', 'Trang', 1, '1982-08-12', 3),
                 (8, 'Tran Cat', 'Dung', 1, '1981-12-04', 3),
                 (9, 'Pham Hoai', 'Bong', 0, '1980-10-11', 3),
                 (10, 'Tran Minh', 'Nguyet', 1, '1981-12-07', 1),
                 (11, 'Ma Thi Hong', 'Xuan', 1, '1981-10-19', 3),
                 (12, 'Le Thao', 'Dung', 1, '1982-11-03', 1),
                 (13, 'Luu Phuong', 'Thanh', 1, '1982-02-25', 1),
                 (14, 'Phan', 'Thanh', 0, '1981-07-03', 1),
                 (15, 'Pham Thu', 'Thuy', 1, '1981-12-04', 1),
                 (16, 'Dang Dinh', 'Tam', 0, '1981-11-24', 1),
                 (17, 'Tong Duc', 'Cuong', 0, '1982-06-25', 1),
                 (18, 'Tran Thu', 'Nga', 1, '1981-09-14', 1),
                 (19, 'Tran Thi Thanh', 'Giang', 1, '1982-03-18', 1),
                 (20, 'Truong Thi', 'My', 1, '1982-08-16', 1),
                 (21, 'Nguyen Thi', 'Hoa', 1, '1982-11-27', 1),
                 (22, 'Ha Son', 'Tri', 0, '1981-08-27', 1),
                 (23, 'Tang My', 'Hanh', 1, '1980-10-28', 1),
                 (24, 'Tran Thi', 'Tam', 1, '1982-02-22', 1),
                 (25, 'Pham Thi', 'Lua', 1, '1981-07-24', 1),
                 (26, 'Huynh Bach', 'Cuc', 1, '1980-09-21', 2),
                 (27, 'Nguyen Thi', 'Tuyet', 1, '1981-12-20', 1),
                 (28, 'Vu Thi', 'No', 1, '1982-04-02', 1),
                 (29, 'Tran My', 'Dung', 1, '1982-01-12', 2),
                 (30, 'Truong Minh', 'Thang', 0, '1982-02-26', 2),
                 (31, 'Le Kim', 'Thoa', 1, '1982-04-01', 1),
                 (32, 'Huynh Thanh', 'Nga', 1, '1980-12-07', 2),
                 (33, 'Tran Thi', 'Loan', 1, '1981-11-25', 1),
                 (34, 'Tran Thi', 'Nhi', 1, '1982-11-18', 1),
                 (35, 'Lam Ngoc', 'Quan', 0, '1981-08-28', 2),
                 (36, 'Nguyen Ngoc', 'Bich', 1, '1981-08-26', 1),
                 (37, 'Vuong Kim', 'Anh', 1, '1982-04-18', 2),
                 (38, 'Nguyen Thu', 'Van', 1, '1982-09-16', 1),
                 (39, 'Phan Mai', 'Phuong', 1, '1981-07-11', 1),
                 (40, 'Pham Thi', 'Thu', 1, '1982-01-26', 2),
                 (41, 'Nguyen Thi', 'Dung', 1, '1982-11-25', 1),
                 (42, 'Doan Thuy', 'Trang', 1, '1982-11-19', 2),
                 (43, 'Hoang Van', 'Hoa', 0, '1982-01-10', 2),
                 (44, 'Nguyen Van', 'Tien', 1, '1981-10-07', 1),
                 (45, 'Du Thi Lieu', 'Dung', 0, '1982-06-17', 2),
                 (46, 'Vu Kieu', 'Oanh', 1, '1982-03-09', 2),
                 (47, 'Nguyen Trong', 'Nghiep', 0, '1981-07-20', 2),
                 (48, 'Nguyen Thuy', 'Huong', 1, '1981-12-14', 1),
                 (49, 'Bui Van', 'Hung', 0, '1981-08-25', 1),
                 (50, 'Ly Cong', 'Duy', 0, '1982-02-14', 2),
                 (51,         'Le Thi',         'Ly',     1, '981-05-28', 2),
                 (52,         'Nguyen Lien',    'Phuong', 1, '1982-09-17', 1),
                 (53,         'Hoang Thi',      'Thuan',  1, '1981-10-25', 2),
                 (54,         'To Phuong',      'Lan',    1, '1982-10-10', 1),
                 (55,         'Tran Thi',       'Phuong', 1, '1981-04-10', 2),
                 (56,         'Nguyen Dong',    'Lan',    1, '1982-07-29', 2),
                 (57,         'Nguyen Van',     'Toan',   0, '1982-06-09', 1),
                 (58,         'Diep Thuy',      'Phuong', 1, '1981-12-13', 2),
                 (59,         'Dao Thi',        'Tue',    1, '1982-12-23', 1),
                 (60,         'Tran Thi',       'Phan',   1, '1982-01-24', 2),
                 (61,         'Tran Thi',       'Thuy',   1, '1982-11-08', 3),
                 (62,         'Nguyen Mong',    'Kieu',   1, '1982-08-23', 2),
                 (63,         'Duong Thi',      'Tuoi',   1, '1981-12-24', 3),
                 (64,         'Nguyen Thi',     'Thuy',   1, '1982-01-05', 2),
                 (65,         'Nguyen Thi',    'Le',     1, '1982-06-21', 3),
                 (66,        'Nguyen Thi',     'Hanh',   1, '1981-01-19', 3),
                 (67,         'Nguyen Van',     'Tam',    0, '1982-07-02', 3),
                 (68,        'Lam Ngoc',       'Phuoc',  0, '1981-02-17', 1),
                 (69,         'Phan Kim',       'Nga',    1, '1982-08-24', 3),
                 (70,         'Huynh Thi',      'Huong',  1, '1981-05-19', 1),
                 (71,         'Nguyen Thu',     'Ha',     1, '1982-04-03', 1),
                 (72,        'Nguyen Van',     'Dung',   0, '1981-12-17', 3),
                 (73,         'Tran Tham',      'Tuoi',   1, '1982-02-4', 1),
                 (74,         'Duong Cong',     'Bang',  0, '1981-06-27', 1 ),
                 (75,         'Le Trung',       'Kien',   0, '1982-02-09', 1),
                 (76,         'Nguyen Van',     'Nghiep', 0, '1982-09-14', 1),
                 (77,         'Nguyen Van',     'Minh',   0, '1981-02-07', 1),
                 (78,         'Ho Duong',       'Thanh',  0, '1981-11-09', 1),
                 (79,         'Quach Kieu',     'Mai',    1, '1982-02-17', 1),
                 (80,         'Dao Thi',        'Phuong', 1, '1982-03-29', 1),
                 (81,         'Tran Thi Ngoc',  'Han',    1, '1982-07-26', 3),
                 (82,         'Tran Tuyet',     'Anh',    1, '1982-06-12', 2),
                 (83,         'Nguyen Cam',     'Huong',  1, '1981-02-03', 3),
                 (84,         'Nguyen Ngoc',    'Suong',  1, '1981-09-11', 3),
                 (85,        'Nguyen Van',     'Loi',    0, '1982-02-02', 1),
                 (86,         'Nguyen Duc',     'Thang',  0, '1981-06-24', 1),
                 (87,         'Bui Thi',        'Hue',    1, '981-12-19', 1),
                 (88,         'Pham Thi',       'Mai',    1, '1981-08-22', 1),
                 (89,         'Nguyen Thi',     'Huong',  1, '1981-11-30', 1),
                 (90,         'Pham Van',       'Trang',  0, '1981-05-06', 1),
				 (91,         'Tran Thuy',      'Tien',   1, '1980-11-27', 2),
                 (92,         'Nguyen Minh',    'Dan',    0, '1982-12-11', 3),
                 (93,         'Do Thi',         'Thao',   1, '1980-10-18', 2),
                 (94,         'Phan Thi',       'Anh',    1, '1981-07-13', 3),
                 (95,         'Dang Kim',       'Anh',    1, '1981-10-18', 2),
                 (96,         'Le Tien',        'Dat',    0, '1982-12-01', 3),
                 (97,        'Pham Hong',     'Tuyet',  1, '1981-10-05', 2),
                 (98,         'Pham Thi',       'Chien',  1, '1981-10-29', 3),
                 (99,         'Nguyen Thi',     'Binh',   1, '1982-12-09', 2),
                 (100,        'Tran Van',       'Viet',   0, '1982-07-15', 2),
                 (101,        'Nguyen Bui',     'Hoa',    0, '1981-02-18', 3),
                 (102,        'Ho Cam',        'Ly',     1, '1982-08-30', 2),
                 (103,        'Huynh Van',      'Khoa',   0, '1981-04-17', 3),
                 (104,        'Huynh Minh',     'Hieu',   1, '1982-04-18', 2),
                 (105,        'Huynh Thanh',    'Viet',   0, '1981-02-02', 3),
                 (106,        'Le Hong',        'Nhung',  1, '1981-12-01', 2),
                 (107,        'Nguyen Thi',     'Van',    1, '1982-02-22', 3),
                 (108,        'Tran Van',       'Quang',  0, '1981-09-24', 2),
                 (109,        'Dang Minh',      'Quan',   0, '1982-02-17', 1),
                 (110,        'Le Thanh',       'Khoa',   0, '1981-07-28', 2),
                 (111,        'Nguyen Tan',     'Tai',    0, '1981-08-22', 2),
                 (112,        'Do Thi',         'Thuy',   1, '1982-08-17', 2),
                 (113,        'Vu Van',         'An',     0, '1982-01-31', 2),
                 (114,       'Nguyen Van',    'Thanh',  0, '1981-11-13',1),
                 (115,        'Bui Van',        'Thanh',  0, '1982-08-12', 2),
                 (116,       'Do Phuong',      'Nam',    0, '1982-01-01', 1),
                 (117,        'Truong Kieu',    'Oanh',   1, '1982-09-14', 2),
                 (118,        'Tran My',        'Thanh',  1, '1981-10-07', 1),
                 (119,        'Pham Van',       'Hoang',  0, '1982-10-27', 1),
                 (120,        'Nguyen Thi',     'Nhung',  1, '1981-10-31', 2),
                 (121,        'Nguyen Thi',    'Lan',    1, '1980-11-12', 2),
                 (122,        'Nguyen Hong',    'Hoa',    1, '1981-12-14', 1),
                 (123,        'Tran Van',       'Phuong', 0, '1982-10-16', 2),
                 (124,        'Tran Van',       'Minh',   0, '1982-07-11', 1),
                 (125,        'Vo Quoc',        'Vuong',  0, '1982-09-29', 2),
                 (126,        'Nguyen Thanh',   'Trung',  0, '1982-12-07', 1),
                 (127,        'Nguyen Thi',     'Thao',   1, '1981-01-30', 1),
                 (128,        'Vo Kim',         'Yen',    1, '1981-12-16', 2),
                 (129,        'Tran Van',       'Son',    0, '1981-07-20', 2),
                 (130,        'Nguyen Van',     'Hai',    0, '1981-05-09', 2),
                 (131,        'Nguyen Thanh',   'Lam',    0, '1982-03-24', 1),
                 (132,        'Pham Lan',       'Anh',    1, '1981-10-06', 2),
                 (133,        'Nguyen Van',     'Doan',   0, '1981-10-15', 1),
                 (134,        'Le Hong',        'Hoa',    1, '1981-12-16', 2),
                 (135,        'Nguyen Van',     'Ngan',   0, '1981-08-06', 1),
                 (136,        'Pham Hong',      'Chung',  0, '1981-05-19', 2),
                 (137,        'Nguyen Hong',    'Hoa',    1, '1981-09-06', 1),
                 (138,        'Le Hong',        'Hanh',   1, '1981-12-16', 1),
                 (139,        'Le Anh',         'Thu',    1, '1981-01-31', 1),
                 (140,        'Tran Le',        'Nga',    1, '1980-11-27', 1),
                 (141,        'Nguyen Thi',     'Huong',  1, '1981-04-04', 3),
                 (142,        'Vuong Cong',     'Hon',    0, '1981-09-18', 3),
                 (143,        'Ta Ngoc',        'Dieu',   0, '1981-08-14', 3),
                 (144,        'Nguyen Duc',     'Hien',   0, '1982-04-19', 3),
                 (145,        'Nguyen Thanh',   'Hai',    0, '1981-12-07', 1),
                 (146,        'Dao Thanh',      'Xuan',   0, '1980-12-30', 2),
                 (147,        'Mai Ngoc',       'Bich',   1, '1981-10-08', 1),
                 (148,        'Pham Thu',       'Han',    1, '1982-12-04', 2),
                 (149,        'Phan Huy',       'Hung',   0, '1981-02-03', 1),
                 (150,        'Nguyen Phuoc',   'Lam',   0, '1980-11-05', 2),
                 (151,        'Dao Minh',       'Than',   0, '1982-04-21', 1),
                 (152,        'Le Van',         'Dung',   0, '1981-12-03', 2),
                 (153,        'Tran Viet',      'Hong',   0, '1982-04-07', 1),
                 (154,        'Nguyen Thanh',   'Hao',    0, '1982-07-20', 2),
                 (155,        'Nguyen Kim',     'Loan',   1, '1981-02-19', 1),
                 (156,        'Nguyen Cong',    'Truong', 0, '1982-08-11', 1);
INSERT INTO `diemthi` VALUES(1,          8.00,         5.00,         8.00),
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
                (156,        4.00,         7.50,         5.00);
INSERT INTO `chitietdt` VALUES (1,'Doi tuong thuoc dien chinh sach',2),
(2,'Can bo, cong nhan vien chuc nha nuoc',1),
(3,'Hoc sinh pho thong',0);

                 
  CREATE TABLE `sinhvien` (
  `SBD` int NOT NULL,
  `Ho` varchar(45) NOT NULL,
  `Ten` varchar(45) NOT NULL,
  `Phai` tinyint DEFAULT NULL,
  `NgaySinh` date NOT NULL,
  `DTDT` int NOT NULL,
  PRIMARY KEY (`SBD`),
    CONSTRAINT `SBD` FOREIGN KEY (`SBD`) REFERENCES `diemthi` (`SBD`) ON DELETE CASCADE
  );
    CREATE TABLE `diemthi` (
   `SBD` int NOT NULL,
  `Toan`double NOT NULL,
  `Van` double NOT NULL,
  `AnhVan` double NOT NULL,
  PRIMARY KEY (`SBD`),
     CONSTRAINT `SBD` FOREIGN KEY (`SBD`) REFERENCES `sinhvien` (`SBD`)  
  );
  create table `chitietdt` (
  `DoiTuongDT` int NOT NULL,
  `DienGiaiDT` varchar(45) NOT NULL,
  `DiemUT` int NOT NULL,
  PRIMARY KEY (`DoiTuongDT`),
 CONSTRAINT `DoiTuongDT` FOREIGN KEY (`DoiTuongDT`) REFERENCES `sinhvien` (`DTDT`)
  );