# import tkinter as tk
# from tabulate import tabulate

# cv = open("D:\documents\python\milk_product\history .csv",'r',newline="")
# data = cv.readlines()


# # data = [('id', 'first name', 'last name', 'age', 'marks'),
# #         (1, 'JohnCena', 'Peter', 24, 74),
# #         (2, 'James', 'Peter', 24, 70),
# #         (3, 'Cena', 'Peter', 14, 64),
# #         (14, 'John', 'Mars', 34, 174)
# #         ]


# class TabulateLabel(tk.Label):
#     def __init__(self, parent, data, **kwargs):
#         super().__init__(parent, 
#                          font=('Consolas', 10), 
#                          justify=tk.LEFT, anchor='nw', **kwargs)

#         text = tabulate(data, headers='firstrow', tablefmt='github', showindex=False)
#         self.configure(text=text)


# class App(tk.Tk):
#     def __init__(self):
#         super().__init__()
#         TabulateLabel(self, data=data, bg='white').grid(sticky='ew')

# if __name__ == "__main__":
#     App().mainloop()



