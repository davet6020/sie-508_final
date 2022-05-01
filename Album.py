# Import libraries
import sqlite3
import tkinter

from tkinter import *

class Album:

  def __init__(self):
    self.show_albums = Tk()
    self.show_albums.geometry("900x500")
    self.title = 'Show All Albums'
    self.columns = ('Album Title', 'Artist Name', 'Media Type')
    self.show_albums.title(self.title)
    self.show_albums.iconbitmap('img/music.ico')

    self.srch_val = ''
    self.conn = sqlite3.connect('db/MusicInventory.db')
    self.c = self.conn.cursor()

  def search(self, srch_val):
    self.srch_val = srch_val

    # Album Search by Album Name to see if it is in the inventory
    q = """select al.AlbumTitle, ar.ArtistName, m.MediaTypeName from Album as al, Artist as ar, MediaType as m
                  where al.ArtistId = ar.ArtistId and al.MediaTypeId = m.MediaTypeId and lower(al.AlbumTitle) = '""" + str(
      self.srch_val) + "'"

    r = self.c.execute(q).fetchall()

    self.show(r)

    print('IM IN THE ALBUM CLASS')
    print(q)
    print(r)

  def show(self, r):
    lbl_mm = Label(self.show_albums, text=self.title, pady=10, font=('MS Serif', 18))
    lbl_mm.grid(row=0, column=0)

    rows = [self.columns] + r

    # find total number of rows and
    # columns in list
    total_rows = len(rows)
    total_cols = len(rows[0])

    # code for creating table
    for i in range(total_rows):
      for j in range(total_cols):
        e = Entry(self.show_albums, fg='black', font=('Arial', 12))
        e.grid(row=i, column=j)
        e.insert(END, rows[i][j])

    self.show_albums.grid()
