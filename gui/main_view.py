import gi

from gui.album.album_label import AlbumLabel
from gi.repository import Gtk

from gui.album.selected_album_view import SelectedAlbum

gi.require_version('Gtk', '3.0')


class MainGrid(Gtk.ScrolledWindow):

    def __init__(self):
        Gtk.ScrolledWindow.__init__(self)
        self.set_border_width(6)

        self.contents = Gtk.VBox()

        self.first_half = Gtk.FlowBox()
        self.first_half.set_valign(Gtk.Align.START)
        self.first_half.set_max_children_per_line(30)
        self.first_half.set_selection_mode(Gtk.SelectionMode.NONE)

        self.populate_flowbox(self.first_half, "gui/folder.jpg")
        self.contents.pack_start(self.first_half, True, True, 0)

        self.second_half = Gtk.FlowBox()
        self.second_half.set_valign(Gtk.Align.START)
        self.second_half.set_max_children_per_line(30)
        self.second_half.set_selection_mode(Gtk.SelectionMode.NONE)

        self.selected_album = SelectedAlbum("gui/folder.jpg")
        self.contents.pack_start(self.selected_album, True, True, 0)

        self.populate_flowbox(self.second_half, "gui/folder2.jpg")
        self.contents.pack_start(self.second_half, True, True, 0)

        self.add(self.contents)

    def populate_flowbox(self, flowbox, fname):
        for i in range(15):
            flowbox.add(AlbumLabel(fname))
