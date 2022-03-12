import tkinter as tk

root= tk.Tk()
root.title("GreenSprings BMI Calculator")

canvas1 = tk.Canvas(root, width = 400, height = 600,  relief='raised')
canvas1.pack()

bg = tk.PhotoImage(file="heart.png")
label5=tk.Label(root, image = bg)
label5.place(x=0, y=0)


label1 = tk.Label(root, text='Check you BMI')
label1.config(font=('helvetica', 14), foreground= "red")
canvas1.create_window(200, 25, window=label1)

label2 = tk.Label(root, text='Enter you height:')
label2.config(font=('helvetica', 10))
canvas1.create_window(200, 100, window=label2)

entry1 = tk.Entry(root)
canvas1.create_window(200, 140, window=entry1)

label3 = tk.Label(root, text='Enter your weight:')
label3.config(font=('helvetica', 10))
canvas1.create_window(200, 240, window=label3)

entry2 = tk.Entry(root)
canvas1.create_window(200, 280, window=entry2)


def BMI():
    height = float(entry1.get())
    weight = float(entry2.get())
    bmi=weight/pow(height, 2)
    if bmi<18.5:
        label4 = tk.Label(root, text= f"Your BMI is:{bmi}, Your are Underweight",font=('helvetica', 10))
        canvas1.create_window(200, 400, window=label4)
    elif bmi>=18.5 and bmi<25.0:
        label4 = tk.Label(root, text= f"Your BMI is:{bmi}, Your are of Healthy weight",font=('helvetica', 10))
        canvas1.create_window(200, 400, window=label4)
    elif bmi>=25.0 and bmi<30.0:
        label4 = tk.Label(root, text= f"Your BMI is:{bmi}, Your are Overweight",font=('helvetica', 10))
        canvas1.create_window(200, 400, window=label4)
    else:
        label4 = tk.Label(root, text= f"Your BMI is:{bmi}, Your are Obese",font=('helvetica', 10))
        canvas1.create_window(200, 400, window=label4)



button1 = tk.Button(text='Calculate BMI', command=BMI, bg='green', fg='white', font=('Agency FB', 14, 'bold'))
canvas1.create_window(200, 360, window=button1)

root.resizable(False, False)
root.mainloop()
