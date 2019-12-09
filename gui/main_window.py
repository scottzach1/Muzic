import gi

from gui.main_view import MainGrid

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class MainWindow(Gtk.Window):

    def __init__(self, scrolled=None):
        Gtk.Window.__init__(self, title="Muzic")

        self.main_grid = MainGrid()

        self.add(self.main_grid)