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


def win(window, window_title, video_source=0):
    window = window
    window.title(window_title)
    video_source = video_source
    ok=False
    
    canvas = tk.Canvas(window, width = vid.width, height = id.height)
    canvas.pack()
    btn_start=tk.Button(window, text='START RECORDING', command=open_camera)
    btn_start.pack(side=tk.LEFT)
    btn_stop=tk.Button(window, text='STOP RECORDING', command=close_camera)
    btn_stop.pack(side=tk.LEFT)
    
    btn_audio=tk.Button(window, text='VOICE ANALYSIS', command=audio_analysis)
    btn_audio.pack(side=tk.LEFT)
    
    btn_quit=tk.Button(window, text='QUIT', command=quit)
    btn_quit.pack(side=tk.LEFT)
    
    window.mainloop()

    
    
def start_audio_analysis(self):
    global duration

    newwindow=tk.Toplevel()
    newwindow.geometry("640x480")
    newwindow.title("Audio Analysis")

    L = tk.Label(newwindow, text = "AUDIO ANALYSIS",font=("Courier", 20))
    L.pack()

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
    # s6=te.get_emotion(detected_text)
    # T.insert(tk.END,s6)






def audio_analysis():
    t1 = threading.Thread(start_audio_analysis)
    t1.start()
    # start_audio_analysis()


App(tk.Tk(),'Video Recorder')