"""
This is the main program that when you run it, it loads the application
"""

# Import external modules
import config
from FormBuilder import FormBuilder
from MainMenu import MainMenu

# Import libraries
import sqlite3

main_menu = MainMenu()
main_menu.form_display()

# mci = FormBuilder()
# # mci.form_inputs('readonly') # Choices are: disabled, normal, or readonly
# # mci.form_controls()
# mci.form_list()



# Create two frames, one for input fields
# frame_inputs = LabelFrame(gui, padx=10, pady=10)
# frame_inputs.pack(padx=10, pady=10)
#
# # The other frame is for buttons and drop-downs
# frame_controls = LabelFrame(gui, padx=10, pady=10)
# frame_controls.pack(padx=10, pady=10)
#
# e = Entry(frame_inputs, width=50)
# e.grid(row=0, column=0)

# myLabel1 = Label(root, text="Hello World!")
# myLabel2 = Label(root, text="My name is Slim Shady.")
# myLabel1.grid(row=0, column=0)
# myLabel2.grid(row=1, column=2)

# exit_button = Button(frame_controls, text="Exit", command=gui.destroy)
# exit_button.grid(row=0, column=0)
# gui.mainloop()

conn = sqlite3.connect('db/MusicInventory.db')
c = conn.cursor()

# cursor.execute("INSERT INTO pictures VALUES (nextval('serial'), 'img/hammer.jpg')")
# int(cursor.execute("SELECT * FROM album").fetchall())


v_albums = """select al.oid, al.AlbumTitle, ar.ArtistName, m.MediaTypeName from Album as al, Artist as ar, MediaType as m
where al.ArtistId = ar.ArtistId and al.MediaTypeId = m.MediaTypeId"""
print(c.execute(v_albums).fetchall())

v_artists = """select ar.oid, ar.ArtistName, g.GenreName from Artist as ar, Genre as g
where ar.GenreID = g.GenreId"""
# print(c.execute(v_artists).fetchall())

# Fetch one record
# fetchone()

# If we ever commit something
# conn.commit()

# Close DB connection
conn.close()
