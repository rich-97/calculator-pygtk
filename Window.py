import gi

gi.require_version('Gtk', '3.0')

from gi.repository import Gtk

class Window (Gtk.Window):

  def __init__ (self, title):
    Gtk.Window.__init__(self, title=title)
    self.Gtk = Gtk
  
  def create_grid (self):
    self.grid = Gtk.Grid()

  def create_button (self, label, column, row):
    button = Gtk.Button(label=label)
    self.add_grid(button, column, row, (1, 1))
    return button


  def add_grid (self, widget, column, row, wh):
    self.grid.attach(widget, column, row, wh[0], wh[1])

        
