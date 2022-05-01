# Import libraries
import sqlite3
import tkinter

from tkinter import *

class Album:

  def __init__(self):
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
    print('IM IN THE ALBUM CLASS')
    print(q)
    print(r)
