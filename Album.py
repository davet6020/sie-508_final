# Import libraries
import sqlite3
import tkinter.ttk
from tkinter import *
from PIL import ImageTk, Image
from urllib.request import urlopen
from io import BytesIO

class Album:

  def __init__(self):
    self.al_frame = Tk()
    self.title = 'Show All Albums'
    self.al_frame.title(self.title)
    self.al_frame.iconbitmap('img/music.ico')
    self.al_frame.geometry("150x150")

    self.al_tree = tkinter.ttk.Treeview(self.al_frame, height=30, padding=4)
    # Tree Columns
    self.al_tree['columns'] = ('Album Title',)
    self.al_tree.column('#0', width=0, stretch=NO)
    self.al_tree.column('Album Title', anchor=W, width=300)

    # Tree Headings
    self.al_tree.heading('#0', text="", anchor=W)
    self.al_tree.heading('Album Title', text='Album Title', anchor=W)

    self.album_title = ''
    self.artist_name = ''
    self.mediatype_name = ''
    self.artist_id = ''
    self.mediatype_id = ''
    self.image_url = ''
    self.drop_artist_name = ''
    self.drop_mediatype_name = ''
    self.r1 = ''
    self.r2 = ''
    self.clicked_artist_name = StringVar()
    self.clicked_mediatype_name = StringVar()

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
      q = """select al.AlbumTitle, al.oid from Album as al order by al.AlbumTitle"""
      r = self.c.execute(q).fetchall()
      self.show(r)
    else:
      self.srch_val = srch_val
      q = """select al.AlbumTitle, ar.ArtistName, m.MediaTypeName, al.ImageURL from Album as al, Artist as ar, MediaType as m
          where  al.ArtistId = ar.ArtistId and al.MediaTypeId = m.MediaTypeId and lower(al.AlbumTitle) = '""" + str(self.srch_val) + "' order by al.AlbumTitle"

      r = self.c.execute(q).fetchall()
      self.show_nice(r)

  def show_nice(self, rows):
    for i in range(len(rows)):
      al_name = rows[i][0]
      ar_name = rows[i][1]
      m_name = rows[i][2]
      al_img = rows[i][3]

    lbl_album_title1 = Label(font=('Ariel', 14), text="Album Title: ")
    lbl_album_title1.grid(row=1, column=1)
    lbl_album_title2 = Label(font=('Ariel', 14), text=al_name)
    lbl_album_title2.grid(row=1, column=2)

    lbl_artist_title1 = Label(self.al_frame, font=('Ariel', 14), text="Artist Name: ")
    lbl_artist_title1.grid(row=2, column=1)
    lbl_artist_title2 = Label(self.al_frame, font=('Ariel', 14), text=ar_name)
    lbl_artist_title2.grid(row=2, column=2)

    lbl_media_type1 = Label(self.al_frame, font=('Ariel', 14), text="Media Type: ")
    lbl_media_type1.grid(row=3, column=1)
    lbl_media_type2 = Label(self.al_frame, font=('Ariel', 14), text=m_name)
    lbl_media_type2.grid(row=3, column=2)

    u = urlopen(al_img)
    raw_data = u.read()
    u.close()

    im = Image.open(BytesIO(raw_data))
    photo = ImageTk.PhotoImage(im.resize((200, 200), Image.ANTIALIAS))

    label = Label(image=photo)
    label.image = photo
    label.grid()

  def show(self, rows):
    for i in range(len(rows)):
      self.al_tree.insert(parent='', index='end', iid=i, values=(rows[i]))

    self.al_tree.grid(padx=20, pady=20)

    self.btn_exit = Button(self.al_frame, text='Exit', font=('Ariel', 14), command=self.al_frame.destroy)
    self.btn_create = Button(self.al_frame, text='Create', command=self.create)
    self.btn_delete = Button(self.al_frame, text='Delete', command=self.delete)
    self.btn_update = Button(self.al_frame, text='Update', command=self.update)

    self.btn_create.grid(row=1, column=2, padx=5)
    self.btn_delete.grid(row=1, column=4, padx=5)
    self.btn_exit.grid(row=1, column=0, padx=10)
    self.btn_update.grid(row=1, column=5, padx=5)

  def create(self):
    self.btn_create.after(10, self.btn_create.destroy)
    self.btn_delete.after(10, self.btn_delete.destroy)
    self.btn_update.after(10, self.btn_update.destroy)

    lbl_album_title = Label(self.al_frame, text="Album Title")
    lbl_album_title.grid(row=1, column=1)
    ent_album_title = Entry(self.al_frame, width=40, fg='black', font=('Arial', 12))
    ent_album_title.grid(row=1, column=3, sticky=(W))

    lbl_image_url = Label(self.al_frame, text="Image URL")
    lbl_image_url.grid(row=2, column=1)
    ent_image_url = Entry(self.al_frame, width=40, fg='black', font=('Arial', 12))
    ent_image_url.grid(row=2, column=3, sticky=(W))

    q1 = """select ar.ArtistName, ar.oid from Artist as ar order by ar.ArtistName"""
    self.r1 = self.c.execute(q1).fetchall()

    options_artist_name = []
    for i in range(len(self.r1)):
      options_artist_name.append(self.r1[i][0])

    q2 = """select m.MediaTypeName, m.oid from MediaType as m order by m.MediaTypeName"""
    self.r2 = self.c.execute(q2).fetchall()

    options_mediatype_name = []
    for i in range(len(self.r2)):
      options_mediatype_name.append(self.r2[i][0])

    # Create Dropdown menu for Artist Name
    lbl_artist = Label(self.al_frame, text="Artist")
    lbl_artist.grid(row=3, column=1)
    self.drop_artist_name = OptionMenu(self.al_frame, self.clicked_artist_name, *options_artist_name, command=self.get_artist_dropdown_val)
    self.drop_artist_name.grid(row=3, column=3, sticky=(W))

    # Create Dropdown menu for MediaType Name
    lbl_mediatype = Label(self.al_frame, text="MediaType")
    lbl_mediatype.grid(row=4, column=1)
    self.drop_mediatype_name = OptionMenu(self.al_frame, self.clicked_mediatype_name, *options_mediatype_name, command=self.get_mediatype_dropdown_val)
    self.drop_mediatype_name.grid(row=4, column=3, sticky=(W))

    btn_save = Button(self.al_frame, text='Save', command=lambda: self.create_item(ent_album_title.get(), ent_image_url.get()))
    btn_save.grid(row=1, column=7, padx=5)

  def get_artist_dropdown_val(self, choice):
    self.artist_name = self.clicked_artist_name.get()

  def get_mediatype_dropdown_val(self, choice):
    self.mediatype_name = self.clicked_mediatype_name.get()

  def create_item(self, album_title, image_url):
    self.album_title = album_title
    self.image_url = image_url

    # Find the artist_name in the list called r1, so I can get the artist_id
    match = [match for match in self.r1 if self.artist_name in match]
    for i in match:
      key = i[0]
      val = i[1]

    self.artist_id = val

    # Find the mediatype_name in the list called r2, so I can get the genre_id
    match = [match for match in self.r2 if self.mediatype_name in match]
    for i in match:
      key = i[0]
      val = i[1]

    self.mediatype_id = val

    i = "insert into Album(AlbumTitle, ArtistId, ImageURL, MediaTypeId) values('{}', {}, '{}', {})".format(self.album_title, self.artist_id, self.image_url, self.mediatype_id)

    r = self.c.execute(i)
    self.conn.commit()
    self.destroy_window()

  def delete(self):
    selected = self.al_tree.focus()
    if '' == selected:
      return

    temp = self.al_tree.item(selected, 'values')

    d = """delete from Album where AlbumID = """ + temp[1]
    r = self.c.execute(d)
    self.conn.commit()
    self.destroy_window()

  def update(self):
    selected = self.al_tree.focus()
    if '' == selected:
      return

    self.btn_create.after(10, self.btn_create.destroy)
    self.btn_delete.after(10, self.btn_delete.destroy)

    temp = self.al_tree.item(selected, 'values')
    e = Entry(self.al_frame, width=40, fg='black', font=('Arial', 12))
    e.insert(0, temp[0])
    e.grid(row=1, column=6, sticky=(W))
    oid = temp[1]
    btn_save = Button(self.al_frame, text='Save', command=lambda: self.update_item(e.get(), oid))
    btn_save.grid(row=1, column=7, padx=5)

  def update_item(self, item, oid):
    self.item = item
    u = """update Album set AlbumTitle = '""" + self.item + """' where AlbumId = """ + oid

    r = self.c.execute(u)
    self.conn.commit()
    self.destroy_window()

  def destroy_window(self):
    self.al_frame.destroy()
