from . import start 
from . import no_query
from . import query 
from . import statement

states = {
  'START': start,
  'NO QUERY': no_query,
  'QUERY': query,
  'STATEMENT': statement,
  'CAT': cat,
}

def on_enter(state, data, output=print):    
  state_actions = states[state]
  state_actions.on_enter(data, output)

def on_input(state, data, output=print, get_input=input):
  state_actions = states[state]
  input_data = get_input()
  return state_actions.on_input(input_data, data, output)
