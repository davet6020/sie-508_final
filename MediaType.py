# Import libraries
import sqlite3
import tkinter
import tkinter.ttk

from tkinter import *

class MediaType:

  def __init__(self):
    self.show_media_type = Tk()
    self.show_media_type.geometry("900x900")
    self.title = 'Show All Albums by MediaType'
    self.columns = ('Album Title', 'Media Type')
    self.show_media_type.title(self.title)
    self.show_media_type.iconbitmap('img/music.ico')
    self.rb_srch = IntVar()
    self.rb_srch.set("1")

    self.srch_val = ''
    self.conn = sqlite3.connect('db/MusicInventory.db')
    self.c = self.conn.cursor()

  # This is the crud form with all entrys. Will be toggled for create, update and delete
  def crud(self, form_type):

    # Create frame for search controls
    lbl_mm = Label(self.show_media_type, text='CRUD', pady=10, font=('MS Serif', 18))
    lbl_mm.grid(row=0, column=0)

    crud = LabelFrame(self.show_media_type, padx=10, pady=10)
    crud.grid(padx=10, pady=10)

    Radiobutton(crud, text='Create', variable=self.rb_srch, value=1).grid(row=0, column=0)
    Radiobutton(crud, text='Update', variable=self.rb_srch, value=2).grid(row=0, column=1, sticky=(W))
    Radiobutton(crud, text='Delete', variable=self.rb_srch, value=3).grid(row=1, column=0)

    if form_type == 'create':       # Set up stuff to create new entry
      title = 'Create new record'
    elif form_type == 'update':     # Set up stuff to update existing entry
      pass
    elif form_type == 'delete':     # Set up stuff to delete existing entry
      pass
    else:
      pass

    media_type_name = Entry(crud, width=6, font=('Ariel', 13))
    media_type_name.grid(row=4, column=1, padx=20, pady=10)

    # Create frame for buttons
    frame_butts = LabelFrame(crud, padx=10, pady=10)
    frame_butts.grid(padx=10, pady=10)

    btn_show_albums = Button(frame_butts, width=15, text="Show All Albums", font=('Ariel', 10),
                             command=lambda: self.show_all_form("albums"))
    btn_show_albums.grid(row=0, column=0, padx=20, pady=10)

    btn_show_artists = Button(frame_butts, width=15, text="Show All Artists", font=('Ariel', 10),
                              command=lambda: self.show_all_form("artists"))
    btn_show_artists.grid(row=0, column=1, padx=20, pady=10)

    btn_exit = Button(frame_butts, width=15, text="Exit", font=('Ariel', 10), command=self.show_media_type.destroy)
    btn_exit.grid(row=0, column=2, padx=20, pady=10, sticky=(W))

  def search(self, srch_val):
    if len(srch_val) < 1:
      self.columns = ('Media Type',)
      q = """select m.MediaTypeName from MediaType as m order by m.MediaTypeName"""
    else:
      self.srch_val = srch_val
      q = """select al.AlbumTitle, m.MediaTypeName from Album as al, MediaType as m
                    where al.MediaTypeId = m.MediaTypeId and lower(m.MediaTypeName) = '""" + \
          str(self.srch_val) + "' order by al.AlbumTitle"

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
        e = Entry(self.show_media_type, width=30, fg='black', font=('Arial', 12))
        e.grid(row=i, column=j)
        e.insert(END, rows[i][j])

    self.show_media_type.grid()
