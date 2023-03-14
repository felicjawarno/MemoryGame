# -*- coding: utf-8 -*-
"""Untitled8.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1z_OkOjPSFdmWv3X39Dc36hrdNfxLNfyZ
"""
from tkinter import *
import numpy as np
import random
from PIL import Image
import os
import pickle 
import tkinter as tk
import matplotlib
matplotlib.use('Agg')
from tkinter import messagebox

class Memory():

  def __init__(self, level, score, moves):
     
     self.moves = moves
     self.score = score
     self.matrx = generating_matrix(level)
  
  def odkrywanie(self, a, b, c, d):
    A = self.matrx
    if A[a][b] == A[c][d]:
      self.score += 1
      A[a][b] = None
      A[c][d] = None
    self.moves += 1
  
  def save(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self.__dict__, file)
  
  def load(self, filename):
    with open(filename, 'rb') as file:
        self.__dict__ = pickle.load(file)


def generating_matrix(a):
  if a == 1:
    t = [1 for i in range(16)]
    A = np.zeros((4, 4))
    for i in range(len(A)):
      for j in range(len(A[0])):
        k = random.randint(0, 15)
        while t[k] == 0:
          k = random.randint(0, 15)
        A[i][j] = (k + 1)
        t[k] = 0
        if k + 1 > 8:
          k -= 8
        A[i][j] = (k + 1)
  if a == 2:
    t = [1 for i in range(36)]
    A = np.zeros((6, 6))
    for i in range(len(A)):
      for j in range(len(A[0])):
        k = random.randint(0, 35)
        while t[k] == 0:
          k = random.randint(0, 35)
        A[i][j] = (k + 1)
        t[k] = 0
        if k + 1 > 18:
          k -= 18
        A[i][j] = (k + 1)
  return A

#Interface
root = tk.Tk()
root.geometry("700x600")
root.title("Memory")

my_frame = Frame(root)
my_frame.pack(pady=50)


def button_click():
    return
#click_btn = PhotoImage(file='Bambi.jpg')
#image = Image.open("Bambi.jpg");
#click_btn = image.resize(50, 50);


a0 = Button(my_frame, text=' ', font=("Helvetica", 20), height=3, width=6, command=lambda: button_click(a0, 0),
               relief="groove")
a1 = Button(my_frame, text=' ', font=("Helvetica", 20), height=3, width=6, command=lambda: button_click(a1, 0),
               relief="groove")
a2 = Button(my_frame, text=' ', font=("Helvetica", 20), height=3, width=6, command=lambda: button_click(a2, 0),
               relief="groove")
a3 = Button(my_frame, text=' ', font=("Helvetica", 20), height=3, width=6, command=lambda: button_click(a3, 0),
               relief="groove")
a4 = Button(my_frame, text=' ', font=("Helvetica", 20), height=3, width=6, command=lambda: button_click(a4, 0),
               relief="groove")
a5 = Button(my_frame, text=' ', font=("Helvetica", 20), height=3, width=6, command=lambda: button_click(a5, 0),
               relief="groove")
a6 = Button(my_frame, text=' ', font=("Helvetica", 20), height=3, width=6, command=lambda: button_click(a6, 0),
               relief="groove")
a7 = Button(my_frame, text=' ', font=("Helvetica", 20), height=3, width=6, command=lambda: button_click(a7, 0),
               relief="groove")
a8 = Button(my_frame, text=' ', font=("Helvetica", 20), height=3, width=6, command=lambda: button_click(a8, 0),
               relief="groove")
a9 = Button(my_frame, text=' ', font=("Helvetica", 20), height=3, width=6, command=lambda: button_click(a9, 0),
               relief="groove")
a10 = Button(my_frame, text=' ', font=("Helvetica", 20), height=3, width=6, command=lambda: button_click(a10, 0),
               relief="groove")
a11 = Button(my_frame, text=' ', font=("Helvetica", 20), height=3, width=6, command=lambda: button_click(a11, 0),
               relief="groove")
a12 = Button(my_frame, text=' ', font=("Helvetica", 20), height=3, width=6, command=lambda: button_click(a12, 0),
               relief="groove")
a13 = Button(my_frame, text=' ', font=("Helvetica", 20), height=3, width=6, command=lambda: button_click(a13, 0),
               relief="groove")
a14 = Button(my_frame, text=' ', font=("Helvetica", 20), height=3, width=6, command=lambda: button_click(a14, 0),
               relief="groove")
a15 = Button(my_frame, text=' ', font=("Helvetica", 20), height=3, width=6, command=lambda: button_click(a15, 0),
               relief="groove")

a0.grid(row=0, column=0)
a1.grid(row=0, column=1)
a2.grid(row=0, column=2)
a3.grid(row=0, column=3)

a4.grid(row=1, column=0)
a5.grid(row=1, column=1)
a6.grid(row=1, column=2)
a7.grid(row=1, column=3)

a8.grid(row=2, column=0)
a9.grid(row=2, column=1)
a10.grid(row=2, column=2)
a11.grid(row=2, column=3)

a12.grid(row=3, column=0)
a13.grid(row=3, column=1)
a14.grid(row=3, column=2)
a15.grid(row=3, column=3)


#s0 = Button(my_frame, text= 'Save the game', font=("Helvetica", 20), height=3, width=6, command=lambda: m1.save(s0, 0),
               #relief="groove")


root.mainloop()