# -*- coding: utf-8 -*-

from Window import Window
from helpers import *

class Calculator (Window):

  def __init__ (self, title):
    Window.__init__(self, title)
    self.create_grid()
    self.size_screen = (3, 1)
    self.buttons = '% . = 0 1 - 2 3 + 4 5 x 6 7 ÷ 8 9 DEL ( ) AC'.split()
    self.input_box = self.Gtk.Label()
    self.input_box.set_name('input')
    self.input_box.set_xalign(0)
    self.output_box = self.Gtk.Label('0.')
    self.output_box.set_name('output')
    self.output_box.set_xalign(1)
    
    count = 0
    for i in xrange(8, 1, -1):
      for j in xrange(0, 3):
        btn = self.create_button(self.buttons[count], j, i)
        btn.connect('clicked', self.on_clicked_btn)
        count += 1

    self.add_grid(self.input_box, 0, 0, self.size_screen)
    self.add_grid(self.output_box, 0, 1, self.size_screen)
    self.add(self.grid)
  
  def input_add_text (self, text):
    input_text = self.input_box.get_text()
    input_text += text
    self.input_box.set_text(input_text)

  def on_clicked_btn (self, button):
    operators = '+ - / * ( )'.split()
    text_btn = button.get_label()

    if text_btn == 'DEL':
      input_text = self.input_box.get_text()
      new_text = ''

      for i in xrange(0, len(input_text) - 1):
        new_text += input_text[i]
      
      self.input_box.set_text(new_text)

    elif text_btn == 'AC':
      self.input_box.set_text('')
      self.output_box.set_text('0.')

    elif text_btn == '=':
      input_text = self.input_box.get_text()
      input_text = input_text.replace('÷', '/')
      input_text = input_text.replace('x', '*')

      if '%' in input_text:
        for i in xrange(0, input_text.count('%')):
          index = input_text.index('%')
          number = ''

          for i in xrange(index, 0, -1):
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
