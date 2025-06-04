#*สร้าง list ใหม่ที่มีค่าทุกตัว 2 จาก list ด้านล่าง
#nums = [3, 6, 9, 12]
# Expected: [6, 12, 18, 24]
nums = [3, 6, 9, 12]
new_nums = [x * 2 for x in nums]
print(new_nums)

#🧪 ข้อที่ 2: Filter Short Words
#กรองเฉพาะคำที่มีความยาวไม่เกิน 4 ตัว
#words = ['cat', 'tiger', 'lion', 'ant', 'elephant']
# Expected: ['cat', 'lion', 'ant']
words = ['cat', 'tiger', 'lion', 'ant', 'elephant']
sort_word = [list(filter(lambda w :len(w) <= 4 ,words))]
print(sort_word)


#🧪 ข้อที่ 3: Squared Odds
#สร้าง list ของเลขกำลังสอง เฉพาะตัวเลขคี่ในช่วง 1-10
# Expected: [1, 9, 25, 49, 81]

double_numbers = [x **2 for x in range(1 , 10+1) if x % 2 !=0]
print(double_numbers)

#🧪 ข้อที่ 4: First Letters
#แยกตัวอักษรแรกของคำใน list ออกมาเป็น list ใหม่
#words = ['python', 'java', 'c++', 'rust']
# Expected: ['p', 'j', 'c', 'r']

words = ['python', 'java', 'c++', 'rust']
first_word = [w[0] for w in words]
print(first_word)


#🧪 ข้อที่ 5: Clean Numbers
#จาก list ที่มีทั้งตัวเลขและ string ให้แปลงเฉพาะตัวเลขเป็น int แล้วรวมใน list ใหม่
#items = ['10', 20, '30', 40, 'fifty', 60]
# Expected: [10, 20, 30, 40, 60]
#ヒント: ใช้ isinstance(x, int) กับ x.isdigit() ช่วยได้ 😉

#อันนี้ไม่รู้เรื่องเลยครับ 
items = ['10', 20, '30', 40, 'fifty', 60]
new_items = [int(x) for x in items if isinstance(x, int) or isinstance(x, str) and x.isdigit()]
print(new_items)


#🧪 ข้อที่ 1: Multiply by 3
#*สร้าง list ใหม่ที่มีค่าทุกตัว 3 จาก list ด้านล่าง
#nums = [2, 5, 7, 11]
# Expected: [6, 15, 21, 33]

nums = [2, 5, 7, 11]
new_nums = [x * 3 for x in nums]
print(new_nums)


#🧪 ข้อที่ 2: Filter Short Words
#กรองเฉพาะคำที่มีความยาวไม่เกิน 5 ตัว
#words = ['dog', 'eagle', 'lion', 'rabbit', 'bat']
# Expected: ['dog', 'lion', 'bat']
words = ['dog', 'eagle', 'lion', 'rabbit', 'bat']
short = [w for w in words if len(w) <5]
print(short)

#🧪 ข้อที่ 3: Squared Odds
#สร้าง list ของเลขกำลังสอง เฉพาะตัวเลขคี่ในช่วง 10-20
# Expected: [121, 169, 225, 289, 361, 441]
squared_oods = [x**2 for x in range(10, 20+1) if x % 2 !=0]
print(squared_oods)

#🧪 ข้อที่ 4: First Letters
#แยกตัวอักษรแรกของคำใน list ออกมาเป็น list ใหม่
#words = ['grape', 'melon', 'date', 'kiwi']
# Expected: ['g', 'm', 'd', 'k']
words = ['grape', 'melon', 'date', 'kiwi']
first_letter = [w[0] for w in words]
print(first_letter)

#🧪 ข้อที่ 5: Clean Numbers
#จาก list ที่มีทั้งตัวเลขและ string ให้แปลงเฉพาะตัวเลขเป็น int แล้วรวมใน list ใหม่
#items = ['25', 15, '60', 'hello', 90, '35']
# Expected: [25, 15, 60, 90, 35]
items = ['25', 15, '60', 'hello', 90, '35']
clean_number = [int(x) for x in items if isinstance(x,int) or (isinstance(x,str)) and x.isdigit()]
print(clean_number)