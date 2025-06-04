#หาค่า BMI
"""
-BMI label -ชื่อ
-ต้องมี ค่าinput น้ำหนัก,ส่วนสูง
-สูตรหาค่า bmi ตารางเปรียบเทียบ 
-outputที่1 แสดงค่า สูตร bmi
-outputที่2 เอาค่าสูตร BMI แสดงออกมา UI
"""
#bmi = weight / (height ** 2)
"""
weight = int(input('what is your weight:'))
height = float(input('what is your height:'))

bmi = weight / (height ** 2)

print(str(bmi))
if bmi < 18.5:
    print('too skinny')
elif bmi < 25.00:
    print('balance')
elif bmi < 30.00:
   print('shubby')
elif bmi < 35.00:
    print('fatty')
else:
    print('over fat')
"""

import tkinter as tk

def get_bmi_calc():
    weight = int(weight_input.get()) 
    height = float(height_input.get())
    
    bmi = weight / (height ** 2)
    bmi = round(bmi, 2)
    
    
    if bmi < 18.5:
        output_label.configure(text=str(bmi) + '\n' +'Too Skinny')
    elif bmi < 25.00:
        output_label.configure(text= str(bmi) + '\n' +'Balance')
    elif bmi < 30.00:
        output_label.configure(text= str(bmi) + '\n' +'Chubby')
    elif bmi < 35.00:
        output_label.configure(text= str(bmi) + '\n' +'Fatty')
    else:
        output_label.configure(text= str(bmi) + '\n' +'Over Fat')
    

window = tk.Tk()
window.title('BMI')
window.minsize(400, 400)

title_label = tk.Label(master=window, text='BMI - Calculator', font= 16)
title_label.pack(pady=20)

weight_label = tk.Label(master=window, text='What is your weight? (kg.)')
weight_label.pack()
weight_input= tk.Entry(master=window)
weight_input.pack()

height_label = tk.Label(master=window, text='What is your height (m.)')
height_label.pack(pady=10)
height_input = tk.Entry(master=window)
height_input.pack()

ok_button = tk.Button(master=window, text='Calculate BMI', command=get_bmi_calc)
ok_button.pack(pady=10)

output_label = tk.Label(master=window, font=12)
output_label.pack(pady=20)

window.mainloop()