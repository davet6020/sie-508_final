# Import libraries
import sqlite3
from tkinter import *
from tkinter.ttk import Treeview


class ShowAllForm:

  def __init__(self, form_type):
    self.show_all_form = Tk()
    self.show_all_form.geometry("900x900")
    self.form_type = form_type

    if self.form_type == 'artists':
      self.title = 'Show All Artists'
      self.columns = ('Artist Name', 'Genre Name')
    elif self.form_type == 'albums':
      self.title = 'Show All Albums'
      self.columns = ('Album Title', 'Artist Name', 'Media Type')
    elif self.form_type == 'genre':
      self.title = 'Show All Genre Types'
      self.columns = ('Genre Name',)
    elif self.form_type == 'media':
      self.title = 'Show All Media Types'
      self.columns = ('Media Type Name',)
    else:
      pass

    self.show_all_form.title(self.title)
    self.show_all_form.iconbitmap('img/music.ico')

    self.v_artists = ''
    self.v_albums = ''
    self.v_genre = ''
    self.v_media = ''

    self.conn = sqlite3.connect('db/MusicInventory.db')
    self.c = self.conn.cursor()

    self.main_form()

    # Close DB connection
    self.conn.close()

  def main_form(self):
    lbl_mm = Label(self.show_all_form, text=self.title, pady=10, font=('MS Serif', 18))
    # lbl_mm.grid(row=0, column=0)

    if self.form_type == 'artists':
      self.show_all_artists()
    elif self.form_type == 'albums':
      self.show_all_albums()
    elif self.form_type == 'genre':
      self.show_all_genre()
    elif self.form_type == 'media':
      self.show_all_media()
    else:
      pass

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
    self.v_media = """select al.AlbumTitle, ar.ArtistName, m.MediaTypeName from Album as al, Artist as ar, MediaType as m
    where al.ArtistId = ar.ArtistId and al.MediaTypeId = m.MediaTypeId"""

    r = self.c.execute(self.v_media).fetchall()
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

    self.show_all_form.grid()

  def show_all_genre(self):
    self.v_genre = """select g.GenreName from Genre as g"""

    r = self.c.execute(self.v_genre).fetchall()
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

    self.show_all_form.grid()

  def show_all_media(self):
    self.v_media = """select m.MediaTypeName from MediaType as m """

    r = self.c.execute(self.v_media).fetchall()
    rows = [self.columns] + r
    print(self.v_media)
    print(rows)

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

    self.show_all_form.grid()

