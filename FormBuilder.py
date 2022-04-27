# Import libraries
import sqlite3
from tkinter import *

class FormBuilder:

  def __init__(self):
    self.gui = Tk()
    self.gui.geometry("900x500")
    self.gui.title('Music Collection Inventory')
    self.gui.iconbitmap('img/music.ico')
    self.state = 'readonly'
    self.fc = ''  # Alias for frame_controls
    self.fi = ''  # Alias for frame_inputs
    self.fl = ''  # Alias for frame_list
    self.e = ''

  # Allows you to create a new record
  def row_create(self):
    pass

  # Allows you to delete the current record
  def row_delete(self):
    pass

  # Allows edit mode of the current record
  def row_update(self):
    # Delete all form frames
    self.fc.destroy()
    self.fi.destroy()

    # Re-create frames with normal mode for inputs
    self.form_inputs('normal')
    self.form_controls()

  # Add text boxes to the form
  def form_controls(self):
    # Create frame for control buttons
    frame_controls = LabelFrame(self.gui, padx=10, pady=10)
    frame_controls.grid(padx=10, pady=10)

    create_button = Button(frame_controls, text="Create", command=self.row_create())
    create_button.grid(row=0, column=0, padx=20)

    update_button = Button(frame_controls, text="Update", command=self.row_update)
    update_button.grid(row=0, column=1, padx=20)

    delete_button = Button(frame_controls, text="Delete", command=self.row_delete())
    delete_button.grid(row=0, column=2, padx=20)

    exit_button = Button(frame_controls, text="Exit", command=self.gui.destroy)
    exit_button.grid(row=0, column=3, padx=20)

    self.fc = frame_controls

  # This will be a grid of data
  def form_display_data(self):
    pass

  # Add text boxes to the form
  def form_inputs(self, state):
    self.state = state

    # Create frame for input fields
    frame_inputs = LabelFrame(self.gui, padx=10, pady=10)

    lbl_artist_name = Label(frame_inputs, text="Artist Name")
    lbl_artist_name.grid(row=0, column=0)
    txt_artist_name = Entry(frame_inputs, width=40, state=self.state)
    txt_artist_name.grid(row=0, column=1, padx=20)

    lbl_album_title = Label(frame_inputs, text="Album Title")
    lbl_album_title.grid(row=1, column=0)
    txt_album_title = Entry(frame_inputs, width=40, state=self.state)
    txt_album_title.grid(row=1, column=1, padx=20)

    lbl_media_type = Label(frame_inputs, text="Media Type")
    lbl_media_type.grid(row=2, column=0)
    txt_media_type = Entry(frame_inputs, width=40, state=self.state)
    txt_media_type.grid(row=2, column=1, padx=20)

    lbl_image_url = Label(frame_inputs, text="Image URL")
    lbl_image_url.grid(row=3, column=0)
    txt_image_url = Entry(frame_inputs, width=40, state=self.state)
    txt_image_url.grid(row=3, column=1, padx=20)

    frame_inputs.grid(padx=10, pady=10)
    self.fi = frame_inputs

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
