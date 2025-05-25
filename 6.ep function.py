# Function - เป็นการรวบรวมคำสั่งต่างๆไว้ในที่เดียว เพื่อประหยัดพื้นที่ เช่น:
width0 = 4
length0 = 4
height0 = 2
box_area0= width0 * length0 * height0 # กำหนด กว้าง x ยาว x สูง มาเก็บไว้ใน box_area

#ตัวอย่างที่1 - เราสามารถสร้างfunctionของเราเองได้ โดยใช้คำสั่ง def get_(ชื่อfunctionที่เราสามารถสร้างได้)
def get_box_area1(): #ในวงเล็บเราจะ(แทนค่าที่1, ค่าที่2, ค่าที่3)
    width1 = 5
    lenght1 = 3
    height1 = 2
    box_area = width1 * lenght1 * height1 # แล้วเรากำหนด ให้ box_area = ค่าที่1 x ค่าที่2 x ค่าที่3
    print(box_area) #และ คำสั่งแสดลงผล
get_box_area1() # เมื่อเราเรียกใช้ fucntion นี้ มันจะแสดงผลทันที เพราะมีคำสั่ง print อยู่ด้วย

#ตัวอย่างที่2 - การใช้ parameter ในวงกลม
def get_box_area2(width2, height2, lenght2): #เราสามารถแทนค่า ในวงกลม ได้เป็น ค่าที่1,2,และ3
    box_area2 = width2 * height2 * lenght2 #กำหนดให้ box_area2 = ค่าที่1 x ค่าที่2 x ค่าที่3
    print(box_area2)
get_box_area2(10, 2, 2) #เมื่อเราใช้งานfunction และแทนค่าในวงกลม(ค่าที่1,2,3) ก็จะแสดงผลลัพธ์ออกมา

#ตัวอย่างที่3 - การใช้ return เพื่อคืนค่า และ ยกเลิกการทำงานของfunctionนั้น เช่น:
def get_box_area(width, height, lenght):
    if width >10 or height >10 or lenght >10:# เพิ่มเงื่อนไข หากค่าใดๆ มีมากกว่า10
        return 'oversize' # ให้ทำการยกเลิกการคำนวน แล้วแสดงผล oversize
    elif width <0 or height <0 or lenght <0: # หรือ เงื่อนไข หากค่าใดๆ น้อยกว่า0
        return 'imposible' # ให้แสดงค่าเป็น imposible
    box_area = width * height * lenght # หากไม่ติดเงื่อนไขใดๆ ก็ให้ทำการคำนวนตามนี้
    return box_area #***เนื่องจากเราไม่ได้ใช้คำสั่งprint เพื่อแสดงผล ค่าที่เราได้มาก็จะไม่มี
    #แต่หากเราใช้ คำสั่ง return - ผลลัพธ์ก็จะคืนค่าให้เรา ทำให้เราสามารถใช้ คำสั่งprint ทีหลังได้

box1 = get_box_area(5, 1, 2) # กล่องแรก ขนาดกล่อง ไม่ได้ติดเงื่อนไข
box2 = get_box_area(15, 2, 4) # กล่องสอง ติดเงื่อนไข มากกว่า 10
box3 = get_box_area(4, -2, 3) # กล่องสาม ติดเงื่อนไข น้อยกว่า 0

print(box1) #เมื่อแสดงผล ค่าที่ return จะแสดงออกมา
print(box2) #ค่าreturn แสดงผลที่ติดเงื่อนไข - oversize
print(box3) #ค่าreturn แสดงผลที่ติดเงื่อนไข - imposible