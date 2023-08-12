import socket
from threading import Thread
from tkinter import *
from tkinter import ttk, filedialog
import ftplib
import os
import time
import ntpath
from pathlib import Path
from playsound import playsound
import pygame
from pygame import mixer

SERVER = None
IP_ADDRESS = '127.0.0.1'
PORT = 8050
BUFFER_SIZE = 4096

name = None
listbox =  None
infoLabel = None
filePathLabel = None

song_counter = 0
song_selected = None

font = "Calibri"

def play():
  global song_selected
  song_selected = listbox.get(ANCHOR)

  pygame
  mixer.init()
  mixer.music.load("shared_files/"+song_selected)
  mixer.music.play()
  if(song_selected != ""):
    infoLabel.configure(text="Now Playing: "+song_selected)
  else:
    infoLabel.configure(text="")

def stop():
  pygame
  mixer.init()
  mixer.music.load("shared_files/"+song_selected)
  mixer.music.pause()
  infoLabel.configure(text="")

def resume():
  pygame
  mixer.init()
  mixer.music.load("shared_files/"+song_selected)
  mixer.music.unpause()

def pause():
  pygame
  mixer.init()
  mixer.music.load("shared_files/"+song_selected)
  mixer.music.pause()

def musicWindow():
  global listbox, infoLabel
  global song_counter

  window = Tk()
  window.title("Music Window")
  window.geometry("300x300")
  window.configure(bg="#87CEFA")

  selectLabel = Label(window, text="Select Song", bg="#87CEFA", font=(font, 8))
  selectLabel.place(x=2, y=1)

  listbox = Listbox(window, height=10, width=39, activestyle="dotbox", bg="#87CEFA", borderwidth=2, font=(font, 10))
  listbox.place(x=10, y=18)

  for file in os.listdir("shared_files"):
    fileName = os.fsdecode(file)
    listbox.insert(song_counter, fileName)
    song_counter = song_counter + 1

  scrollbar1 = Scrollbar(listbox)
  scrollbar1.place(relheight=1, relx=1)
  scrollbar1.config(command=listbox.yview)

  playButton = Button(window, text="Play", width=10, bg="#87CEEB", bd=1, font=(font, 10), command=play)
  playButton.place(x=20, y=200)

  resumeButton = Button(window, text="Resume", width=10, bg="#87CEEB", bd=1, font=(font, 10), command=resume)
  resumeButton.place(x=20, y=250)

  stopButton = Button(window, text="Stop", width=10, bg="#87CEEB", bd=1, font=(font, 10), command=stop)
  stopButton.place(x=110, y=200)

  pauseButton = Button(window, text="Pause", width=10, bg="#87CEEB", bd=1, font=(font, 10), command=pause)
  pauseButton.place(x=110, y=250)

  uploadButton = Button(window, text="Upload", width=10, bg="#87CEEB", bd=1, font=(font, 10))
  uploadButton.place(x=200, y=200)

  downloadButton = Button(window, text="Download", width=10, bg="#87CEEB", bd=1, font=(font, 10))
  downloadButton.place(x=200, y=250)

  infoLabel = Label(window, text="", bg="#87CEEB", fg="#00F", font=(font, 8))
  infoLabel.place(x=4, y=280)

  window.resizable(False, False)
  window.mainloop()


def setup():
  global SERVER, IP_ADDRESS, PORT
  SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  SERVER.connect((IP_ADDRESS, PORT))

  musicWindow()

setup()