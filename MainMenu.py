# Import libraries
import sqlite3
import tkinter

from Album import Album
from Artist import Artist
from Genre import Genre
from MediaType import MediaType
from ShowAllForm import ShowAllForm
from tkinter import *
from idlelib.tooltip import Hovertip

class MainMenu:

  def __init__(self):
    self.gui = Tk()
    self.gui.geometry("800x800")
    self.gui.title('Music Collection Inventory')
    self.gui.iconbitmap('img/music.ico')
    self.rb_srch = IntVar()
    self.rb_srch.set("1")
    self.form_type = ''
    self.srch_type = ''
    self.srch_val = ''
    self.thing_to_crud = ''
    self.txt_srch = StringVar()
    self.txt_srch.set('')
    self.txt_srch.trace("w", self.printer)
    self.what_widget = ''
    self.msg = ''

    self.conn = sqlite3.connect('db/MusicInventory.db')
    self.c = self.conn.cursor()

    self.main_form()

  def printer(self, index, mode):
    print(self.txt_srch.get())

  def main_form(self):
    lbl_mm = Label(self.gui, text="Main Menu", pady=10, font=('MS Serif', 18))
    lbl_mm.grid(row=0, column=0)

    # Create frame for search controls
    frame_srch = LabelFrame(self.gui, padx=10, pady=10)
    frame_srch.grid(padx=10, pady=10)

    Radiobutton(frame_srch, text='Album', variable=self.rb_srch, value=1).grid(row=2, column=0)
    Radiobutton(frame_srch, text='Artist', variable=self.rb_srch, value=2).grid(row=2, column=1, sticky=(W))
    Radiobutton(frame_srch, text='Genre', variable=self.rb_srch, value=3).grid(row=3, column=0)
    Radiobutton(frame_srch, text='Media', variable=self.rb_srch, value=4).grid(row=3, column=1, sticky=(W))

    btn_srch = Button(frame_srch, width=15, text="Search", font=('Ariel', 10),
                      command=lambda: self.search(self.rb_srch.get(), self.txt_srch.get().lower()))
    btn_srch.grid(row=4, column=0, padx=20, pady=10)

    self.txt_srch = Entry(frame_srch, width=60, font=('Ariel', 13))
    self.txt_srch.grid(row=4, column=1, padx=20, pady=10)

    xmsg = """
    1. Select radio button of what type of item you want to search.\n'
    2. Type in Name of item to search for. (case insensitive)\n
    3. Click the Search button.\n
    Note: Clicking Search button without specifying item Name \n
    returns all of the items of the radio button type selected.
    """
    self.tooltip(frame_srch, xmsg)
    # self.tooltip(self.txt_srch, 'Type in name of what you are searching for.   If empty, returns all rows')

    # Create frame for buttons
    frame_butts = LabelFrame(self.gui, padx=10, pady=10)
    frame_butts.grid(padx=10, pady=10)

    # btn_show_albums = Button(frame_butts, width=18, text="Show All Albums", font=('Ariel', 10),
    #                          command=lambda: self.show_all_form("albums"))
    # btn_show_albums.grid(row=0, column=0, padx=8, pady=10, sticky=(E))
    #
    # btn_show_artists = Button(frame_butts, width=18, text="Show All Artists", font=('Ariel', 10),
    #                           command=lambda: self.show_all_form("artists"))
    # btn_show_artists.grid(row=0, column=1, padx=8, pady=10, sticky=(W))
    #
    # btn_genre = Button(frame_butts, width=18, text="Show All Genre Types", font=('Ariel', 10),
    #                    command=lambda: self.show_all_form("genre"))
    # btn_genre.grid(row=0, column=2, padx=8, pady=10, sticky=(W))
    #
    # btn_media = Button(frame_butts, width=18, text="Show All Media Types", font=('Ariel', 10),
    #                    command=lambda: self.show_all_form("media"))
    # btn_media.grid(row=0, column=3, padx=8, pady=10, sticky=(W))

    btn_exit = Button(frame_butts, width=18, text="Exit", font=('Ariel', 14), command=self.gui.destroy)
    btn_exit.grid(row=1, column=0, columnspan=4, padx=250, pady=10, sticky=(W))

  def tooltip(self, what_widget, msg):
    self.what_widget = what_widget
    self.msg = msg
    mytip = Hovertip(self.what_widget, msg)

  def crud(self, thing_to_crud):
    self.thing_to_crud = thing_to_crud
    if self.thing_to_crud == 'media':
      crud = MediaType()
      crud.crud('create')

  def show_all_form(self, form_type):
    self.form_type = form_type

    if self.form_type == 'artists':
      saa = ShowAllForm('artists')
    elif self.form_type == 'albums':
      saa = ShowAllForm('albums')
    elif self.form_type == 'genre':
      saa = ShowAllForm('genre')
    elif self.form_type == 'media':
      saa = ShowAllForm('media')
    else:
      pass

  def search(self, srch_type, srch_val):
    self.srch_type = srch_type
    self.srch_val = srch_val

    if self.srch_type == 1:       # Album Search by Album Name to see if it is in the inventory
      s = Album(self.gui)
      s.search(self.srch_val)
    elif self.srch_type == 2:     # Artist Search by Artist name to see all albums associated to that Artist
      s = Artist()
      s.search(self.srch_val)
    elif self.srch_type == 3:     # Genre Search by Genre to see all Artists of the selected Genre
      s = Genre()
      s.search(self.srch_val)
    elif self.srch_type == 4:     # Media Search by Media to see all Albums of the selected Media
      s = MediaType()
      s.search(self.srch_val)
    else:
      pass

  # Display the form
  def form_display(self):
    self.gui.mainloop()
