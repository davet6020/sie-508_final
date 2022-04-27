# Import libraries
import sqlite3
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

    btn_show_albums = Button(frame_butts, width=15, text="Show All Albums", font=('Ariel', 10), command=self.show_all_albums())
    btn_show_albums.grid(row=0, column=0, padx=20, pady=10)

    btn_show_artists = Button(frame_butts, width=15, text="Show All Artists", font=('Ariel', 10), command=self.show_all_albums())
    btn_show_artists.grid(row=0, column=1, padx=20, pady=10)

    btn_exit = Button(frame_butts, width=15, text="Exit", font=('Ariel', 10), command=self.gui.destroy)
    btn_exit.grid(row=0, column=2, padx=20, pady=10, sticky=(W))

  def show_all_albums(self):
    pass

  def search(self):
    rbl = Label(self.gui, text=self.rb_srch.get())
    # rbl.grid(row=6)

  # Add text boxes to the form
  def form_list(self):
    # Create frame for input fields
    frame_list = LabelFrame(self.gui, padx=10, pady=10)

    conn = sqlite3.connect('db/MusicInventory.db')
    c = conn.cursor()

    v_albums = """select al.AlbumTitle, ar.ArtistName, m.MediaTypeName from Album as al, Artist as ar, MediaType
    as m where al.ArtistId = ar.ArtistId and al.MediaTypeId = m.MediaTypeId order by ar.ArtistName, al.AlbumTitle"""
    rows = c.execute(v_albums).fetchall()

    # find total number of rows and
    # columns in list
    total_rows = len(rows)
    total_cols = len(rows[0])

    print('total_rows: {}'.format(total_rows))
    print('total_columns: {}'.format(total_cols))

    # code for creating table
    for i in range(total_rows):
      for j in range(total_cols):
        self.e = Entry(frame_list, width=30, fg='black', font=('Arial', 12))

        self.e.grid(row=i, column=j)
        self.e.insert(END, rows[i][j])

    frame_list.grid(padx=10, pady=10)
    self.fl = frame_list

  # Display the form
  def form_display(self):
    self.gui.mainloop()
