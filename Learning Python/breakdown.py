"""
adult = 590
child = 295

output
total price - 
pure price - 
service charge 10% -
vat - 
provincial -

"""

import tkinter as tk

def get_bf_calc():
    
    adult = int(adult_input.get()) 
    child = int(child_input.get())
    
    adult_price = adult * 590
    child_price = child * 295
    
    total_price_people = adult_price + child_price
    total_price_people = round(total_price_people, 2)
    output_total_price_people_label.configure(text='ยอดรวม :' + str(total_price_people))
    
    pure_price = total_price_people / 1.187
    pure_price = round(pure_price, 2)
    output_pure_price_label.configure(text='ราคาเพียว :' + str(pure_price))
    
    
    service_charge = pure_price * 0.1
    service_charge = round(service_charge, 2)
    output_service_charge_label.configure(text='Service Charge 10% :' + str(service_charge))
    
    vat = (pure_price + service_charge) * 0.07
    vat = round(vat, 2)
    output_vat_label.configure(text='vat :'+ str(vat))
    
    provincial = pure_price * 0.01
    provincial = round(provincial, 2)
    output_provincial_label.configure(text='Provincial :'+ str(provincial))
    
    final_price = pure_price + service_charge + vat + provincial
    final_price = round(final_price, 2)
    output_final_price_label.configure(text='ยอดทั้งหมด :'+ str(final_price))
    
    

window = tk.Tk()
window.title('Breakdown ABF')
window.minsize(500, 550)
window.config(bg="#f4f4f9")  # Set a light background color

# Title label with bigger font and padding
title_label = tk.Label(master=window, text='Breakdown ABF', font=("Helvetica", 20, "bold"), bg="#f4f4f9", fg="#333")
title_label.pack(pady=30)

# Credit label
credit_label = tk.Label(master=window, text='By. Jirath T', font=("Helvetica", 10), bg="#f4f4f9", fg="#555")
credit_label.pack()

# Adult input
adult_label = tk.Label(master=window, text='How many Adults ? :', font=("Helvetica", 12), bg="#f4f4f9", fg="#333")
adult_label.pack(pady=5)
adult_input = tk.Entry(master=window, font=("Helvetica", 12), relief="solid", width=20)
adult_input.pack(pady=5)

# Child input
child_label = tk.Label(master=window, text='How many Children ? :', font=("Helvetica", 12), bg="#f4f4f9", fg="#333")
child_label.pack(pady=5)
child_input = tk.Entry(master=window, font=("Helvetica", 12), relief="solid", width=20)
child_input.pack(pady=5)

# Breakdown button
ok_button = tk.Button(master=window, text='Breakdown', command=get_bf_calc, font=("Helvetica", 14, "bold"), bg="#5cb85c", fg="white", relief="raised", width=20, height=2)
ok_button.pack(pady=20)

# Output labels with styled fonts and spacing
output_total_price_people_label = tk.Label(master=window, font=("Helvetica", 14, "bold"), fg="red", bg="#f4f4f9")
output_total_price_people_label.pack(pady=10)

output_pure_price_label = tk.Label(master=window, font=("Helvetica", 14), bg="#f4f4f9")
output_pure_price_label.pack(pady=10)

output_service_charge_label = tk.Label(master=window, font=("Helvetica", 14), bg="#f4f4f9")
output_service_charge_label.pack(pady=10)

output_vat_label = tk.Label(master=window, font=("Helvetica", 14), bg="#f4f4f9")
output_vat_label.pack(pady=10)

output_provincial_label = tk.Label(master=window, font=("Helvetica", 14), bg="#f4f4f9")
output_provincial_label.pack(pady=10)

output_final_price_label = tk.Label(master=window, font=("Helvetica", 14, "bold"), fg="red", bg="#f4f4f9")
output_final_price_label.pack(pady=10)

# Main loop
window.mainloop()