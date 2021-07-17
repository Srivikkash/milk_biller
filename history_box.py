from tkinter import *
import tkinter.ttk as ttk
import csv


def history(root):

    TableMargin = Frame(root, width=500)
    TableMargin.pack(side=TOP)
    scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
    scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
    tree = ttk.Treeview(TableMargin, columns=('sm170', 'sm500', 'sm1l', 'fcm250', 'fcm500', 'fcm1l', 'curd_140', 'curd_500', 'curd_6_cup', 'curd_10 _cup', 'curd_20_cup', 'butter_milk', 'sum'), height=400, selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    tree.heading('sm170', text="sm170", anchor=W)
    tree.heading('sm500', text="sm500", anchor=W)
    tree.heading('sm1l', text="sm1l", anchor=W)
    tree.heading('fcm250', text="fcm250", anchor=W)
    tree.heading('fcm500', text="fcm500", anchor=W)
    tree.heading('fcm1l', text="fcm1l", anchor=W)
    tree.heading('curd_140', text="curd_140", anchor=W)
    tree.heading('curd_500', text="curd_500", anchor=W)
    tree.heading('curd_6_cup', text="curd_6_cup", anchor=W)
    tree.heading('curd_10 _cup', text="curd_10 _cup", anchor=W)
    tree.heading('curd_20_cup', text="curd_20_cup", anchor=W)
    tree.heading('butter_milk', text="butter_milk", anchor=W)
    tree.heading('sum', text="sum", anchor=W)

    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=200)
    tree.column('#2', stretch=NO, minwidth=0, width=200)
    tree.column('#3', stretch=NO, minwidth=0, width=300)
    tree.column('#4', stretch=NO, minwidth=0, width=300)
    tree.column('#5', stretch=NO, minwidth=0, width=300)
    tree.column('#6', stretch=NO, minwidth=0, width=300)
    tree.column('#7', stretch=NO, minwidth=0, width=300)
    tree.column('#8', stretch=NO, minwidth=0, width=300)
    tree.column('#9', stretch=NO, minwidth=0, width=300)
    tree.column('#10', stretch=NO, minwidth=0, width=300)
    tree.column('#11', stretch=NO, minwidth=0, width=300)
    tree.column('#12', stretch=NO, minwidth=0, width=300)
    tree.column('#13', stretch=NO, minwidth=0, width=300)
    tree.pack()

    with open('D:\documents\python\milk_product\history .csv') as f:
        reader = csv.DictReader(f, delimiter=',')
        for row in reader:
            sm170 = row['sm170']
            sm500 = row['sm500']
            sm1l = row['sm1l']
            fcm250 = row['fcm250']
            fcm500 = row['fcm500']
            fcm1l = row['fcm1l']
            curd_140 = row['curd_140']
            curd_500 = row['curd_500']
            curd_6_cup = row['curd_6_cup']
            curd_10_cup = row['curd_10_cup']
            curd_6_cup = row['curd_6_cup']
            curd_20_cup = row['curd_20_cup']
            butter_milk = row['butter_milk']
            sum = row['sum']
            tree.insert("", 0, values=(sm170,sm500,sm1l,fcm250,fcm500,fcm1l,curd_140,curd_500,curd_6_cup,curd_10_cup,curd_20_cup,butter_milk,sum))
def main():

    root = Tk()
    root.title("History")
    width = 500
    height = 400
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    root.geometry("%dx%d+%d+%d" % (width, height, x, y))
    root.resizable(0, 0)
    alter = history(root)
    root.mainloop()

if __name__ == '__main__':
    main()