#coding:utf-8
from tkinter import *
import tkinter as tk
from tkinter.messagebox import *
from functools import partial
from math import *

class Calculatrice( tk.Tk ): 

    def __init__ ( self ):
        
        tk.Tk.__init__( self )
        self.a=StringVar()
        self.ecran=Entry(self, width=60, background="gray64", font="time 15 bold",justify="r",textvariable=self.a)
        self.ecran.grid(row=0,columnspan=7, ipady=30, sticky='w')
        self.text = ""
        #self.a.set("0")
        

    def clic(self,texte):
        if texte.strip()=="=":
            self.a.set(eval(self.a.get()))

        else:
            if texte.strip()=="x":
                self.a.set(self.a.get()+"*")
            elif texte.strip()=="CE":
                self.init()
            elif texte.strip()=="x^y":
                self.a.set(self.a.get()+"^")    
            else:
                self.a.set(self.a.get()+texte.strip())
        """else:
            if texte.strip()=="x^y":
                self.a.set(self.a.get()+"^")
               # self.a.set(eval(self.a.get()-"**"))
                #self.a.set(self.a.get()+"^")
            else:
                self.a.set(self.a.get()+texte.strip())"""
               
        
        
        #self.ecran.delete(ALL)
        #self.ecran.create_text(700-30, 90-30, text=self.text, font="Arial 15 bold")
        #self.evale(texte)

    
    
    def bouttons(self,texte,ligne,colonne):
        self.btn=Button(self, text=texte,font="arial 13",bd=5, relief=GROOVE, foreground="white",bg="gray22", command=partial(self.clic,texte)).grid(row=ligne, column=colonne,ipadx=28,ipady=5,padx=1,sticky="W",columnspan=1)

    def num_btn(self,texte,ligne,colonne):
        self.btn=Button(self, text=texte,font="arial 13",bd=5,relief=GROOVE, foreground="white",bg="gray40", command=partial(self.clic,texte)).grid(row=ligne, column=colonne,ipadx=28,ipady=5,padx=1,sticky="W",columnspan=1)
        
    def creer_btn(self):
        btn=Button(self, text="Rad    |     Deg",bd=8, foreground="white", relief=RIDGE,font="arial 14",bg="gray22",command=partial(self.clic,"Rad  |  Deg")).grid(row=1, column=0,sticky="NW",pady=2,columnspan=2,ipadx=40,ipady=5)

        self.bouttons(" x! ",1,2)
        self.bouttons("  ( ",1,3)
        self.bouttons("  ) ",1,4)
        self.bouttons("% ",1,5)
        self.bouttons("CE",1,6)

        self.bouttons("Inv",2,0)
        self.bouttons(" sin",2,1)
        self.bouttons(" In ",2,2)
        self.num_btn(" 7 ",2,3)
        self.num_btn(" 8 ",2,4)
        self.num_btn(" 9 ",2,5)
        self.bouttons("  /  ",2,6)

        self.bouttons("  p ",3,0)
        self.bouttons("cos",3,1)
        self.bouttons("log",3,2)
        self.num_btn(" 4 ",3,3)
        self.num_btn(" 5 ",3,4)
        self.num_btn(" 6 ",3,5)
        self.bouttons("  x ",3,6)

        self.bouttons("  e ",4,0)
        self.bouttons(" tan",4,1)
        self.bouttons("  v ",4,2)
        self.num_btn(" 1 ",4,3)
        self.num_btn(" 2 ",4,4)
        self.num_btn(" 3 ",4,5)
        self.bouttons("  -  ",4,6)


        btn=Button(self, text="Ans",font="arial 11",bd=5, foreground="white",bg="gray22", command=partial(self.clic,"Ans")).grid(row=5, column=0,ipadx=28,ipady=5,padx=1,sticky="W",columnspan=1)
        btn=Button(self, text="EXP",font="arial 11",bd=5, foreground="white",bg="gray22", command=partial(self.clic,"EXP")).grid(row=5, column=1,ipadx=28,ipady=5,padx=1,sticky="W",columnspan=1)

        btn=Button(self, text="x^y",font="arial 11", bd=5,foreground="white",bg="gray22", command=partial(self.clic,"x^y")).grid(row=5, column=2,ipadx=28,ipady=5,padx=1,sticky="W",columnspan=1)

        self.num_btn(" 0 ",5,3)
        self.num_btn("  . ",5,4)

        btn=Button(self, text=" = ",font="arial 13",bd=5, foreground="white",bg="purple3", command=partial(self.clic," = ")).grid(row=5, column=5,ipadx=28,ipady=5,padx=1,sticky="W",columnspan=1)
        self.bouttons("  + ",5,6)

if __name__ == "__main__":
    Calculatrice=Calculatrice()
    Calculatrice.title("Ma     😁️     Calculatrice       😃️") 
    Calculatrice.creer_btn()
    Calculatrice.resizable(width=False,height=False)
    Calculatrice.mainloop()
    
