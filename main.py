from tkinter import *
from tkinter.filedialog import askopenfile, asksaveasfilename
from tkinter.messagebox import showerror

filename = None

def NewFile():
    global filename
    filename = None
    Text.delete(1.0, END)
    
    
def SaveFile():
    global filename
    if filename is None:
        SaveAs()
    else:
        try:
            with open(filename, 'w') as f:
                f.write(text.get(1.0, END).rstrip())
        except Exception as e:
            showerror("Erro ao salvar", f"Não foi possível salvar o arquivo.\nErro: {e}")    
     
      
def SaveAs():
    global filename
    file_path = asksaveasfilename(defaultextension=".txt",
                                  filetypes=[("Text files", "*.txt"),
                                             ("All files", "*.*")])
    if not file_path:
        return
    filename = file_path
    SaveFile()
        
    
def OpenFile():
    global filename
    file = askopenfile(mode='r')
    if file:
        filename = file.name
        text.delete(1.0, END)
        text.insert(1.0, file.read())
        file.close()
    
    
root = Tk()
root.title("My Python Text Editor")
root.geometry("600x500")

text = Text(root, wrap="word", undo=True)
text.pack(expand=True, fill="both")

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=False)
filemenu.add_command(label="New", command=NewFile)
filemenu.add_command(label="Open", command=OpenFile)
filemenu.add_command(label="Save", command=SaveFile)
filemenu.add_command(label="Save As...", command=SaveAs)
filemenu.add_separator()
filemenu.add_command(label="Quit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

root.config(menu=menubar)
root.mainloop()