#function formate string
name="got"
print(name.upper())
print(name.lower())

#บอกเพศผู้ใช้
name1=input("กรุณาป้อนชื่อ พร้อมคำนำหน้าชื่อ")
if name1.startswith("นาย") :
    print("เพศชาย")
elif name1.startswith("นางสาว"):
    print("เพศหญิง")
