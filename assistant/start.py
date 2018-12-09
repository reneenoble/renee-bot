from . import no_query

def on_enter(data, output=print):
  output('Welcome!')
  output('Ask me a question!')

def on_input(input_data, data, output=print):
  return no_query.on_input(input_data, data, output)
