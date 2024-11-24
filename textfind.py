#หา text ในประโยค
text= "Hello Python"
print(text.count("Hello"))

text1= "สัญญาจ้างงานประจำปี 2567 มีผลตั้งแต่ มกราคม 2567 ถึง ธันวาคม 2567"
update= text1.replace("2567","2568")
print(update)

text2= "  Python  ".strip() #เป็นการลบช่องวางซ้ายขวา
print(len(text2))

text3= "ฉันชื่อ {0} อายุ {1} ปี".format("got",31)
print(text3)