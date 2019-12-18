import gi

from gui.album.album_label import AlbumLabel
from gi.repository import Gtk

from gui.album.selected_album_view import SelectedAlbum

gi.require_version('Gtk', '3.0')


def generate_list():
    album_list = []
    for i in range(50):
        if i != 27:
            album_list.append(AlbumLabel("Battle Born", "gui/folder.jpg"))
        else:
            album_list.append(AlbumLabel("Direct Hits", "gui/folder2.jpg"))
    return album_list


class MainGrid(Gtk.ScrolledWindow):

    def __init__(self):
        Gtk.ScrolledWindow.__init__(self)
        self.set_border_width(6)

        self.resizing = True

        self.album_list = generate_list()

        self.contents = Gtk.VBox()

        self.first_half = Gtk.FlowBox()
        self.first_half.set_max_children_per_line(30)
        self.first_half.set_valign(Gtk.Align.START)
        self.first_half.set_selection_mode(Gtk.SelectionMode.NONE)

        self.selected_album = SelectedAlbum("gui/folder.jpg")

        self.second_half = Gtk.FlowBox()
        self.second_half.set_max_children_per_line(30)
        self.second_half.set_valign(Gtk.Align.START)
        self.second_half.set_selection_mode(Gtk.SelectionMode.NONE)

        self.add_components()

        self.contents.pack_start(self.first_half, True, True, 0)
        self.contents.pack_start(self.selected_album, True, False, 0)
        self.contents.pack_start(self.second_half, True, True, 0)

        self.add(self.contents)

        self.resizing = False

    def resize(self):
        if self.resizing:
            return
        self.resizing = True
        self.remove_components()
        self.add_components()
        self.resizing = False

    def add_components(self):
        allocated_width = 1673  # self.first_half.get_allocated_width()
        num_cols = int(allocated_width / 200)
        selected_index = 27
        num_first_half = int(selected_index + num_cols - (selected_index % num_cols))

        print('num_cols: ' + str(num_cols))
        print('num_first: ' + str(num_first_half))

        for album in self.album_list[0:num_first_half]:
            self.first_half.add(album)

        print('first: ' + str(len(self.first_half.get_children())))

        for album in self.album_list[num_first_half:]:
            self.second_half.add(album)

        print('second: ' + str(len(self.second_half.get_children())))

    def remove_components(self):
        for child in self.first_half.get_children():
            self.first_half.remove(child)
        print('num_left => ' + str(len(self.first_half.get_children())))
        for child in self.selected_album.get_children():
            self.selected_album.remove(child)
