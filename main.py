import gi

from gui.main_window import MainWindow

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

def resized(window):
    print("I have resized.")

win = MainWindow()
win.connect("destroy", Gtk.main_quit)
# win.connect('check-resize', resized)
win.show_all()
Gtk.main()
