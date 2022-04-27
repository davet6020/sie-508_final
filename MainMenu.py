# Import libraries
import sqlite3
from ShowAllForm import ShowAllForm
from tkinter import *

class MainMenu:

  def __init__(self):
    self.gui = Tk()
    self.gui.geometry("800x400")
    self.gui.title('Music Collection Inventory')
    self.gui.iconbitmap('img/music.ico')
    self.rb_srch = IntVar()
    self.rb_srch.set("1")
    self.main_form()

  def main_form(self):
    lbl_mm = Label(self.gui, text="Main Menu", pady=10, font=('MS Serif', 18))
    lbl_mm.grid(row=0, column=0)

    # Create frame for search controls
    frame_srch = LabelFrame(self.gui, padx=10, pady=10)
    frame_srch.grid(padx=10, pady=10)

    Radiobutton(frame_srch, text='Album', variable=self.rb_srch, value=1).grid(row=2, column=0)
    Radiobutton(frame_srch, text='Artist', variable=self.rb_srch, value=2).grid(row=2, column=1, sticky=(W))

    btn_srch = Button(frame_srch, width=15, text="Search", font=('Ariel', 10), command=self.search())
    btn_srch.grid(row=4, column=0, padx=20, pady=10)

    txt_srch = Entry(frame_srch, width=60, font=('Ariel', 13))
    txt_srch.grid(row=4, column=1, padx=20, pady=10)

    # Create frame for buttons
    frame_butts = LabelFrame(self.gui, padx=10, pady=10)
    frame_butts.grid(padx=10, pady=10)

    btn_show_albums = Button(frame_butts, width=15, text="Show All Albums", font=('Ariel', 10), command=self.show_all_albums)
    btn_show_albums.grid(row=0, column=0, padx=20, pady=10)

    btn_show_artists = Button(frame_butts, width=15, text="Show All Artists", font=('Ariel', 10), command=self.show_all_artists)
    btn_show_artists.grid(row=0, column=1, padx=20, pady=10)

    btn_exit = Button(frame_butts, width=15, text="Exit", font=('Ariel', 10), command=self.gui.destroy)
    btn_exit.grid(row=0, column=2, padx=20, pady=10, sticky=(W))

  def show_all_albums(self):
    saa = ShowAllForm('Show All Albums')
    saa.form_display()

  def show_all_artists(self):
    saa = ShowAllForm('Show All Artists')
    saa.form_display()

  def search(self):
    rbl = Label(self.gui, text=self.rb_srch.get())
    # rbl.grid(row=6)

  # Display the form
  def form_display(self):
    self.gui.mainloop()
