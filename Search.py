# Import libraries
import sqlite3
from tkinter import *
from tkinter.ttk import Treeview


class Search:

  def __init__(self, form_type):
    self.show_all_form = Tk()
    self.show_all_form.geometry("900x900")
    self.form_type = form_type

    if self.form_type == 'artists':
      self.title = 'Show All Artists'
      self.columns = ('Artist Name', 'Genre Name')
    else:
      self.title = 'Show All Albums'
      self.columns = ('Album Title', 'Artist Name', 'Media Type')
      # tree = Treeview(self.show_all_form, columns=columns, show='headings')

    self.show_all_form.title(self.title)
    self.show_all_form.iconbitmap('img/music.ico')

    self.v_albums = ''
    self.v_artists = ''

    self.conn = sqlite3.connect('db/MusicInventory.db')
    self.c = self.conn.cursor()

    self.main_form()

  def main_form(self):
    lbl_mm = Label(self.show_all_form, text=self.title, pady=10, font=('MS Serif', 18))
    lbl_mm.grid(row=0, column=0)

    if self.form_type == 'artists':
      self.show_all_artists()
    else:
      self.show_all_albums()

  def show_all_artists(self):
    self.v_artists = """select ar.ArtistName, g.GenreName from Artist as ar, Genre as g
    where ar.GenreID = g.GenreId"""

    r = self.c.execute(self.v_artists).fetchall()
    rows = [self.columns] + r

    # find total number of rows and
    # columns in list
    total_rows = len(rows)
    total_cols = len(rows[0])

    # code for creating table
    for i in range(total_rows):
      for j in range(total_cols):
        e = Entry(self.show_all_form, width=20, fg='black', font=('Arial', 12))
        e.grid(row=i, column=j)
        e.insert(END, rows[i][j])

    self.show_all_form.grid()

  def show_all_albums(self):
    self.v_albums = """select al.AlbumTitle, ar.ArtistName, m.MediaTypeName from Album as al, Artist as ar, MediaType as m
    where al.ArtistId = ar.ArtistId and al.MediaTypeId = m.MediaTypeId"""

    r = self.c.execute(self.v_albums).fetchall()
    rows = [self.columns] + r

    # find total number of rows and
    # columns in list
    total_rows = len(rows)
    total_cols = len(rows[0])

    # code for creating table
    for i in range(total_rows):
      for j in range(total_cols):
        e = Entry(self.show_all_form, fg='black', font=('Arial', 12))
        e.grid(row=i, column=j)
        e.insert(END, rows[i][j])

    # columnwidth = {'0': 7, '1': 12, '2': 20, '3': 35, '4': 15, '5': 15, '6': 22}
    # self.table.width(**columnwidth)

    self.show_all_form.grid()

