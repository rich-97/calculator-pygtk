# -*- coding: utf-8 -*-

from Window import Window
from helpers import *

class Calculator (Window):

  def __init__ (self, title):
    Window.__init__(self, title)
    self.create_grid()
  
    self.size_screen = (3, 1)

    self.input_box = self.Gtk.Label()
    self.input_box.set_name('input')
    self.input_box.set_xalign(0)
  
    self.output_box = self.Gtk.Label('0.')
    self.output_box.set_name('output')
    self.output_box.set_xalign(1)

    self.create_button('%', 0, 8).connect('clicked', self.on_clicked_btn)
    self.create_button('.', 1, 8).connect('clicked', self.on_clicked_btn)
    self.create_button('=', 2, 8).connect('clicked', self.on_clicked_btn)
    self.create_button('0', 0, 7).connect('clicked', self.on_clicked_btn)
    self.create_button('1', 1, 7).connect('clicked', self.on_clicked_btn)
    self.create_button('-', 2, 7).connect('clicked', self.on_clicked_btn)
    self.create_button('2', 0, 6).connect('clicked', self.on_clicked_btn)
    self.create_button('3', 1, 6).connect('clicked', self.on_clicked_btn)
    self.create_button('+', 2, 6).connect('clicked', self.on_clicked_btn)
    self.create_button('4', 0, 5).connect('clicked', self.on_clicked_btn)
    self.create_button('5', 1, 5).connect('clicked', self.on_clicked_btn)
    self.create_button('x', 2, 5).connect('clicked', self.on_clicked_btn)
    self.create_button('6', 0, 4).connect('clicked', self.on_clicked_btn)
    self.create_button('7', 1, 4).connect('clicked', self.on_clicked_btn)
    self.create_button('÷', 2, 4).connect('clicked', self.on_clicked_btn)
    self.create_button('8', 0, 3).connect('clicked', self.on_clicked_btn)
    self.create_button('9', 1, 3).connect('clicked', self.on_clicked_btn)
    self.create_button('DEL', 2, 3).connect('clicked', self.on_clicked_btn)
    self.create_button('(', 0, 2).connect('clicked', self.on_clicked_btn)
    self.create_button(')', 1, 2).connect('clicked', self.on_clicked_btn)
    self.create_button('AC', 2, 2).connect('clicked', self.on_clicked_btn)


    self.add_grid(self.input_box, 0, 0, self.size_screen)
    self.add_grid(self.output_box, 0, 1, self.size_screen)
    self.add(self.grid)
  
  def input_add_text (self, text):
    input_text = self.input_box.get_text()
    input_text += text
    self.input_box.set_text(input_text)

  def on_clicked_btn (self, button):
    text_btn = button.get_label()

    if text_btn == 'DEL':
      input_text = self.input_box.get_text()
      new_text = ''

      for i in range(0, len(input_text) - 1):
        new_text += input_text[i]
      
      self.input_box.set_text(new_text)

    elif text_btn == 'AC':
      self.input_box.set_text('')
      self.output_box.set_text('0.')

    elif text_btn == '=':
      operators = ['+', '-', '/', '*', '(', ')']
      input_text = self.input_box.get_text()
      input_text = input_text.replace('÷', '/')
      input_text = input_text.replace('x', '*')

      if '%' in input_text:
        for i in range(0, input_text.count('%')):
          index = input_text.index('%')
          number = ''

          for i in range(index, 0, -1):
            if input_text[i - 1] in operators:
              break
            else:
              number += input_text[i - 1]

          search = reverse(number) + '%'
          replace = str(float(number) / 100)
          input_text = input_text.replace(search, replace)


      self.output_box.set_text(eval_str(input_text) + '.')

    else:
      self.input_add_text(text_btn)
