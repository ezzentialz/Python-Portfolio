#Module - คือการเรียกใช้คำสั่ง ที่อยู่ในโปรเจ็คแยก moduleshape.py มาใช้งาน
import moduleshape as m   #โดยคำสั่งเรียกใช้ module คือ import ตามด้วย(ชื่อโปรเจ็ค) as ตรงนี้ใช้เพื่อย่อคำว่า moduleshape ให้สั้นลงเพื่อเรียกใช้เป็นชื่อสั้นๆ

#ตัวอย่างที่ 1 - หาพื้นที่ วงกลม
circle = m.get_circle_area(5)  #สร้างคำสั่ง จากนั้น กำหนดpathของmoduleตามด้วยจุด (moduleshape. หรือ m. )ตามด้วยfunctionที่จะเรียกใช้ และค่าที่ต้องการ
print(circle) #จากนั้นใช้คำสั่ง แสดลงผล

#ตัวอย่างที่ 2 - หาพื้นที่ สามเหลี่ยม
triangle = m.get_triangle_area(6, 7) #สร้างคำสั่ง = (path. + function name + (ค่าที่ต้องการ))
print(triangle) #แสดงผลลัพธ์

#ตัวอย่างที่ 3 - หาพื้นที่ สี่เหลี่ยมผืนผ้า
rectangle = m.get_rectangle_area(10, 3)
print(rectangle)