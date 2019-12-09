import gi

from gui.label import AlbumLabel

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GdkPixbuf


class MainGrid(Gtk.ScrolledWindow):

    def __init__(self):
        Gtk.ScrolledWindow.__init__(self)

        self.flowbox = Gtk.FlowBox()
        self.flowbox.set_valign(Gtk.Align.START)
        self.flowbox.set_max_children_per_line(30)
        self.flowbox.set_selection_mode(Gtk.SelectionMode.NONE)

        self.populate_flowbox()

        self.add(self.flowbox)

    def populate_flowbox(self):
        button_label = 'Button'

        for i in range(100):
            self.flowbox.add(AlbumLabel())


