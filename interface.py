from tkinter.filedialog import askopenfilename, asksaveasfilename
from HuffmanEnc import *
import huffManDecompressor
import tkinter as tk

global filepath
filepath=False


def open_file():
    """Open a file for editing."""
    global filepath
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    text_info.delete(1.0, tk.END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        text_info.insert(tk.END, text)
    window.title(filepath)
    process_info.config(text="Opened a file")
    return filepath

def save_file():
    """Save the current file as a new file."""
    global filepath
    filepath = asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text = text_info.get(1.0, tk.END)
        output_file.write(text)
    window.title(filepath)
    process_info.config(text="file saved")
    return filepath

#Save and compress function
def saveandcompress():
    path = save_file()
    main = HuffmanEnCoding(path)
    comPath = main.compress()
    process_info.config(text="file saved and compressed")
    return

#compress function
def compress():
    path=filepath
    main = HuffmanEnCoding(path)
    comPath = main.compress()
    process_info.config(text="file compressed")
    return    

#Decompress function
def decompress():
    global filepath
    filepath = askopenfilename(
        filetypes=[("Bin files", "*.bin"), ("All Files", "*.*")]
    )
    filepath = huffManDecompressor.decompress(filepath)
    if not filepath:
        return
    text_info.delete(1.0, tk.END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        text_info.insert(tk.END, text)    
    process_info.config(text="Binary file decompressed")    
    return



#Configuring Tkinter Root window
window=tk.Tk()
window.title("File Compression")
window.minsize(height=300,width=550)
w=window.winfo_screenwidth() 
h =window.winfo_screenheight()
window.geometry("%dx%d+0+0" % (w, h))

#Adding scrollbar to that window
scrollbar=tk.Scrollbar(window)
scrollbar.pack(side='right',fill='y')

#menu frame to display buttons
frame_buttons=tk.Frame(window)
frame_buttons.pack(side='top',fill='x')

#Configuring and packing frame buttons
open_btn=tk.Button(frame_buttons,text='Open',command=open_file,font=("URW Palladio L","15","bold"))
save_btn=tk.Button(frame_buttons,text='Save As',command=save_file,font=("URW Palladio L","15","bold"))
saveAndEncode=tk.Button(frame_buttons,text='Save and Compress',command=saveandcompress,font=("URW Palladio L","15","bold"))
EncodeFile=tk.Button(frame_buttons,text='Compress',command=compress,font=("URW Palladio L","15","bold"))
DecodeFile=tk.Button(frame_buttons,text='Decompress',command=decompress,font=("URW Palladio L","15","bold"))

open_btn.pack(side='left',fill='both',expand=True)
save_btn.pack(side='left',fill='both',expand=True)
saveAndEncode.pack(side='left',fill='both',expand=True)
EncodeFile.pack(side='left',fill='both',expand=True)
DecodeFile.pack(side='left',fill='both',expand=True)

open_btn.config(bg="#242424",fg="#08BD80",borderwidth=0,highlightthickness=0)
save_btn.config(bg="#242424",fg="#08BD80",borderwidth=0,highlightthickness=0)
saveAndEncode.config(bg="#242424",fg="#08BD80",borderwidth=0,highlightthickness=0)
EncodeFile.config(bg="#242424",fg="#08BD80",borderwidth=0,highlightthickness=0)
DecodeFile.config(bg="#242424",fg="#08BD80",borderwidth=0,highlightthickness=0)

#Label to display background process at bottom of window
process_info=tk.Label(window,height="1")
process_info.pack(side='bottom',fill='x')
process_info.config(bg="#242424",fg="#08BD80",borderwidth=0,highlightthickness=0)

#Text field
text_info=tk.Text(window,width=w,height=h,yscrollcommand=scrollbar.set)
scrollbar.config(command=text_info.yview)
text_info.pack(side=tk.LEFT, expand=1,fill='both')
text_info.config(bg="#323333",fg="white",borderwidth=0,highlightthickness=0,font=("URW Palladio L","18"))


window.mainloop()