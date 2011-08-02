import gtk, pygtk
import gobject
import pynotify

from Pymodoro import *

class Gui:

    def on_window_destroy(self, widget):
        gtk.main_quit()

    def status_clicked(self, widget):
        """docstring for status_clicked"""
        self.window.show_all()

    def delete_event(self, window, event):
        """docstring for delete_event"""
        self.window.hide_on_delete()

    def show_about_dialog(self):
        """docstring for show_about_dialog"""
        dialog = gtk.MessageDialog(
        parent         = None,
        flags          = gtk.DIALOG_DESTROY_WITH_PARENT,
        type           = gtk.MESSAGE_INFO,
        buttons        = gtk.BUTTONS_CLOSE,
        message_format = "Do you want to close this Status Icon program?")
        dialog.set_title('Popup Window')
        dialog.connect('response', self.destroyer)
        dialog.show() 

    def popup(self, button, widget, data=None):
        self.menu = gtk.Menu()

        about = gtk.MenuItem()
        about.set_label("About")
        quit = gtk.MenuItem()
        quit.set_label("Quit")

        about.connect("activate", self.show_about_dialog)
        quit.connect("activate", gtk.main_quit)

        self.menu.append(about)
        self.menu.append(quit)

        self.menu.show_all()

    def update_labels(self):
        """Update labels on the gui"""
        self.num_pomodoros_label.set_text(str(self.pymodoro.num_pomodoros) + " pomodoros completed")
        self.num_big_breaks_label.set_text(str(self.pymodoro.num_big_breaks) + " extended breaks taken")
        remaining_time = self.pymodoro.current_clock.time
        minutes = remaining_time / 60
        seconds = remaining_time % 60
        self.time_left_label.set_text("%d:%s remaining" % (minutes, str(seconds).rjust(2,'0')))  
        return True

    def notify_expiry(self,message,title):
        """docstring for notify_expiry"""
        n = pynotify.Notification(title, message)
        n.show()

    def __init__(self):
        """docstring for __init__"""
        self.pymodoro = Pymodoro(self)

        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.set_size_request(400,300)
        self.window.set_title("Pymodoro")

        self.main_box = gtk.VBox(False, 5)
        self.bottom_box = gtk.HBox(False, 5)
        self.info_box = gtk.VBox(False, 5)

        self.start_pomodoro_button = gtk.Button("Start a pomodoro...")
        self.start_pomodoro_button.connect('clicked', self.pymodoro.start_pomodoro)

        self.time_left_label = gtk.Label("0:00 remaining")
        self.num_pomodoros_label = gtk.Label("0 pomodoros completed")
        self.num_big_breaks_label = gtk.Label("0 extended breaks taken")

        self.window.add(self.main_box)
        self.main_box.pack_start(self.start_pomodoro_button)
        self.main_box.pack_start(self.bottom_box)
        self.bottom_box.pack_start(self.time_left_label)
        self.bottom_box.pack_start(self.info_box)
        self.info_box.pack_start(self.num_pomodoros_label)
        self.info_box.pack_start(self.num_big_breaks_label)

        self.clock_timer = gobject.timeout_add(1000, self.pymodoro.update_clocks)
        self.gui_timer = gobject.timeout_add(1000, self.update_labels)

        pynotify.init("Pymodoro")
        self.status_icon = gtk.status_icon_new_from_stock(gtk.STOCK_GOTO_TOP)
        self.status_icon.connect('activate', self.status_clicked)
        self.status_icon.connect('popup-menu', self.popup)
        self.window.connect('delete-event', self.delete_event)
        # self.window.connect("destroy", self.on_window_destroy)
        self.window.show_all()

def start():
    """Start pymodoro"""
    gui = Gui()
    gtk.main()

if __name__ == "__main__":
    start()
