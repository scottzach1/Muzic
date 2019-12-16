import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GdkPixbuf


class SelectedAlbum(Gtk.Frame):

    def __init__(self, fname):
        Gtk.VBox.__init__(self)
        self.set_border_width(6)

        self.album_contents = Gtk.HBox()

        # Contains Album Heading and song list.
        self.header_splitter = Gtk.VBox()

        self.header = Gtk.Label()
        self.header.set_markup("<b>The Killers - Greatest Hits</b>\n")
        self.header.set_halign(Gtk.Align.START)

        # Splits song list into cols.
        self.track_list = self.generate_songs()

        self.header_splitter.add(self.header)
        self.header_splitter.add(self.track_list)
        self.header_splitter.set_hexpand(True)

        # Adds album art.
        self.album_art = self.generate_album_art("gui/folder.jpg")
        self.album_art.set_halign(Gtk.Align.END)

        # Add components to main view.
        self.album_contents.pack_start(self.header_splitter, True, True, 18)
        self.album_contents.pack_start(self.album_art, False, False, 0)
        self.add(self.album_contents)

        # Change bg color.
        self.override_colors()

    def override_colors(self):
        button = Gtk.Button()
        color = button.get_style_context().get_background_color(Gtk.StateFlags.NORMAL)
        self.override_background_color(self.get_state(), color)

    @staticmethod
    def generate_songs():
        colum_box = Gtk.HBox()

        track_cols = []

        for i in range(3):
            track_cols.append(Gtk.VBox())

        for col_no in range(len(track_cols)):
            col = track_cols[col_no]

            for track_no in range(1, 7):
                song_label = SongLabel(track_no)
                col.pack_start(song_label, True, True, 3)

            colum_box.pack_start(col, True, True, 0)
            colum_box.set_valign(Gtk.Align.START)

            if col_no + 1 != len(track_cols):
                padding = Gtk.Label()
                padding.set_markup("\t")
                colum_box.pack_start(padding, False, False, 0)

        return colum_box

    def generate_album_art(self, fname):
        pix_buf = GdkPixbuf.Pixbuf.new_from_file_at_scale(
            filename=fname,
            width=200,
            height=200,
            preserve_aspect_ratio=True
        )
        return Gtk.Image.new_from_pixbuf(pix_buf)


class SongLabel(Gtk.HBox):

    def __init__(self, track_no):
        Gtk.HBox.__init__(self)

        self.track_no = Gtk.Label()
        self.track_no.set_markup(str(track_no) + "  ")
        self.track_no.set_halign(Gtk.Align.START)

        self.track_name = Gtk.Label()
        self.track_name.set_markup("Mr Brightside")
        self.track_name.set_halign(Gtk.Align.START)

        self.track_duration = Gtk.Label()
        self.track_duration.set_markup("5:34")
        self.track_duration.set_halign(Gtk.Align.END)

        self.pack_start(self.track_no, False, False, 0)
        self.pack_start(self.track_name, True, True, 0)
        self.pack_start(self.track_duration, True, True, 0)
