# Import libraries
import sqlite3
import tkinter
import tkinter.ttk

from tkinter import *

class Genre:

  def __init__(self):
    self.show_genre = Tk()
    self.show_genre.geometry("900x900")
    self.title = 'Show All Artists by Genre'
    self.columns = ('Artist Name', 'Genre Name')
    self.show_genre.title(self.title)
    self.show_genre.iconbitmap('img/music.ico')

    self.srch_val = ''
    self.conn = sqlite3.connect('db/MusicInventory.db')
    self.c = self.conn.cursor()

  def search(self, srch_val):
    if len(srch_val) < 1:
      self.columns = ('Genre Name',)
      q = """select g.GenreName from Genre as g order by g.GenreName"""
    else:
      self.srch_val = srch_val
      q = """select ar.ArtistName, g.GenreName from Artist as ar, Genre as g
                          where ar.GenreId = g.GenreId and lower(g.GenreName) = '""" + str(
        self.srch_val) + "' order by ar.ArtistName"

    r = self.c.execute(q).fetchall()
    self.show(r)

  def show(self, r):
    rows = [self.columns] + r

    # find total number of rows and
    # columns in list
    total_rows = len(rows)
    total_cols = len(rows[0])

    # code for creating table
    for i in range(total_rows):
      for j in range(total_cols):
        e = Entry(self.show_genre, width=30, fg='black', font=('Arial', 12))
        e.grid(row=i, column=j)
        e.insert(END, rows[i][j])

    self.show_genre.grid()
