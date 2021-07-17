from json_operation import*
from tkinter import*
from csv import*
from os import close
from tkinter.ttk import*
from tkinter.messagebox import showinfo
import history_box
import time
import datetime


today = datetime.date.today()

# dd/mm/YY
d1 = today.strftime("%d/%m/%Y")

time_1 = time.strftime("%I:%M %p")

dt = [d1,time_1]

class vars:
    def __init__(self) :
            self.txt1 = IntVar()
            self.txt2 = IntVar()
            self.txt3 = IntVar()
            self.txt4 = IntVar()
            self.txt5 = IntVar()
            self.txt6 = IntVar()
            self.txt7 = IntVar()
            self.txt8 = IntVar()
            self.txt9 = IntVar()
            self.txt10 = IntVar()
            self.txt11 = IntVar()
            self.txt12 = IntVar()




class design(vars):
    def __init__(self,window):
        vars.__init__(self)
        self.window = window
        
        Label(self.window, text="Sm 170").grid(column=0, row=0)
        Entry(self.window,textvariable=self.txt1,width=10).grid(column=2, row=0)

        Label(self.window, text="Sm 500").grid(column=0, row=1)
        Entry(self.window,textvariable=self.txt2,width=10).grid(column=2, row=1)

        Label(self.window, text="Sm 1L").grid(column=0, row=2)
        Entry(self.window,textvariable=self.txt3,width=10).grid(column=2, row=2)
        
        Label(self.window, text="fcm 250").grid(column=0, row=3)
        Entry(self.window,textvariable=self.txt4,width=10).grid(column=2, row=3)
        
        Label(self.window, text="fcm 500").grid(column=0, row=4)
        Entry(self.window,textvariable=self.txt5,width=10).grid(column=2, row=4)

        Label(self.window, text="fcm 1L").grid(column=0, row=5)
        Entry(self.window,textvariable=self.txt6,width=10).grid(column=2, row=5)

        Label(self.window, text="c_140").grid(column=0, row=6)
        Entry(self.window,textvariable=self.txt7,width=10).grid(column=2, row=6)

        Label(self.window, text="c_500").grid(column=0, row=7)
        Entry(self.window,textvariable=self.txt8,width=10).grid(column=2, row=7)

        Label(self.window, text="c.c_6").grid(column=0, row=8)
        Entry(self.window,textvariable=self.txt9,width=10).grid(column=2, row=8)

        Label(self.window, text="c.c_10").grid(column=0, row=9)
        Entry(self.window,textvariable=self.txt10,width=10).grid(column=2, row=9)

        Label(self.window, text="c.c_20").grid(column=0, row=10)
        Entry(self.window,textvariable=self.txt11,width=10).grid(column=2, row=10)

        Label(self.window, text="b.m").grid(column=0, row=11)
        Entry(self.window,textvariable=self.txt12,width=10).grid(column=2, row=11)

        
        btn1 = Button(self.window, text="Submit", command=self.clicked)
        btn1.grid(column=5, row=12)
    
        btn2 = Button(self.window, text="save history",command=self.run)
        btn2.grid(column=6,row=12)

        btn3 = Button(self.window,text="view history",command=history_box.main)
        btn3.grid(column=7,row=12)



    def clicked(self):
        
        global sum_value
            
        try:
                
            smtot = ((int(self.txt1.get())*sm170)+(int(self.txt2.get())*sm500)+(int(self.txt3.get())*sm1l))
            fcmtot = ((int(self.txt4.get())*fcm250)+(int(self.txt5.get())*fcm500)+(int(self.txt6.get())*fcm1l))
            curdtot = ((int(self.txt7.get())*c140)+(int(self.txt8.get())*cup50)+(int(self.txt9.get())*cup50)+(int(self.txt10.get())*cup100)+(int(self.txt11.get())*cup200)+(int(self.txt12.get())*bm))
            sum_value = smtot + fcmtot + curdtot
            Label(self.window,text ="AMOUNT :" + str(sum_value),font="family",).place(x=0,y=255)
        except:
            self.window2 = Toplevel()
            Label(self.window2,text ="In Valid entry pls try again",).grid(column=0,row=1)
            Button(self.window2,text="ok",command=self.window2.destroy).grid(column=1,row=2)


    def run(self):
        cv = open("history .csv",'a',newline='')
        
        try:
            var = [int(self.txt1.get()),int(self.txt2.get()),int(self.txt3.get()),int(self.txt4.get()),int(self.txt5.get()),int(self.txt6.get()),
            int(self.txt7.get()),int(self.txt8.get()),int(self.txt9.get()),int(self.txt10.get()),int(self.txt11.get()),
            int(self.txt12.get()),sum_value,dt]
        except:
            self.window2 = Toplevel()
            Label(self.window2,text=" error Enter your calculation and submit it to save").grid(column=0,row=0)
            Button(self.window2,text="ok",command=self.window2.destroy).grid(column=1,row=2)
 
        #write the history list
        writer_ob = writer(cv)
        writer_ob.writerow(var)
        self.window2 = Toplevel()
        self.window2.title("Notify")
        Label(self.window2,text='History Saved',font='bold').grid(column=0,row=0)
        Button(self.window2,text="Done",command=self.window2.destroy).grid(column=0,row=2)
        cv.close()



def main(): 
    window = Tk()
    
    # Create a Frame for border
    window.title(" ")
    window.configure(borderwidth=7, relief="solid",background="#000fff000")
    app = design(window)
    window.mainloop()


if __name__ == '__main__':
    main()
