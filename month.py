month=input("ป้อนเดือน")

if month.endswith("คม") :
    print("เดือนนี้มี 31 วัน")
elif month.endswith("ยน"):
    print("เดือนนี้มี 30 วัน")
else : print("เดือนนี้เป็นเดือนกุมภาพันธ์")