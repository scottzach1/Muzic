import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class MainGrid(Gtk.FlowBox):

    def __init__(self):
        Gtk.FlowBox.__init__(self)
        self.set_valign(Gtk.Align.START)
        self.set_max_children_per_line(30)
        self.set_selection_mode(Gtk.SelectionMode.NONE)

        self.populate_flowbox()

    def populate_flowbox(self):
        button_label = 'Button'

        for i in range(50):
            button = Gtk.Label(label=button_label)
            self.add(button)
