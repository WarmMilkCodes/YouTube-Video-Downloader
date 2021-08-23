import tkinter as tk
from pytube import YouTube

def Download_Video():
    url = YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    tk.Label(window,text = 'Success!', font = 'arial 15 bold', fg='white', bg='black', padx= 2).place(x=485, y=145)

window=tk.Tk()
window.geometry("600x200")
window.config(bg="#FF0000")
window.resizable(width=False,height=False)
window.title('YouTube Video Downloader')

link = tk.StringVar()

tk.Label(window,text = '    YouTube Video Downloader    ', font='arial 20 bold', fg="Black", bg="#FF0000").pack()
tk.Label(window, text = 'Paste your YouTube link below ', font='arial 15 bold', bg='#FF0000').place(x=140,y=60)

link_enter = tk.Entry(window, width = 53,textvariable = link, font = 'arial 15 bold', bg='White').place(x=5,y=100)

tk.Button(window,text = 'DOWNLOAD VIDEO', font = 'arial 15 bold', fg='white', bg='black', padx= 2,command=Download_Video).place(x=190, y=140)


window.mainloop()
