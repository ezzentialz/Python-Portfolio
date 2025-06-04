'''# เขียนโปรแกรมพิมพ์ตัวเลข 1 ถึง 10 ทีละบรรทัด
#ใช้ for i in range(...)
for i in range(1, 11):
    print(i)


#2. เขียนฟังก์ชัน sum_odd(n)
#คืนผลรวมของเลขคี่ตั้งแต่ 1 ถึง n
#เช่น sum_odd(10) → 1+3+5+7+9 = 25
def sum_odd(n):
    total = 0
    
    for i in range(1, n+1):
        if i % 2 != 0:
            total += i
    return total 
    
print(sum_odd(10))   
     
#3.ให้รับตัวเลขจากผู้ใช้ แล้วพิมพ์ตารางสูตรคูณของตัวเลขนั้น
#เช่น พิมพ์ 5 แล้วได้

num = int(input(f"please enter number: "))

for i in range(1, 13):
    calc = num*i 
    print(calc)
    

#4. เขียน loop ที่พิมพ์ตัวอักษรแต่ละตัวในคำว่า "python"
#คำใบ้: ใช้ for char in "python":

word = "python"
for char in "python":
    print(char)

#5. หาค่าเฉลี่ยของเลข 5 ตัว โดยรับค่าจากผู้ใช้ทีละตัว
#(ใช้ loop + บวกสะสม แล้วหาร 5)

a = int(input(f"input first number: "))
b = int(input(f"input second number: "))
c = int(input(f"input third number: "))
d = int(input(f"input forth number: "))
e = int(input(f"input fifth number: "))

numbers = [a,b,c,d,e]
for i in numbers:
    i += 1 / 5
    print(i)'''
    
    
    
#เขียนฟังก์ชัน sum_even(n)
##คืนผลรวมของเลขคี่ตั้งแต่ 1 ถึง n
#เช่น sum_even(10) → 2+4+6+8+10


'''def sum_even(n): #สร้างฟังชั่น
    total = 0 #สร้างตัวแปร เก็บค่าในฟังชั่น
    
    for i in range(1,n+1): #ลูป i เริ่มตั้งแต่ 1 ถึง (สมมุติว่าอยากได้เลข10) ปกติจะเขียน 11 แต่เราสามารถใช้ 10+1 หรือ n+1
        
        if i % 2 == 0: #ตรงนี้เป็นเงื่อนไขว่า อยากได้เลขคู่: คือ หาก i ที่วิ่งเนี่ย มาหาร 2 แล้วเหลือเศษ ได้เท่ากับ 0 (เลขคู่ทั้งหลาย)
            
            total += i # จะเอาเลขตัวนั้นแหละ มา+กัน เก็บไว้ใน total
            
    return total # ***สำคัญ*** การคืนค่า ของ total คือจากตอนแรกเนี่ย total = 0 เมื่อreturn ค่าจากเงื่อนไขif แล้วนำไปแทนที่เลข0

print(sum_even(7)) # ตรงนี้คือ เมื่อเราปริ๊น ฟังชั่น>sum_even(n) เราได้กำกับให้เลข n เนี่ยมีค่าเป็น 7  ไอเลข7ก็จะไปวิ่งตามฟังชั่นที่เราสร้างขึ้นมา
# คำตอบก็จะได้ 12 !!!!!! '''


#✅ ข้อที่ 1: พิมพ์เลขคู่ระหว่าง 1 ถึง 50
#ให้แสดงเฉพาะเลขคู่เท่านั้น
#ใช้ if ตรวจ i % 2 == 0


numbers=[]
for i in range(1, 50+1):
    num = i
    if i % 2 == 0:
        numbers.append(num)
print(numbers)


#✅ ข้อที่ 2: หาผลรวมของเลขที่หาร 3 ลงตัว ตั้งแต่ 1 ถึง n
#สร้างฟังก์ชัน sum_div3(n)
#เช่น sum_div3(10) → 3 + 6 + 9 = 18

def sum_div3(n):
    total = 0
    
    for i in range(1, n+1):
        if i % 3 == 0:
            total += i
    return total

print(sum_div3(10))

#✅ ข้อที่ 3: ให้ผู้ใช้กรอกเลข 5 ตัว แล้วหาค่ามากที่สุด
#เก็บใน list + ใช้ max()

numbers = []
for i in range(5):
    num = int(input(f"please enter any number {i+1}: "))
    numbers.append(num)  
    
print(max(numbers))    

#✅ ข้อที่ 4: พิมพ์ดาวตามจำนวนที่ผู้ใช้กำหนด
#*
#**
#***
#****
#*****
#ใช้ for i in range(1, n+1) + "*" * i

star = "*"
for i in range(1,5+1):
    print("*" * i)

#✅ ข้อที่ 5: นับถอยหลังจาก n ถึง 1
#เขียนโปรแกรมให้รับ n แล้วพิมพ์นับถอยหลัง
#เช่น n = 5 → 5, 4, 3, 2, 1
#ใช้ range(n, 0, -1)

def count_down(n):
    number=[]
    for i in range(n, 0, -1):
        number.append(i)
    print(number)
    
count_down(5)