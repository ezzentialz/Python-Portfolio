#✅ ข้อที่ 1: หาความยาวชื่อของผู้ใช้
#ให้ผู้ใช้พิมพ์ชื่อ แล้วแสดงว่า “ชื่อคุณยาวกี่ตัวอักษร”
#Hint: ใช้ input() + len()
try:
    name = input(f"please enter your name: ")
    print(f"your name is {name} has lengh: {len(name)}")
except Exception:
    print(f"please enter your name")
    
#✅ ข้อที่ 2: เปลี่ยนเลขเป็นข้อความ
#รับอายุผู้ใช้ แล้วแสดงว่า "คุณอายุ xx ปี" โดยแปลงอายุ (int) เป็น string
#Hint: ใช้ str() + input()
age = str(input(f"what is your age: "))
print(f"your age is: {age} and {age} is: {type(age)}")

#✅ ข้อที่ 3: หาค่ามากสุด
#ให้ผู้ใช้พิมพ์เลข 3 ตัว แล้วหาว่าค่ามากสุดคือเท่าไร
#Hint: ใช้ max()
try:
    a = input(f"please enter first number: ")
    b = input(f"please enter second number: ")
    c = input(f"please enter third number: ")
    numbers = [a, b, c]
    print(f"the max number is: {max(numbers)}")
except Exception:
    print(f"{Exception}")   
    
#✅ ข้อที่ 4: ปัดเศษทศนิยม
#รับค่าทศนิยม แล้วปัดเศษให้เหลือ 2 ตำแหน่ง
#Hint: ใช้ round()
try:
    float_number = float(input(f"please enter any numbers"))
    calc = 22/7 * float_number **2
    print(f"the result for Circle area is {round(calc, 2)}")
except Exception:
    print(f"Really? numbers")
    
#✅ ข้อที่ 5: หาค่าสัมบูรณ์
#รับเลขจำนวนเต็มจากผู้ใช้ แล้วแสดงค่าสัมบูรณ์
#Hint: ใช้ abs()
try:
    number = float(input(f"please enter any number: "))
    print(f"{abs(number)}")
except Exception:
    print(f"{Exception}")    
    
#✅ ข้อที่ 6: รวมค่าทั้งหมดใน list
#สร้าง list ของคะแนน เช่น [70, 80, 90] แล้วหาผลรวม
#Hint: ใช้ sum()
try:
    list_score = [70, 80, 90]
    total = sum(list_score)
    print(f"the list score: {list_score} and the total score: {total}")
except Exception:
    print(f"{Exception}")  
    
#✅ ข้อที่ 7: แปลงข้อความเป็น list ของตัวอักษร
#รับข้อความ เช่น "banana" แล้วแปลงเป็น list
#Hint: ใช้ list()
try:
    item_list = input(f"what is your favorite food: ")
    print(list(item_list))
except Exception:
    print(f"{Exception}")  

#✅ ข้อที่ 8: เรียง list จากน้อยไปมาก
#ให้ list ของตัวเลข แล้วเรียงจากน้อยไปมาก
#Hint: ใช้ sorted()
try:
    number_list = [2,1,6,8,9,7,5]
    print(f"this is number in the list: {number_list}")
    print(f"and here is when we sort the number {sorted(number_list)}")
except Exception:
    print(f"{Exception}") 
    
#✅ ข้อที่ 9: กลับลำดับ list
#เช่น [1, 2, 3] → [3, 2, 1]
#Hint: ใช้ reversed() + list()
try:
    number_list = [2,1,6,8,9,7,5]
    revers_list = reversed(number_list)
    print(f"this is number in the list: {number_list}")
    print(f"and here is when we sort the number {sorted(number_list)}")
    print(f"and reversed list {list(reversed(sorted(number_list)))}")
except Exception:
    print(f"{Exception}") 

#✅ ข้อที่ 10: ตรวจว่าค่าที่รับมาคือ int หรือไม่
#รับค่าจาก input() แล้วตรวจว่าเป็น int หรือไม่
#Hint: ใช้ isinstance()

try:
    number_input = int(input(f"if you in put number: "))
    print(f"it will show you that this is integer: {isinstance(number_input, int)}")
    
except Exception:
    print(f"{Exception}") 