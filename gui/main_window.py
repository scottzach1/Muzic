import gi

from gui.main_view import MainGrid

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class MainWindow(Gtk.Window):

    def __init__(self, scrolled=None):
        Gtk.Window.__init__(self, title="Muzic")
        self.set_border_width(10)
        self.set_default_size(1500, 950)

        header = Gtk.HeaderBar(title="Muzic")
        header.set_subtitle("A Simple Muzic Player")
        header.props.show_close_button = True

        self.set_titlebar(header)

        self.main_grid = MainGrid()

        self.add(self.main_grid)
        self.show_all()