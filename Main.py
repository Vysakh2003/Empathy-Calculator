import tkinter as tk
import cv2

import PIL.Image, PIL.ImageTk
import time
import datetime as dt
import pyaudio
import threading
import wave
import AudioS2TWPMAnalysis as aa
import VoiceSpectroChroma as Voice
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,NavigationToolbar2Tk)



font = "courier"
fontsize = 15
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
record_on = False
frames = []
p = pyaudio.PyAudio()
stream = None
counter = 0
#duration = 10

class App:
    def __init__(self, window, window_title="", video_source=0):
        self.window = window
        self.window.title(window_title)
        self.video_source = video_source
        self.ok=False
        self.canvas = tk.Canvas(window, width = 800, height = 500)
        self.canvas.pack()
        self.btn_audio=tk.Button(window, text='VOICE ANALYSIS',activebackground = "pink", activeforeground = "blue", bg='#0052cc',fg='#ffffff',height=4, width=30, command=self.audio_analysis)
        self.btn_audio.pack(side=tk.LEFT)
      
        self.btn_quit=tk.Button(window, text='QUIT',activebackground = "pink", activeforeground = "blue", bg='#0052cc',fg='#ffffff',height=4, width=30, command=quit)
        self.btn_quit.pack(side=tk.LEFT)
        self.delay=10
        self.window.mainloop()

    
    
    def start_audio_analysis(self):
        global duration

        newwindow=tk.Toplevel()
        newwindow.geometry("640x480")
        newwindow.title("Audio Analysis")

        L = tk.Label(newwindow, text = "AUDIO ANALYSIS",font=("Courier", 20))
        L.pack()

        al = tk.Label(newwindow, text = "Please wait calibrating mic...\nSpeak After Few Mins..",font=("Courier", 13))
        al.pack(pady=20)

        T = tk.Text(newwindow,font=("Courier", 14),height=18)
        T.pack()

        plot_button = tk.Button(newwindow, text = "Plot Spectrogram", command = Voice.Spectrogramplot, width = '14', height='1')
        plot_button.pack()    

        plot_button = tk.Button(newwindow, text = "Plot Chromagram", command = Voice.Chromagramplot, width = '14', height='1')
        plot_button.pack()      
        duration = detected_text = None
        detected_text,duration = aa.speech_to_text()
        #print(detected_text , duration)
        s1 = "\n\nSpeech Content = "+detected_text
        T.insert(tk.END, s1)
        word_count = aa.No_of_words()
        s2 = "\n\nNumber of Words = "+str(word_count)+" Words"
        T.insert(tk.END, s2)
        s3 = "\n\nDuration of Speech = "+str(duration)+" Seconds"
        T.insert(tk.END, s3)
        wpm=aa.WPM(duration)
        s4="\n\nSpeed of Speech = "+str(wpm)+" Words Per Minute (WPM)"
        T.insert(tk.END, s4)
        tips=aa.get_tips(wpm)
        common_tips=aa.common_tips()
        s5="\n\nTips/Suggestions : \n"+tips+common_tips+"\n\n"
        T.insert(tk.END, s5)
       

    def plot(self):
        global dct,cnt
        names = dct.values()
        values = cnt.values()

        newwindow2=tk.Toplevel()
        newwindow2.title("Bar Graph - Video Analysis")
        newwindow2.geometry("600x410")
        f = Figure(figsize = (15, 4),dpi = 100)
        canvas = FigureCanvasTkAgg(f,master = newwindow2)
        NavigationToolbar2Tk(canvas, newwindow2)
        ax = f.add_subplot()
        ax.bar(names,values)
        ax.set_xlabel('Emotion')
        canvas.draw()
        canvas.get_tk_widget().pack()

    

    def audio_analysis(self):
        t1 = threading.Thread(target = self.start_audio_analysis)
        t1.start()
  


 

App(tk.Tk(),'Audio  Recorder')