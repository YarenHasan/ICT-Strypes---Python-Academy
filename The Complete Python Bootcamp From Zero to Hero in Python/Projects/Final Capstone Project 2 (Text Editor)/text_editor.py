from tkinter import *
import tkinter.filedialog as tk
import tkinter.messagebox as tk2


class Application(Frame):

    def __init__(self, master):
        """
        This is the constructor for the Application class.
        It initializes the GUI window and calls create_widgets() to set up the interface.
        """
        super(Application, self).__init__(master)
        self.create_widgets()

    def create_widgets(self):
        """
        Sets up the interface:
            Adds a Text widget (self.text1) where the user can write text.
            Creates a menu bar with three menus: File, Edit, and Tools.
            Adds options to each menu, linking them to the functions defined below.
        """
        self.text1 = Text(width=20, height=20)
        self.text1.pack(expand=YES, fill=BOTH)  # to make the textbox fill the entire window

        menubar = Menu(self)
        filemenu = Menu(menubar)
        editmenu = Menu(menubar)
        toolsmenu = Menu(menubar)
        filemenu.add_command(label='New', command=self.newDoc)
        filemenu.add_command(label='Save', command=self.saveDoc)
        filemenu.add_command(label='Open', command=self.openDoc)
        editmenu.add_command(label='Copy', command=self.copy)
        editmenu.add_command(label='Paste', command=self.paste)
        editmenu.add_command(label='Clear', command=self.clear)
        toolsmenu.add_command(label='Word Count', command=self.wordCount)
        menubar.add_cascade(label='File', menu=filemenu)
        menubar.add_cascade(label='Edit', menu=editmenu)
        menubar.add_cascade(label='Tools', menu=toolsmenu)
        root.config(menu=menubar)

    def newDoc(self):
        """
        Asks the user if they want to start a new document.
        If they say yes, it clears all text in the editor.
        """
        if tk2.askyesno("Message", "Unsaved work will be lost. Continue?"):
            self.text1.delete("1.0", END)

    def saveDoc(self):
        """
        Opens a dialog box asking where to save the file.
        Saves the content of the text box (self.text1) to a .txt file.
        """
        savefile = tk.asksaveasfile(mode='w', defaultextension=".txt")
        text2save = str(self.text1.get("1.0", END))
        savefile.write(text2save)
        savefile.close()

    def openDoc(self):
        """
        Opens a file chooser to select a text file.
        Reads the file and inserts its contents into the text box.
        """
        openfile = tk.askopenfile(mode='r')
        text = openfile.read()
        self.text1.insert(END, text)
        openfile.close()

    def copy(self):
        """
        Copies the selected text to the clipboard using self.clipboard_append().
        """
        var = str(self.text1.get(SEL_FIRST, SEL_LAST))
        self.clipboard_clear()
        self.clipboard_append(var)

    def paste(self):
        """
        Gets the text from the clipboard and pastes it at the top of the text box ("1.0" position).
        """
        result = self.selection_get(selection="CLIPBOARD")
        self.text1.insert("1.0", result)

    def clear(self):
        """
        Clears all text from the text box.
        """
        self.text1.delete("1.0", END)

    def wordCount(self):
        """
        Gets the full text from the editor.
        Splits it into a list of words using whitespace.
        Shows the number of words in a pop-up message box.
        """
        userText = self.text1.get("1.0", END)
        wordList = userText.split()
        number_of_words = len(wordList)
        tk2.showinfo('Word Count', 'Words:  ' + str(number_of_words))


root = Tk()
root.title('Text Editor')
root.geometry('700x600')
app = Application(root)
app.mainloop()
