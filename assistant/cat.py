from . import no_query

import re

def on_enter(statement, output=print):
  output("Oh a kitty!!")

def on_input(input_data, question, output=print):
  return no_query.on_input(input_data, None, output)
