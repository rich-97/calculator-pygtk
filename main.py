#!/usr/bin/env python

import gi
from Calculator import Calculator

gi.require_version('Gtk', '3.0')

from gi.repository import Gtk, Gdk

style_provider = Gtk.CssProvider()

css = open('main.css', 'rb')
css_data = css.read()
css.close()

style_provider.load_from_data(css_data)

Gtk.StyleContext.add_provider_for_screen(
    Gdk.Screen.get_default(), 
    style_provider,
    Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
)

app = Calculator('Calculator')
app.connect('delete-event', Gtk.main_quit)
app.show_all()
Gtk.main()
