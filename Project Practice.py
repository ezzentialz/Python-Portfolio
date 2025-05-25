import tkinter as tk

def get_calc():
    number = int(number_input.get())
    if number == 0:
        return output_label.configure(text= 'Absolute 0')
    
    output = ''

    for i in range(1, 25):
        output += str(number) + ' x ' + str(i)
        output += ' = ' + str(number * i) + '\n'

    output_label.configure(text=output)    

window = tk.Tk()
window.title('แม่สูตรคูณ')
window.minsize(500, 600)

window_label = tk.Label(master=window, text='แม่สูตรคูณ')
window_label.pack(pady=20)
number_input = tk.Entry(master=window)
number_input.pack()
submit_button = tk.Button(master=window, text='ได้แก่', command=get_calc, 
                          width=5, height=1,)
submit_button.pack(pady=10)

output_label = tk.Label(master= window)
output_label.pack(pady=20)

window.mainloop()