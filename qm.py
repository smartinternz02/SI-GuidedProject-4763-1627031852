import pyqrcode
import cv2
data="mobilephones"
data1="tablets"
data2="headphones"
data3="smartwatches"
data4="speakers"
data5="laptops"
data6="accessories"
data7="earphones"
data8="Smart TV"
data9="cameras"
data10="Home Theatre"


my_QR =pyqrcode.create(data)
my_QR1 =pyqrcode.create(data1)
my_QR2 =pyqrcode.create(data2)
my_QR3 =pyqrcode.create(data3)
my_QR4=pyqrcode.create(data4)
my_QR5 =pyqrcode.create(data5)
my_QR6 =pyqrcode.create(data6)
my_QR7 =pyqrcode.create(data7)
my_QR8 =pyqrcode.create(data8)
my_QR9 =pyqrcode.create(data9)
my_QR10 =pyqrcode.create(data10)

my_QR.png("QR.png", scale="10")
my_QR1.png("QR1.png", scale="10")
my_QR2.png("QR2.png", scale="10")
my_QR3.png("QR3.png", scale="10")
my_QR4.png("QR4.png", scale="10")
my_QR5.png("QR5.png", scale="10")
my_QR6.png("QR6.png", scale="10")
my_QR7.png("QR7.png", scale="10")
my_QR8.png("QR8.png", scale="10")
my_QR9.png("QR9.png", scale="10")
my_QR10.png("QR10.png", scale="10")


s=cv2.imread('QR.png')
s1=cv2.imread('QR1.png')
s2=cv2.imread('QR2.png')
s3=cv2.imread('QR3.png')
s4=cv2.imread('QR4.png')
s5=cv2.imread('QR5.png')
s6=cv2.imread('QR6.png')
s7=cv2.imread('QR6.png')
s8=cv2.imread('QR6.png')
s9=cv2.imread('QR6.png')
s10=cv2.imread('QR6.png')
d=cv2.QRCodeDetector()
data, bbox, straight_qrcode = d.detectAndDecode(s)
data, bbox, straight_qrcode = d.detectAndDecode(s1)
data, bbox, straight_qrcode = d.detectAndDecode(s2)
data, bbox, straight_qrcode = d.detectAndDecode(s3)
data, bbox, straight_qrcode = d.detectAndDecode(s4)
data, bbox, straight_qrcode = d.detectAndDecode(s5)
data, bbox, straight_qrcode = d.detectAndDecode(s6)
data, bbox, straight_qrcode = d.detectAndDecode(s7)
data, bbox, straight_qrcode = d.detectAndDecode(s8)
data, bbox, straight_qrcode = d.detectAndDecode(s9)
data, bbox, straight_qrcode = d.detectAndDecode(s10)

print(d)
if bbox is not None:
 print(data)
