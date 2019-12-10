import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GdkPixbuf


class AlbumLabel(Gtk.VBox):

    def __init__(self, fname):
        Gtk.VBox.__init__(self)
