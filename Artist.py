# Import libraries
import sqlite3
import tkinter
import tkinter.ttk

from tkinter import *

class Artist:

  def __init__(self):
    self.show_artist = Tk()
    self.show_artist.geometry("900x500")
    self.title = 'Show All Artists'
    self.columns = ('Artist Name', 'Album Title', 'Media Type')
    self.show_artist.title(self.title)
    self.show_artist.iconbitmap('img/music.ico')

    self.srch_val = ''
    self.conn = sqlite3.connect('db/MusicInventory.db')
    self.c = self.conn.cursor()

  def search(self, srch_val):
    self.srch_val = srch_val

    # Artist Search by Artist name to see all albums associated to that Artist
    q = """select ar.ArtistName, al.AlbumTitle, m.MediaTypeName from Album as al, Artist as ar, MediaType as m
                    where al.ArtistId = ar.ArtistId and al.MediaTypeId = m.MediaTypeId and lower(ar.ArtistName) = '""" + str(
      self.srch_val) + "'"

    r = self.c.execute(q).fetchall()
    self.show(r)

  def show(self, r):
    lbl_mm = Label(self.show_artist, text=self.title, pady=10, font=('MS Serif', 18))
    lbl_mm.grid(row=0, column=0)

    rows = [self.columns] + r

    # find total number of rows and
    # columns in list
    total_rows = len(rows)
    total_cols = len(rows[0])

    # code for creating table
    for i in range(total_rows):
      for j in range(total_cols):
        e = Entry(self.show_artist, width=30, fg='black', font=('Arial', 12))
        e.grid(row=i, column=j)
        e.insert(END, rows[i][j])

    self.show_artist.grid()
