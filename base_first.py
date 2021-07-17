# from os import close
# from tkinter import *
# from tkinter.ttk import*
# from json_operation import *
# from csv import writer

# #open a window using gui
# window = Tk()
# window.title("")
# window.configure(background='#78d6ff')
# # window.geometry('1000x500')#window open size

# txt1 = IntVar()
# txt2 = IntVar()
# txt3 = IntVar()
# txt4 = IntVar()
# txt5 = IntVar()
# txt6 = IntVar()
# txt7 = IntVar()
# txt8 = IntVar()
# txt9 = IntVar()
# txt10 = IntVar()
# txt11 = IntVar()
# txt12 = IntVar()

# Label(window, text="Sm 170").grid(column=0, row=0)
# Entry(window,textvariable=txt1,width=10).grid(column=2, row=0)

# Label(window, text="Sm 500").grid(column=0, row=1)
# Entry(window,textvariable=txt2,width=10).grid(column=2, row=1)

# Label(window, text="Sm 1L").grid(column=0, row=2)
# Entry(window,textvariable=txt3,width=10).grid(column=2, row=2)
 
# Label(window, text="fcm 250").grid(column=0, row=3)
# Entry(window,textvariable=txt4,width=10).grid(column=2, row=3)
 
# Label(window, text="fcm 500").grid(column=0, row=4)
# Entry(window,textvariable=txt5,width=10).grid(column=2, row=4)

# Label(window, text="fcm 1L").grid(column=0, row=5)
# Entry(window,textvariable=txt6,width=10).grid(column=2, row=5)

# Label(window, text="c_140").grid(column=0, row=6)
# Entry(window,textvariable=txt7,width=10).grid(column=2, row=6)

# Label(window, text="c_500").grid(column=0, row=7)
# Entry(window,textvariable=txt8,width=10).grid(column=2, row=7)

# Label(window, text="c.c_6").grid(column=0, row=8)
# Entry(window,textvariable=txt9,width=10).grid(column=2, row=8)

# Label(window, text="c.c_10").grid(column=0, row=9)
# Entry(window,textvariable=txt10,width=10).grid(column=2, row=9)

# Label(window, text="c.c_20").grid(column=0, row=10)
# Entry(window,textvariable=txt11,width=10).grid(column=2, row=10)

# Label(window, text="b.m").grid(column=0, row=11)
# Entry(window,textvariable=txt12,width=10).grid(column=2, row=11)

# def close_win():
#     print('close')
#     pass


# def clicked():
#     global sum_value
#     smtot = ((int(txt1.get())*sm170)+(int(txt2.get())*sm500)+(int(txt3.get())*sm1l))
#     fcmtot = ((int(txt4.get())*fcm250)+(int(txt5.get())*fcm500)+(int(txt6.get())*fcm1l))
#     curdtot = ((int(txt7.get())*c140)+(int(txt8.get())*cup50)+(int(txt9.get())*cup50)+(int(txt10.get())*cup100)+(int(txt11.get())*cup200)+(int(txt12.get())*bm))
#     sum_value = smtot + fcmtot + curdtot
#     Label(window,text ="AMOUNT :" + str(sum_value),font="family",).place(x=0,y=255)
    


# def run():
#     cv = open("D:\documents\python\milk_product\history .csv",'a',newline='')
#     var = [(int(txt1.get()),int(txt2.get()),int(txt3.get()),int(txt4.get()),int(txt5.get()),
#     int(txt6.get()),int(txt7.get()),int(txt8.get()),int(txt9.get()),int(txt10.get()),int(txt11.get()),
#     int(txt12.get()),sum_value)]
#     #write the history list
#     writer_ob = writer(cv)
#     writer_ob.writerow(var)
#     window3 = Tk()
#     window3.title("Notify")
#     Label(window3,text='History Saved',font='bold').grid(column=0,row=0)
#     btn4 = Button(window3,text="ok",command=close_win).grid(column=0,row=2)
#     cv.close()


# def history():
#     cv = open("D:\documents\python\milk_product\history .csv",'r')
#     window2 = Tk()
#     window2.title("HISTORY")
#     his = cv.readlines()
#     Label(window2,text=his).grid(column=0,row=1)
    


# btn1 = Button(window, text="Submit", command=clicked)
# btn1.grid(column=5, row=12)

# btn2 = Button(window, text="save history",command=run)
# btn2.grid(column=6,row=12)

# btn3 = Button(window,text="view history",command=history)
# btn3.grid(column=7,row=12)


# window.mainloop()

