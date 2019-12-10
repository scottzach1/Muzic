import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GdkPixbuf


class AlbumLabel(Gtk.VBox):

    def __init__(self, fname):
        Gtk.VBox.__init__(self)

        pix_buf = GdkPixbuf.Pixbuf.new_from_file_at_scale(
            filename=fname,
            width=200,
            height=200,
            preserve_aspect_ratio=True
        )

        self.image = Gtk.Image.new_from_pixbuf(pix_buf)
        self.label = Gtk.Label(label="Battle Born\nThe Killers")

        self.pack_start(self.image, True, True, 0)
        self.pack_end(self.label, True, True, 0)
