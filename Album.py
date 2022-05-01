class Album:

  def __init__(self, srch_val):
    self.srch_val = srch_val

  def search(self, srch_val):
    # rbl = Label(self.gui, text=self.rb_srch.get())
    self.srch_val = srch_val

    q = """select al.AlbumTitle, ar.ArtistName, m.MediaTypeName from Album as al, Artist as ar, MediaType as m
          where al.ArtistId = ar.ArtistId and al.MediaTypeId = m.MediaTypeId and ar.ArtistName = '""" + str(
      self.srch_val) + "'"

    r = self.c.execute(q).fetchall()
    # rows = [self.columns] + r
    print('IN THE ALBUM CLASS')
    print(q)
    print(r)
