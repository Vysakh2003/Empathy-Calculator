import tkinter as tk
import tkinter.font as font
import os
from sample import *

window=tk.Tk()
window.title("ANALYSA - A Perfect Mentor")
window.geometry("1200x730")

def call_text():
    window.destroy()
    text_analysis_func(window)

def call_text_view():
    new_window = tk.Toplevel()
    new_window.geometry("1500x700")
    new_window.title("Teacher - TEXT RESULT")
    la = tk.Label(new_window, text = "RESULT OF TEXT ANALYSIS OF STUDENT",font =("Tkdefault", 20))
    la.pack(pady=5)
    la['font'] = font.Font(size=20, weight='bold')
    with open("text_result.txt", "r") as f:
        tk.Label(new_window, text=f.read(),font =("Tkdefault", 20)).pack()

def call_audio_view():
    new_window1 = tk.Toplevel()
    new_window1.geometry("1500x700")
    new_window1.title("Teacher - AUDIO RESULT")
    la = tk.Label(new_window1, text = "RESULT OF AUDIO ANALYSIS OF STUDENT",font =("Tkdefault", 20))
    la.pack(pady=5)
    la['font'] = font.Font(size=20, weight='bold')
    with open("audio_result.txt", "r") as f1:
        tk.Label(new_window1, text=f1.read(),font =("Tkdefault", 19)).pack()

def call_audio():
    window.destroy()
    import Main

def redirect():

    window.destroy()
    window.quit()
    os.system("python E:\Hackathon\SIH2022-main\code\login.py")



def page(window):
    la = tk.Label(window, text = "Choose Your Login",font =("Tkdefault", 20))
    la.pack(pady=5)
    la['font'] = font.Font(size=20, weight='bold')
    teacher = tk.Button(window,text="TEACHER",font=("Courier", 10),width=50,height=13,bg='green',fg='#ffffff',activebackground = "pink", activeforeground = "blue",command=teacher1)  # command missing
    teacher.pack(pady="20", padx="20")
    teacher['font'] = font.Font(size=14, weight='bold')
    student = tk.Button(window,text="STUDENT",font=("Courier", 10),width=50,height=13,bg='blue',fg='#ffffff',activebackground = "pink", activeforeground = "blue",command=student1)
    student.pack(pady="20", padx="20")
    student['font'] = font.Font(size=14, weight='bold')
    



def teacher1():
    newwindow2=tk.Toplevel()
    newwindow2.geometry("1300x680")
    la = tk.Label(newwindow2, text = "Choose To View",font =("Tkdefault", 20))
    la.pack(pady=5)
    la['font'] = font.Font(size=20, weight='bold')
    fnd = tk.Button(newwindow2,text="TEXT RESULT",font=("Courier", 8),width=35,height=7,bg='green',fg='#ffffff',activebackground = "pink", activeforeground = "blue", command=call_text_view)
    fnd.pack(pady=20)
    fnd['font'] = font.Font(size=14, weight='bold')
    fnd = tk.Button(newwindow2,text="AUDIO RESULT",font=("Courier", 8),width=35,height=7,bg='blue',fg='#ffffff',activebackground = "pink", activeforeground = "blue",command=call_audio_view)
    fnd.pack(pady=20)
    fnd['font'] = font.Font(size=14, weight='bold')
    submit_button = tk.Button(newwindow2, text="Logout", default='active',activebackground = "pink", activeforeground = "blue",height=2, width=20,  command=redirect)
    submit_button.pack(pady=20)
    submit_button['font'] = font.Font(size=18, weight='bold')



def student1():
    newwindow1=tk.Toplevel()
    newwindow1.geometry("1300x680")
    la = tk.Label(newwindow1, text = "Choose To Analyse",font =("Tkdefault", 20))
    la.pack(pady=5)
    la['font'] = font.Font(size=20, weight='bold')
    fnd = tk.Button(newwindow1,text="TEXT ANALYSIS",font=("Courier", 8),width=35,height=7,bg='green',fg='#ffffff',activebackground = "pink", activeforeground = "blue", command=call_text)
    fnd.pack(pady=20)
    fnd['font'] = font.Font(size=14, weight='bold')
    fnd = tk.Button(newwindow1,text="AUDIO ANALYSIS",font=("Courier", 8),width=35,height=7,bg='blue',fg='#ffffff',activebackground = "pink", activeforeground = "blue",command=call_audio)
    fnd.pack(pady=20)
    fnd['font'] = font.Font(size=14, weight='bold')
    submit_button = tk.Button(newwindow1, text="Logout", default='active',activebackground = "pink", activeforeground = "blue",height=2, width=20, command=redirect)
    submit_button.pack(pady=20)
    submit_button['font'] = font.Font(size=18, weight='bold')



page(window)
window.mainloop()
