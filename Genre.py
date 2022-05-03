# Import libraries
import sqlite3
import tkinter
import tkinter.ttk
from tkinter import *


class Genre:

  def __init__(self):
    self.g_frame = Tk()
    self.title = 'Show All Genre Types'
    self.g_frame.title(self.title)
    self.g_frame.iconbitmap('img/music.ico')
    self.g_frame.geometry("900x750")

    self.g_tree = tkinter.ttk.Treeview(self.g_frame, height=30, padding=4)
    # Tree Columns
    self.g_tree['columns'] = ('Genre Name',)
    self.g_tree.column('#0', width=0, stretch=NO)
    self.g_tree.column('Genre Name', anchor=W, width=200)

    # Tree Headings
    self.g_tree.heading('#0', text="", anchor=W)
    self.g_tree.heading('Genre Name', text='Genre Name', anchor=W)

    self.item = ''
    self.btn_exit = ''
    self.btn_create = ''
    self.btn_delete = ''
    self.btn_save = ''
    self.btn_update = ''
    self.srch_val = ''
    self.conn = sqlite3.connect('db/MusicInventory.db')
    self.c = self.conn.cursor()

  def search(self, srch_val):

    if len(srch_val) < 1:
      q = """select g.GenreName, g.oid from Genre as g order by g.GenreName"""
    else:
      self.srch_val = srch_val
      q = """select g.GenreName, g.oid from Genre as g where lower(g.GenreName) = '""" + str(self.srch_val) + "' order by g.GenreName"
      print(q)

    r = self.c.execute(q).fetchall()
    self.show(r)

  def show(self, rows):
    for i in range(len(rows)):
      self.g_tree.insert(parent='', index='end', iid=i, values=(rows[i]))

    self.g_tree.grid(padx=20, pady=20)

    self.btn_exit = Button(self.g_frame, text='Exit', font=('Ariel', 14), command=self.g_frame.destroy)
    self.btn_create = Button(self.g_frame, text='Create', command=self.create)
    self.btn_delete = Button(self.g_frame, text='Delete', command=self.delete)
    self.btn_update = Button(self.g_frame, text='Update', command=self.update)

    self.btn_create.grid(row=1, column=2, padx=5)
    self.btn_delete.grid(row=1, column=4, padx=5)
    self.btn_exit.grid(row=1, column=0, padx=10)
    self.btn_update.grid(row=1, column=5, padx=5)

  def create(self):
    self.btn_delete.after(10, self.btn_delete.destroy)
    self.btn_update.after(10, self.btn_update.destroy)

    e = Entry(self.g_frame, width=40, fg='black', font=('Arial', 12))
    e.grid(row=1, column=3, sticky=(W))
    btn_save = Button(self.g_frame, text='Save', command=lambda: self.create_item(e.get()))
    btn_save.grid(row=1, column=7, padx=5)

  def create_item(self, item):
    self.item = item
    i = """insert into Genre(GenreName) values('""" + self.item + "')"
    r = self.c.execute(i)
    self.conn.commit()
    self.destroy_window()

  def delete(self):
    selected = self.g_tree.focus()
    if '' == selected:
      return

    temp = self.g_tree.item(selected, 'values')

    d = """delete from Genre where GenreID = """ + temp[1]
    r = self.c.execute(d)
    self.conn.commit()
    self.destroy_window()

  def update(self):
    selected = self.g_tree.focus()
    if '' == selected:
      return

    self.btn_create.after(10, self.btn_create.destroy)
    self.btn_delete.after(10, self.btn_delete.destroy)

    temp = self.g_tree.item(selected, 'values')
    e = Entry(self.g_frame, width=40, fg='black', font=('Arial', 12))
    e.insert(0, temp[0])
    e.grid(row=1, column=6, sticky=(W))
    oid = temp[1]
    btn_save = Button(self.g_frame, text='Save', command=lambda: self.update_item(e.get(), oid))
    btn_save.grid(row=1, column=7, padx=5)

  def update_item(self, item, oid):
    self.item = item
    u = """update Genre set GenreName = '""" + self.item + """' where GenreId = """ + oid

    r = self.c.execute(u)
    self.conn.commit()
    self.destroy_window()

  def destroy_window(self):
    self.g_frame.destroy()
