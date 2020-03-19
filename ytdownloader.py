import tkinter as tk
from tkinter import filedialog, Button

from pytube import YouTube

def downloadVid():
    global E1, E2
    string =E1.get()
    string2 = E2.get()
    yt = YouTube(str(string))
    videos = yt.streams.filter()
    s=1
    for v in videos:
        print(str(s) + '.' + str(v))
        s +=1
    n=int(input("Enter your choice"))
    vid=videos[n-1]
    destination=str(input("Enter your destination"))
    vid.download(destination)
    print(yt.filename+"\n Ha been downloaded")
root=tk.Tk()

def saveFile():
    path = filedialog.askdirectory()
    return path

w=tk.Label(root,text="Youtube Downloader")
w.grid(column=0, row=1)

E1=tk.Entry(root,bd=5)
E1.grid(column=0, row=2)
E2=tk.Entry(root,bd=5)
E2.grid(column=0, row=3)

choice = tk.Listbox(root)
choice.grid(column=0, row=6)

saveBtn=tk.Button(root,text="Browse",command=saveFile)

button=tk.Button(root,text="Download",command=downloadVid)
button.grid(column=0, row=5)
saveBtn.grid(column=0, row=4)


root.mainloop()