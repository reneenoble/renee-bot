import assistant

def prompt():
  '''The prompt for the commandline interface of the assistant.'''
  return input('> ')

def run(state, data):
  '''Run through an assistants' conversation.'''
  while state != 'END':
    # Do something based on the state
    assistant.on_enter(state, data, output=print)
    # Change the conversation state based on a prompt 
    state, data = assistant.on_input(state, data, output=print, get_input=prompt)

if __name__ == '__main__':
  state = 'START'
  data = None

  run(state, data)
