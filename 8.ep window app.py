# window app - การสร้างหน้า Application โดยจะมีการใช้function ใน module ของ python ที่ชื่อว่า Tkinter
import tkinter as tk  # import module function tkinter เข้ามาและเปลี่ยนชื่อเป็น tk


#****ส่วนเพิ่มเติมที่เข้ามาทีหลัง - ข้ามไปก่อน ****
def set_massage(): #เรากำหนดตัวแปรขึ้นมาว่า หากมีการใช้งาน function นี้
    word=text_input.get() #เราสร้างตัวแปรชื่อว่า wordขึ้นมา เพื่อรับค่าจาก text_input ที่มีการพิมพ์เข้ามาใหม่ โดยใช้คำสั่ง .get()
    title_label.configure(text=word) #แล้วนำมาแทนที่ label ในส่วนของ title_lable โดยใช้function .configure 
    #โดยการแทนค่า(textอันเก่า ด้วย wordอันใหม่ที่มีการพิมพ์ลงในช่อง text_input)



window = tk.Tk()  #สร้างwindowขึ้นมา โดยเรียกใช้function Tk() ของ module (tk. หรือ tkinter.) - คำสั่ง TK() คือการสร้างหน้าwindow
window.title('Testing program') #เรียกใช้function tk.TK() หรือ window ตามด้วย  .title เพื่อตั้งชื่อ App ของเรา
            #ในวง window.title() ตรงนี้ จะเป็นชื่อ App ของเราจะเป็น Str - string ข้อความ (ต้องมี "  " ครอบไว้)
window.minsize(400, 400) #กำหนดขนาด app ของเรา - โดยเรียกคำสั่ง window.(หรือtk.TK) + function minsize(ขนาดกว้าง x ขนาดยาว) 




#การสร้าง UI - User interface ในหน้า Application
title_label = tk.Label(master=window, text='Learning with fun') #สร้างข้อความ โดยเรียกใช้function label() จากmodule tk.
# ข้างในวงเล็บ จะมี master เพื่อบอกตำแหน่งว่าข้อความนี้จะไปอยู่ไหนส่วนไหน และ text('  ') เป็นชนิดข้อความ = 'ข้อความที่อยากใส่'
title_label.pack() #เมื่อสร้างlabelแล้ว จะต้องนำมา แพ็คลงไปใน app โดยเราจะใช้ คำสั่ง .pack()

text_input = tk.Entry(master=window) #ในส่วนนี้จะเป็นการสร้างช่องข้อความ โดยการเรียก function Entry จากmoduel(tk)
text_input.pack() #จากนั้นก็ แพ็คลงใน App

ok_button = tk.Button(master=window, text='OK', command=set_massage) #ส่วนนี้เป็นการใส่ปุ่ม โดยเรียกfunction button จากmoduel(tk)
# ในส่วนของ command - คือการกำหนดค่าให้ ตัวปุ่มทำงานแล้วเกิดอะไรขึ้น โดยเราตั้งให้ ทำงานตาม (set_massage ในด้านบน)
ok_button.pack() #จากนั้นก็ แพ็คลงใน App





window.mainloop() #สร้างคำสั่งเพื่อ - startตัวAPP ของเราด้วย function mainloop