import tkinter as tk
from tkinter import ttk

from Views.EQPricingViews import *



#LabelInput(r_info, "Lab", input_class=ttk.Radiobutton,var=self._vars['Lab'], input_args={"values": ["A", "B", "C"]}).grid(row=1, column=0)


root = tk.Tk()
root.title('Free Pricer testing')
root.columnconfigure(0, weight=1)

entry = tk.DoubleVar()
entry2 = tk.DoubleVar()


a = ttk.LabelFrame(master=root,text="LABEL FRAME")
a.columnconfigure(0,weight=1)
a.columnconfigure(1,weight=1)
a.columnconfigure(2,weight=1) 
a.columnconfigure(3,weight=1) 
a.rowconfigure(0, weight=1)
a.grid(row=1,column=0,sticky=tk.EW,padx=3,pady=3)

LabelEntry(master=a, var=entry, label="XXX").grid(row=1, column=0,sticky=tk.EW,padx=10,pady=10)
LabelRadioButton(master=a, var=entry2, label="YYY",input_args={'values':['A','B','C']}).grid(row=2, column=0,sticky=tk.EW,padx=3,pady=3)

LabelEntry(master=a, var=entry, label="XX2").grid(row=1, column=1,sticky=tk.EW)
LabelRadioButton(master=a, var=tk.DoubleVar(), label="YY2",input_args={'values':['A','B','C']}).grid(row=2, column=1,sticky=tk.EW,padx=3,pady=3)

LabelEntry(master=a, var=entry, label="XX2").grid(row=1, column=2,sticky=tk.EW,padx=5,pady=5)
LabelRadioButton(master=a, var=tk.DoubleVar(), label="YY2",input_args={'values':['A','B','C']}).grid(row=2, column=2,sticky=tk.EW,padx=3,pady=3)

LabelEntry(master=a, var=entry, label="XX2").grid(row=3, column=3,sticky=tk.EW)

root.mainloop()
