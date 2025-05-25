#Condition หรือ if, elif(Else-If), Else  - คือการประกาศค่าให้ทำตาม เงื่อนไข เช่น

score = 88   #แทนค่า score = (คะแนนที่ได้)

if score >= 85:  # เงื่อนไขแรก if - คะแนนได้มากกว่าหรือเท่า85 
    print('Grade A') # ให้ทำการ แสดงผล Grade A

elif score >= 70: # เงื่อนไขที่2 **ในส่วนนี้จะใช้ elif เมื่อเงื่อนไขแรกไม่ตรง
    print('Grade B') 

elif score >= 60: # ***สังเกตได้ว่า elif สามารถมีได้หลายตัว หลายเงื่อนไข
    print('Grade C')

elif score >= 55: 
    print('Grade D')

else: # ***** สำคัญที่สุดคือ elif จะเป็นเงื่อนไขสุดท้าย และจะไม่มีอะไรต่อท้ายนี้แล้ว
    print('Grade F')