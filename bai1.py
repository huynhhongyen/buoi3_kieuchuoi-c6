# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 14:59:59 2024

@author: ASUS
"""


chuoi = "Đại học Quốc gia, Khu phố 6, P. Linh Trung, Q. Thủ Đức, Tp. HCM"
chuoi1 = chuoi.split(', ')
print('1.',chuoi1)

chuoi2 = chuoi.replace("P. ",'').replace("Q. ",'').replace("Tp. ",'')
chuoi3 = chuoi2.split(', ')
print('\n2.',chuoi3) 