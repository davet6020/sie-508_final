# Import libraries
import sqlite3
from tkinter import *

class ShowAllForm:

  def __init__(self, title):
    self.show_all_form = Tk()
    self.show_all_form.geometry("900x500")
    self.title = title
    self.show_all_form.title(self.title)
    self.show_all_form.iconbitmap('img/music.ico')

    # self.main_form()

  def main_form(self):
    lbl_mm = Label(self.show_all_form, text=self.title, pady=10, font=('MS Serif', 18))
    lbl_mm.grid(row=0, column=0)

  def show_all_albums(self):
    pass

  # Display the form
  def form_display(self):
    self.show_all_form.mainloop()
