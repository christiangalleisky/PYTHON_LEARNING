#This is an example of using the tkinter python extension to create a basic window with button

from tkinter import *
import LEXER

class MyFirstGUI: #class definition

    #This is the initialize function for a class.
    #Variables belonging to this class will get created and initialized in this function
    #What is the self parameter? It represents this class itself.
    #By using self.functionname, you can call functions belonging to this class.
    #By using self.variablename, you can create and use variables belonging to this class.
    #It needs to be the first parameter of all the functions in your class

    def __init__(self, root):
        #Master is the default prarent object of all widgets.
        #You can think of it as the window that pops up when you run the GUI code.
        self.master = root
        self.master.title("My Cat Registration System")
        self.DB = []
        self.x = 0.0
        self.y = 1.0
        
        #grid function puts a widget at a certain location
        # return value is none, please do not use it like self.label=Label().grad()
        #it will make self.label=none and you will no longer be able to change the label's content
        #top row

        self.Lexbutton = Button (self.master, text=" Lex Next Line", command=self.LexALine)
        self.Lexbutton.grid(row=0,column=0, sticky=E)
        
        self.submitbutton = Button (self.master, text="Quit", command=quit)
        self.submitbutton.grid(row=0,column=3, sticky=E)

        #2nd row
        self.textInputLabel = Label(self.master, text="Input")
        self.textInputLabel.grid(row=1,column=0,sticky=E)

        self.textSourceInput = Text(self.master, height = 5, width = 25)
        self.textSourceInput.grid(row=1, column=1, sticky =E)
        
        self.textOutputLabel = Label(self.master, text="Output")
        self.textOutputLabel.grid(row=1,column=2,sticky=E)

        self.textSourceOutput = Text(self.master, wrap = WORD, height = 5, width = 25)
        self.textSourceOutput.grid(row=1, column=3, sticky =E)
        
        #3rd row
        self.count = 1
        self.CountKeeperLabel = Label(self.master, text = "LineCount")
        self.CountKeeperLabel.grid(row=2, column=0, sticky =E)
        self.CountKeeper = Label(self.master, text = self.count)
        self.CountKeeper.grid(row=2, column=1, sticky =E)
        
        #make sure LEXER.py is in same directory
    def LexALine (self):
        print ("a line lexed!")
        self.x += 1.0
        self.y += 1.0
        self.CodeLine = self.textSourceInput.get(self.x, self.y)
        self.CodeLine = LEXER.lex(self.CodeLine)
        self.textSourceOutput.insert(INSERT, self.CodeLine)
        self.count += 1
        self.CountKeeper = Label(self.master, text = self.count)
        self.CountKeeper.grid(row=2, column=1, sticky =E)
        
if __name__ == '__main__':
    myTkRoot = Tk()
    my_gui = MyFirstGUI(myTkRoot)
    myTkRoot.mainloop()
